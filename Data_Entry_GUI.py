

import shelve
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\MyFile')


def InsertData(Items_Name , Rate , Quantity , Vender):
    
   
    M_item = shelfFile['items']
    M_Rate = shelfFile['prices']
    M_QTY = shelfFile['quantities']
    M_Vender = shelfFile['venders']
    
    M_Rate = M_Rate + [Rate]
    shelfFile['prices'] = M_Rate
    
    M_item = M_item + [Items_Name]
    shelfFile['items'] = M_item
    
    M_QTY = M_QTY + [Quantity]
    shelfFile['quantities'] = M_QTY

    
    M_Vender = M_Vender + [Vender]
    shelfFile['venders'] = M_Vender
    
    print(M_QTY)
    print(M_Rate)

    
    
    
    


i =0


from tkinter import *
import tkinter as tk

#from tkinter import Tk , Label , Button , Entry , Text

window = tk.Tk()
window.title('MyAPP2')
window.geometry('400x400')

#Label(text =' ' font=(font,size)
title = tk.Label(text="PEN AND PAPER \n ***********************", font=('Arial Time New Roman',15 , ))
title.grid(column =1 , row=0)



label_Item = tk.Label(text="Item_Name :" ,font=('Arial',10))
label_Item.grid(column=0 , row=1)
Item_field = tk.Entry()
Item_field.grid(column =1 , row = 1)



i =0
def checkme():
    
    
    M_item = shelfFile['items']
    M_Rate = shelfFile['prices']
    M_QTY = shelfFile['quantities']
    M_Vender = shelfFile['venders']

    
    if i in range(len(M_item)):
        if Item_field.get() in M_item:
            Quantity_field.insert(10,M_QTY[i])
            Price_field.insert(10,M_Rate[i])
            Vender_field.insert(10,M_Vender[i])
    
            
j=0            
def clickme():
    
    Items_Name = Item_field.get()
    Rate = Price_field.get()
    Quantity = Quantity_field.get()
    Vender = Vender_field.get()
    
    InsertData(Items_Name , Rate , Quantity , Vender)
    Item_field.delete(0,END)
    Price_field.delete(0,END)
    Quantity_field.delete(0,END)
    Vender_field.delete(0,END)
    Item_field.focus()
    
    

BtnCheck = tk.Button(text="check", bg='red', fg='white', font=('Arial',9), command=checkme)
BtnCheck.grid(column =2 , row =1)




label_Quantity = tk.Label(text="Item_Quantity:" ,font=('Arial',10))
label_Quantity.grid(column=0 , row=2)
Quantity_field = tk.Entry()
Quantity_field.grid(column =1 , row = 2)

label_Price = tk.Label(text="Item_Price :" ,font=('Arial',10))
label_Price.grid(column=0 , row=3)
Price_field = tk.Entry()
Price_field.grid(column =1 , row = 3)


label_Vender = tk.Label(text="Vender :" ,font=('Arial',10))
label_Vender.grid(column=0 , row=4)
Vender_field = tk.Entry()
Vender_field.grid(column =1 , row = 4)

'''text_field = tk.Text(master = window,height=10,width=30)
text_field.grid(column=0 , row=3)'''


    
button1 = tk.Button(text="Add Item", bg='green', fg='white', font=('Arial',10), command=clickme)
button1.grid(column =0 , row =5)





window.mainloop()


