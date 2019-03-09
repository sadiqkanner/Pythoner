import barcode
import random

def barcode_generators():
    j=0
    while j < 1:
        
        num = 100000001122
        for i in range(1,12):
            num = num+1
            image = barcode.get_barcode_class("ean13")
            image_bar = image(u'{}'.format(num))
            file = open('C:\\Users\sadiq\Desktop\cd'+str(i)+'.svg',"wb")
            image_bar.write(file)
            print(image_bar)
            
            
        j=j+1
             
             
print("Success")  
    
for i in range(1,5):
    barcode_generators()
    