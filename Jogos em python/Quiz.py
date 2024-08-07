print("Bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N) ")
print(answer_user)

if answer_user != "S":
    quit()
    
score = 0
    
print("Começando...")
print("Qual é a selação com mais copas do mundo? \n (A) França \n (B) Itália \n (C) Brasil \n (D) Argentina \n")
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
    
print("Qual o(a) maior atleta olímpico brasileiro em medalhas? \n (A) Neymar \n (B) Rebecca Andrade \n (C) César Cielo \n (D) Lucão \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
    
print(f"Quiz acabou... Pontuação: {score}/2")