from Funções import *

print("############################\n")
print("Qual a data de vencimento?")
print("Formato:Dia-Mês-Ano. Exemplo: 19-12-2012\n")
print("############################\n")

due_date = input("")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Entrada inválida!")
