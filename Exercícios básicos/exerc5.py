numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero_int = int(numero)
    dividendo = numero_int % 2
    if dividendo == 0:
        print("Seu número é par")
    else:
        print("Seu número é impar")
    
    
else:
    print("Você não digitou um número inteiro")