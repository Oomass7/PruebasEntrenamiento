tables = []
tableToClearing = []  
x = 1
j = 0

for i in range(0,89):
    multi = x * j
    x += 1
    if x == 10:
        x = 1
        j += 1
        
    if len(tableToClearing) == 9:
        tables.append(tableToClearing)
        
    tableToClearing.append(multi)   
    

print(tables)
        