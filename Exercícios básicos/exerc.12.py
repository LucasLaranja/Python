lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao == "i":
        valor = input("valor: ")
        lista.append(valor)
    elif opcao == "a":
        indice_str = input(
            "Escolha o índice para apagar: "
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print("Não foi possível apagar esse índice.")
        
    elif opcao == "l":
        
        if len(lista) == 0:
            print("Não existe nada para listar")
        
        for i, valor in enumerate(lista):
            print(i, valor)
            
    else:
        print("Escolha entre i, a ou l.")