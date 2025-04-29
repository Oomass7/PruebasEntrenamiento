# # Solicitar entrada al usuario
# entrada = input("Ingrese números separados por comas: ")

# # Dividir la entrada en una lista
# valores = entrada.split(",")

# inNumbers = [int(valor) for valor in valores]

# for j in inNumbers:
#     print(type(j).__name__)

# print(inNumbers)


# # for i in valores:
# #     print(type(i).__name__)

# # Imprimir la lista (opcional)
# print(valores)

# list1 = list(range(0,10))
# list2 = range(50, 99)
# list3 = list(range(89, 101, 2))
# list4 = list(range(52,3, -7))

# print(list4)

# for i in list4:
#     print(i)
    
#Vamos a crear los primeros 10 resultados de la tabla de multiplicar

T = []
num = []




for i in range(11):
    for j in range(11):
        multi = i * j
        num.append(multi)
        if i > 10:
            num.clear
T.append(num)

print(T)
print(num)    

        
        
    
    
    
    
        
    










# print(type(list1).__name__)
# print(type(list2).__name__)
# print(type(list3).__name__)
# print(type(list4).__name__)

# for i in range(50, 98):
#     print(i)


















