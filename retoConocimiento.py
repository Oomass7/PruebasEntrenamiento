
luggageWe = float(input("Ingrese el peso del equipaje en kg: "))

luggageTy = input("Ingrese el tipo de equipaje (fragil, normal, pesado): ")

luggageDes = input("Ingrese el destino del equipaje (internacional/nacional): ")

if luggageWe > 32:
    print("Sobrepeso no permitido")
elif luggageTy.lower == "fragil" and luggageDes.lower == "internacional":
    print("Enviar a Area Especial Internacional")
elif luggageTy.lower == "fragil" and luggageDes.lower == "nacional":
    print("Enviar a Area Especia Nacional")
elif luggageTy.lower == "pesado" and luggageWe > 23 and luggageWe < 32:
    print("Enviar a Carga pesada")
elif luggageTy.lower == "normal" and luggageWe < 23 and luggageWe > 0:
    print("Equipaje normal")
else:
    print("Enviar a revision manual")