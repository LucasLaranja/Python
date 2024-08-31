import random

nove_digitos = ""
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro__digito = (resultado_digito_1 * 10) % 11
primeiro__digito if primeiro__digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro__digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo__digito = (resultado_digito_2 * 10) % 11
segundo__digito if segundo__digito <= 9 else 0

validacao = f"{nove_digitos}{primeiro__digito}{segundo__digito}"

print(validacao)