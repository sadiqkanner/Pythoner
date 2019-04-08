import cv2
from datetime import datetime, timedelta
import time
import shelve

def Capture_Image(no):

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow("Press Space To Capture", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "C:\\Users\sadiq\Desktop\Images\ img"+str(no)+".png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break    
    
    cam.release()
    cv2.destroyAllWindows()



shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')

Toyes_Records = shelfFile['Toyes_Record']
# Toyes_Records=[]
today = datetime.now()


while True:
    
    k = len(Toyes_Records)
    g = Toyes_Records[k-1]
    x = g.split()
    no = x[1]
  
    barcode = input('\nEnter To Continue ...\n')   
    if barcode !='':
        shelfFile.close()
        print("EXIT")        
        break
    
    while True:
        
        no= int(no) + int(1)
        shelfFile.close()
        
        Barcode = input('Enter QR Code here :\t')
        print(Toyes_Records)
        
        if Barcode =='':
            shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
            break
        bb=[]
        for i in range(len(Toyes_Records)):
            x = Toyes_Records[i].split()
            bb = bb +[x[5]]
        if Barcode in bb:
            print("Barcode Already Exist \n1:It's Enogh \n2:Do You Want to add More :")
            add = input()
            if add =='':
                break
            if add =='1':
                break
            if add =='2':
                qty =int(input("How many ITems Do you Want to add : "))
                if qty == '':
                    break
                price=input("Enter Price : ")
                Capture_Image(no)
                if price =='':
                    break
                j=1
                while j <= qty:
                    Toyes_Records=Toyes_Records+["toye"+" "+str(no)+" "+"date"+" "+str(today)+" "+str(Barcode)+" "+str(price)+" "+"on"]
                    print(Toyes_Records)
                    j=j+1
                    
                break
        if barcode not in bb:
            
            Capture_Image(no)
            price=input("Enter Price : ")
            if price =='':
                break
                
            Toyes_Records=Toyes_Records+["toye"+" "+str(no)+" "+"date"+" "+str(today)+" "+str(Barcode)+" "+str(price)+" "+"on"]
            print(Toyes_Records)
    
            shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
            shelfFile['Toyes_Record'] = Toyes_Records
            shelfFile.close()
         
         
         
         
         
         
         
         














"""
import cv2
from datetime import datetime, timedelta
import time
import shelve

def Capture_Image(no):

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow("Press Space To Capture", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "C:\\Users\sadiq\Desktop\Images\ img"+str(no)+".png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break    
    
    cam.release()
    cv2.destroyAllWindows()



shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')

Toyes_Records = shelfFile['Toyes_Record']

today = datetime.now()


while True:
    
    k = len(Toyes_Records)
    g = Toyes_Records[k-1]
    x = g.split()
    no = x[1]
  
    barcode = input('\nEnter To Continue ...\n')   
    if barcode !='':
        shelfFile.close()
        print("EXIT")        
        break
    
    while True:
        
        no= int(no) + int(1)
        shelfFile.close()
        
        Barcode = input('Enter QR Code here :\t')
        print(Toyes_Records)
        
        if Barcode =='':
            shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
            break
        bb=[]
        for i in range(len(Toyes_Records)):
            x = Toyes_Records[i].split()
            bb = bb +[x[5]]
        if Barcode in bb:
            print("Barcode Already Exist ")
            # break

        Capture_Image(no)
        
        price=input("Enter Price : ")
        if price =='':
            break
            
        Toyes_Records=Toyes_Records+["toye"+" "+str(no)+" "+"date"+" "+str(today)+" "+str(Barcode)+" "+str(price)+" "+"on"]
        print(Toyes_Records)

        shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Toyes')
        shelfFile['Toyes_Record'] = Toyes_Records
        shelfFile.close()
"""
