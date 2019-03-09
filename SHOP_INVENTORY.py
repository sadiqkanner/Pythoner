try:
    import cv2
except:
    print("CV2 not Import ")
import shelve
from tkinter import *
import time


def Show_Image(no):
    
    image = cv2.imread('C:\\Users\sadiq\Desktop\Images\ img'+str(no)+'.png')

    cv2.imshow('Image Name',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def Display(records,today,no):
    
    header="""
    PEN AND PAPER SHOP
    Cell#  0218838388
    DHA COMMERCIAL AREA PHASE-6
    Date : """+str(today.date())+"""  
          
    """'PRICE'.ljust(1)+""" """+'QTY'.center(15)+""" """+'AMOUNT'.ljust(10)+"""
    ----------------------------"""
    
    print(header)
    grand =[]
    for i in range(len(records)):
        
        x = records[i].split()
        Recipe_no = x[2]
        
        if x[2] ==no:
            
            m = x[10]
            tt = int(m)
            grand = grand + [tt]
            body =x[7].ljust(1)+" "+x[9].center(15)+" "+str(x[10])
            print("\t",body)

    gt="""    ----------------------------
    """+'TOTAL'.ljust(17)+""" """+str(sum(grand))+"""
    """
    print(gt)



def Printer(records,today,no):
    
    
    header="""           PEN AND PAPER 
    
    Date : """+str(today.date())+"""
    """'No:'+no+"""
           
    """'PRICE'.ljust(1)+""" """+'QTY'.center(15)+""" """+'AMOUNT'.ljust(5)+"""\n---------------------------------
    """
    
    grand =[]
    b=[]
    for i in range(len(records)):
        x = records[i].split()
        Recipe_no = x[2]
        if Recipe_no == no:
            m = x[10]
            tt = int(m)
            grand = grand + [tt]
            body =" "+x[7].ljust(2)+" "+x[9].center(18)+" "+str(x[10]+" ")
            
            b=b+[body]

            
            
    gt="""---------------------------------
    """+'TOTAL'.ljust(20)+""" """+str(sum(grand))+"""
    
    """'CELL: 021-8838388 '"""
    """'ITTEHAD COMMERICAL DHA'"""
    """
    x='\n    '.join(b)

    yy=(header+x+gt)
    baconFile = open('D:\\Records\Recipe_temp_file.txt', 'w')
    
    baconFile.write(yy)
    
    import os
    fd = os.startfile('D:\\Records\Recipe_temp_file.txt', 'print')
    baconFile.close()
    



import time
import shelve
from datetime import datetime, timedelta

shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
Toyes_Records = shelfFile['Toyes_Record']
shelfFile.close()

shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Shop_Data')
records = shelfFile['SHOP']
shelfFile.close()

barcodes=['1000000011241','1000000011296','1000000011289','1000000011265','1000000011234','1000000011319','1000000011258','1000000011302','1000000011272','1000000011364','1000000011371','1000000011388']

today = datetime.now()

while True:
    
    k = len(records)
    g = records[k-1]
    x = g.split()
    no = x[2]
    rt=-1

    barcode = input('1: Display Result : \t \n2: Print Result : \t \nEnter To Continue ...\n')
    if barcode =='1':
        Display(records,today,no)
    if barcode == '2':
        Printer(records,today,no)
    
    if barcode !='1' and barcode !='2'and barcode !='':
        
        print("EXIT")
        break
    
    
    no= int(no) + int(1)
    print('recipe No ',no)
    grand=[]
    while True:
        
        rt =rt+1
        
        barcode = input('Enter QR Code here :\t')
        
        if barcode =='':
            break
        if barcode == '1122334455673':
            print("Dicount here ")
            dis_amount = input ("Enter discount amont : \t")
                
            records =records + ["Recipe No# "+str(no)+" No#  "+str(rt+1)+" "+str(today)+" "+"Discount"+" x "+"nil"+" "+str(dis_amount)+" "+barcode]
                
            # shelfFile = shelve.open('D:\\Records\Shop_Data') 
            shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Shop_Data')
            shelfFile['SHOP'] = records
            shelfFile.close()
            break
            
        if barcode not in barcodes:
            
            for i in range(len(Toyes_Records)):
                x = Toyes_Records[i].split()
                
                if x[5] == barcode:
                    if x[7] =='off':
                        print("Item already Sale ")
                        bbr = bbr +[x[5]]
                        break  
                                        
                    print("Status ==> ",x[7])
                    s = 'off'
                    x[7]=s
                    print(barcode," == ",x[5])
                    print("Price is ==> ",x[6])   
                    print("New Status ==> ",s)
                    
                    try:
                        Show_Image(no)
                    except:
                        print("Image missing ")
                     
                    Toyes_Records[i]="toye"+" "+str(x[1])+" "+"date"+" "+str(today)+" "+str(barcode)+" "+str(x[6])+" "+str(s)
                    
                    confirm = input("Please Confirm to Save File Y|N : \t ")
                    if confirm == 'y' or confirm =='Y':
                        shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
                        shelfFile['Toyes_Record']=Toyes_Records
                        shelfFile.close()
                        
                        no_pg=1
                        price = x[6]
                        print("PRICE ",price)
                        try:
                            P_price = int(price)*int(no_pg)
                        except:
                            print("Somthing missing Please wait and  try again ...\n")
                            time.sleep(3)
                        
                                    
                        records =records + ["Toye No# "+str(no)+" No#  "+str(rt+1)+" "+str(today)+" "+str(price)+" x "+str(no_pg)+" "+str(P_price)+" "+barcode]

                        shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Shop_Data')  
                        shelfFile['SHOP'] = records
                        shelfFile.close()
                        print("TOYES DONE")
                       
        for i in range(len(barcodes)):
           
            if barcode == barcodes[i]:
                
                price = input("Enter Price : ")
                if price =='':
                    break
                if price.isalpha() and price.isalnum():
                    print("Price must be Integer")
                    break
                no_pg =input('Enter qty : ')
                if no_pg=='':
                    break
                if no_pg.isalpha() and no_pg.isalnum():
                    print("Quantity must be Integer")
                    break
                    
                try:
                    P_price = int(price)*int(no_pg)
                except:
                    print("Somthing missing Please wait and  try again ...\n")
                    shelfFile.close()
                    time.sleep(3)
                    break
                    
                            
                print('\t \t \t \t \t \t Price is : ',price)
                print('\t \t \t \t \t \t amount : ',P_price)
                grand=grand+[P_price]
                print("\t \t \t \t \t \t*********************")
                print("\t \t \t \t \t \t GRAND TOTAL : ",str(sum(grand)))
                
                confirm = input("Please Confirm to Save File Y|N : \t ")
                if confirm == 'y' or confirm =='Y':
                        
                    records =records + ["Recipe No# "+str(no)+" No#  "+str(rt+1)+" "+str(today)+" "+str(price)+" x "+str(no_pg)+" "+str(P_price)+" "+barcode]
                                
                    shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Shop_Data')      
                    shelfFile['SHOP'] = records
                    shelfFile.close()
                    print("ALL DONE")
                    
              
    
shelfFile.close()
