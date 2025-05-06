#MENU
#1. DEPOSITAR
#2. RETIRAR
#3. MOSTRAR SALDO
#4. SALIR






usersAcount = []

while True:
    print("-"*50)
    print("MENU \n1. Depositar \n2. Retirar \n3. Mostrar Saldo \n4. Salir")
    print("-"*50)
    try:
        option = input("Digite la opcion que desea: ")
    except:
        print("Por favor digite solo el numero de la opcion")
        
    while True:
        match option:
            case 1:
                print("-"*50)
                print("DEPOSITAR")
                print("-"*50)
                
                name = input("Ingresa tu nombre: ")
                if name not in usersAcount:
                    number = input("")
                
                
            case 2:
                print("-"*50)
                print("RETIRAR")
                print("-"*50)
                
            case 3:
                print("-"*50)
                print("MOSTRAR SALDO")
                print("-"*50)
                
            case 4:
                print("Gracias por utilizar el programa")
            
            case _:
                print("Digite una opcion que este en el menu")
                

    
    
    
    
    
    
    
    