#MENU
#1. DEPOSITAR
#2. RETIRAR
#3. MOSTRAR SALDO
#4. SALIR





usersAcount = [{"nombre": "Tomas",
                "Account": "123456789",
                "saldo": 200000},
                
               {"nombre": "Andres",
                "Account": "987654321", 
                "saldo": 3000000},

               {"nombre": "David",
                "Account": "456789123",
                "saldo": 500000}]

while True:
    print("-"*50)
    print("MENU \n1. Depositar \n2. Retirar \n3. Mostrar Saldo \n4. Salir")
    print("-"*50)
    option = int(input("Digite la opcion que desea: "))
        

    match option:
        case 1:
            print("-"*50)
            print("DEPOSITAR")
            print("-"*50)
            number = (input("Ingrese su numero de cuenta: "))
            for i in usersAcount:
                if i["Account"] == number:
                    print("Bienvenido", i["nombre"])
                    try:
                        deposit = int(input("Cuanto desea depositar: "))
                        if deposit <= 0:
                            print("El monto a depositar no puede ser menor o igual a 0")
                            break
                        else:
                            i["saldo"] += deposit
                            print("Deposito exitoso")
                            break
                    except:
                        print("Por favor digite solo numeros")
                        break
                else:
                    print("No existe una cuenta con ese numero o ingresaste mal el numero")
                    break
                
        
        case 2:
            print("-"*50)
            print("RETIRAR")
            print("-"*50)
            number = (input("Ingrese su numero de cuenta: "))
            for i in usersAcount:
                if i["Account"] == number:
                    if  i["saldo"] <= 0:
                        print("No tiene saldo en la cuenta")
                        break
                    else:
                        print("Bienvenido", i["nombre"])
                        try:
                            withdraw = int(input("Cuanto deseas retirar: "))
                            if withdraw > i["saldo"]:
                                print("No tiene suficiente saldo")
                                break
                            else:
                                i["saldo"] -= withdraw
                                print("Retiro exitoso")
                                break
                        except:
                            print("Por favor digite solo numeros")
                            break
                else:
                    print("No existe una cuenta con ese numero o ingresaste mal el numero")
                    break
            
        case 3:
            print("-"*50)
            print("MOSTRAR SALDO")
            print("-"*50)
            number = (input("Ingrese su numero de cuenta: "))
            for i in usersAcount:
                if i["Account"] == number:
                    print("Bienvenido", i["nombre"])
                    print("Su saldo es de: ", i["saldo"])
                    break
                else:
                    print("No existe una cuenta con ese numero o ingresaste mal el numero")
                    break
            
        case 4:
            print("Gracias por utilizar el programa")
            break
        
        case _:
            print("Digite una opcion que este en el menu")
    exit           
                  
    
    
    
    
    
    
