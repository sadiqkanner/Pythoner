import barcode
import shelve
from datetime import datetime, timedelta
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Toyes\Toyes_data')
          
num = 1234567890123
record = []
status = 'Active'
today = datetime.today()
for i in range(0,10):
    
    ok = input("Please Confirm with Press 1 : ")
    if ok =='':
        break
    if ok =='1':
        
        import barcode
        import random
        nn = input("Enter BarCode Name : ")
        num = num +1 
        image = barcode.get_barcode_class("code128")
        image_bar = image(u'{}'.format(num))
        file = open('C:\\Users\sadiq\Desktop\ '+str(nn)+'.svg',"wb")
        image_bar.write(file)
        print(image_bar)
        
     
        print("Success")  
        
        




'''

search = input("Enter Barcode : ")
for i in range(len(Barcodes)):
    if search == Barcodes[i]:
        print("Hello ",Barcodes[i])
        print("Hello ",Items[i])
        print("Hello ",Prices[i])
        print("HEllo ",our_barcode[i])
        
'''
