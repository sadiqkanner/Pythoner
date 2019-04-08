recovery_records = []

with open('C:\\Users\sadiq\Desktop\Recovery.txt', 'r') as filehandle:  
    for line in filehandle:
        recovered = line[:-1]
        recovery_records.append(recovered)


import shelve
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\Print Records\Record_temp')

shelfFile['ABC']=[]

ree = input("Press 1 For Recovery all Data : \t")
if ree =='1':
    shelfFile['ABC']=recovery_records
    shelfFile.close()
    print("data has been recovered succesfully")
shelfFile.close()

