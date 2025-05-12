estudentsList = []

def addEstudent():
    print("AGREGAR ESTUDIANTE")
    identi = input("Ingrese el ID del estudainte que desea registrar: ")
    existe = False
    for estudent in estudentsList:
        if estudent.get("id") == identi:
            existe = True
            break
        elif estudent.get("id") == identi:
            print("El usuario ya esta registrado.") 
            
    if not existe:
        print("Ingrese los datos del estudiante")
        name = input("Nombre: ")
        age = input("Edad: ")
        note = input("Nota: ")
        estudent = {
            "name" : name,
            "id" : identi,
            "age" : age,
            "note" : note
        }
        estudentsList.append(estudent)
    else:
        print("El estudainte ya se encuentra registrado")
    print(estudentsList)
    
    
        
def menu():
    print("-"*60)
    print("MENU")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Actualizar informacion del estudiante")
    print("4. Eliminar estuiante")
    print("5. Calcular promedio del estudiante")
    print("6. Listar estudiantes por debajo de una nota")
    print("7. Salir")
    option = input("Seleccione una opción del menu: ")
    print("-"*60)
    return option


def main():
    while True:
        option = menu()
        match option:
            case "1":
                addEstudent()    
            
main()