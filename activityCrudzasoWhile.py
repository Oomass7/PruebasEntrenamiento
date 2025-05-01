reparationList = []

while True:
    try:
        print("-" * 40)
        print("MENU \n1. Registra nueva reparación \n2. Ver reparaciones pendiente: \n3. Marcar una reparacion como lista \n4. Salir del sistema")
        print("-" * 40)
        option = int(input("Ingrese el numero de la opcion que aparece en el menu: "))
        match option:
            case 1:
                print("-" * 40)
                print("REGISTRAR UNA NUEVA REPARACION")
                print("-" * 40)
                detailReparation = input("Escriba la reparacion pendiente: ")
                reparationList.append(detailReparation)
                continue
            case 2:
                x = 1
                print("-" * 40)
                print("VER REPARACIONES PENDEINTES")
                print("-" * 40)
                if len(reparationList) == 0:
                    print("No hay reparaciones pendientes\n")
                for i in reparationList:
                    print(f"{x}. {i}")
                    x += 1
                continue
            case 3:
                while True:
                    print("-" * 40)
                    print("MARCAR UNA REPARACION COMO COMPLETADA")
                    print("-" * 40)
                    x = 1
                    if len(reparationList) == 0:
                        print("No hay reparaciones pendientes\n")
                        break
                    else:
                        for i in reparationList:
                            print(f"{x}. {i}")
                            x += 1
                        deleteReparation = (input("Escribe la reparacion que completaste: "))
                        if deleteReparation not in reparationList:
                            print("Escribiste mal la reparacion o no esta en la lista")
                        else:
                            reparationList.pop(deleteReparation)
                        
                        continue
            case 4:
                print("-" * 40)
                print("Muchas gracias por utilizar el programa")
                print("-" * 40)
                break
            
            case _:
                print("El numero que ingresaste no esta en el menu")
        exit
    except:
        print("Por favor ingrese solo el numero que aparece en el menu: ")










