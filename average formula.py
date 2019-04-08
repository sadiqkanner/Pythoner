list = [21321,2321,11213,20213,36323,10023,55232,693323,862323]

total = float(sum(list))
avg=[]
for i in range(len(list)):
    
    avg = avg + [list[i] * 100 / total]
    

for i in range(len(avg)):
    print(avg[i])