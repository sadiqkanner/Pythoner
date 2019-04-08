 
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
    
    Date : """+str(today.date())+"""       """'No:'+no+"""
           
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
            body =x[7].ljust(2)+" "+x[9].center(18)+" "+str(x[10]+" ")
            
            b=b+[body]

            
            
    gt="""---------------------------------
    """+'TOTAL'.ljust(20)+""" """+str(sum(grand))+"""
    
"""'CELL: 021-8838388 '"""
    """'ITTEHAD COMMERICAL AREA DHA'"""
    """
    x='\n    '.join(b)

    yy=(header+x+gt)
    baconFile = open('C:\\Users\sadiq\Desktop\Print Records\temp.txt', 'w')
    
    baconFile.write(yy)
    
    import os
    fd = os.startfile('C:\\Users\sadiq\Desktop\Print Records\temp.txt', 'print')
    




import shelve
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Record_temp')  
from datetime import datetime, timedelta


barcodes=['1000000011241','1000000011296','1000000011289','1000000011265','1000000011234','1000000011319','1000000011258','1000000011302','1000000011272','1000000011364','1000000011371','1000000011388']

today = datetime.today()

while True:
    
    records = shelfFile['ABC']
    k = len(records)
    g = records[k-1]
    x = g.split()
    no = x[2]
    rt=-1
    barcode = input('1: Display Result : \t \n2: Print Result : \t \n3: All records \nEnter To Continue ...\n')
    if barcode =='1':
        Display(records,today,no)
    if barcode == '2':
        Printer(records,today,no)
    if barcode == '3':
        Days(records,today)
    if barcode =='n':
        shelfFile.close()
        print("EXIT")
        break
    
    no= int(no) + int(1)
    print('recipe No ',no)
    
    grand =[]
    while True:
        rt =rt+1
        barcode = input('Enter QR Code here :\t')
        
        if barcode =='':
             
            break
        
        for i in range(len(barcodes)):

            if barcode == barcodes[i]:

                price = input("Enter Price : ")
                if price =='':
                    break

                no_pg =input('Enter qty : ')
                if no_pg=='':
                    break
                
                P_price = int(price)*int(no_pg)
                print('\t \t \t \t \t \t Price is : ',price)
                print('\t \t \t \t \t \t amount : ',P_price)
                records =records + ["Recipe No# "+str(no)+" No#  "+str(rt+1)+" "+str(today)+" "+str(price)+" x "+str(no_pg)+" "+str(P_price)+" "+barcode]
                
                grand = grand + [P_price]
                
                print("\t \t \t \t \t \t Grand Total is : ",str(sum(grand)))
                shelfFile['ABC'] = records
                
                
              
            
    
    print('Exit')
    
