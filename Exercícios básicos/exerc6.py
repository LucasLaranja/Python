hora = input("Que horas são no momento ? ")

hora = int(hora)

try:

    if hora >= 1 and hora <= 5:
        print("Boa madrugada")

    elif hora >=6 and hora <= 11:
        print("Bom dia")

    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    
    else:
        print("Boa noite")

except:
    print("Por favor digite apenas números inteiros")