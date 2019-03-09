class Inventry:
   
    def AddItem():

        items = ['ABC','abc','XYZ','xyz','MMN','OOP']

        while True:
            ab = input('Enter Item Name ')
            if ab =='':
                break
        
          
            print(items,ab)
            Item_Check(items,ab)
            
            if ab not in items:
                items = items+[ab]
                print(items)
    

    def Item_Check(items,ab):
    
        if ab in items:
            print('exist')
            return
        

    AddItem()