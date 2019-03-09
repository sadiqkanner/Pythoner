import shelve
from datetime import datetime, timedelta


shelfFile = shelve.open('C:\\Users\sadiq\Desktop\PROJECT Python\Printing Inventory\Mydata001')
x=shelfFile['records']
Items = shelfFile['items'] 
Barcodes =shelfFile['barcodes'] 
Prices = shelfFile['prices']
our_barcode = shelfFile['our_barcode']


while True:
    
    search = input("Enter Barcode : ")
    if search == '':
        break
        
    for i in range(len(Barcodes)):
        if search == Barcodes[i]:
            print("Barcode is => ",Barcodes[i])
            print("Item is => ",Items[i])
            print("Price is => ",Prices[i])
            print("Our_Barcode is => ",our_barcode[i])
                    
            no_pg =input('Enter the Number of Copied Pages : \t')
            total = int(Prices[i]) * int(no_pg)
            x=x + [str(datetime.now())+" "+Barcodes[i]+" "+str(our_barcode[i])+" "+Items[i]+" "+Prices[i]]
            print(x)
            shelfFile['records'] = x