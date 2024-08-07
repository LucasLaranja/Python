import random

print("Bem vindo ao Guess Number!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: Valor informado não é númerico. Favor informe um número!")
    quit()
    
random_number = random.randint(0, choice_number)
    
n_choices = 0
    
while True:
    answer_user = input("adivinhe o número: ")
    
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: Valor informado não é númerico. Favor informe um número!")
        continue
    
    n_choices = n_choices + 1
    
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, tente um número menor...")
    else:
        print("Chutou baixo, tente um número maior...")
        
print("N° de tentativas: " + str(n_choices))
        
