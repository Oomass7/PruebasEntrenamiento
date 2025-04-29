tables = []

for i in range(10):
    tableToClearing = []
    for j in range(1,11):    
        multi = j * i
        tableToClearing.append(multi)
    tables.append(tableToClearing)

print(tables)