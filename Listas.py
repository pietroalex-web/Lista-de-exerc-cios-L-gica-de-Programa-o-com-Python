lista_musicas = [] # lista de músicas
nova_musica = "" # Variavel par adicionar uma nova musica
opcao = 0 
while opcao != 5:
    print("O que voce deseja fazer?")
    print("[1] - Adicionar musica")
    print("[2] - Visualizar lista músicas")
    print("[3] - Apagar uma musica")
    print("[4] - atualizar musicas")
    print("[5] - sair")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        nova_musica = str(input("Nova música:"))
        lista_musicas.append(nova_musica)
        print("Musica ", nova_musica, "adicionada com sucesso🙃")
    elif opcao == 2:
        print("============")
        x = 1
        for musica in lista_musicas:
            print(x, " - ", musica)
            x += 1
    elif opcao == 3:
        print("============")
        x = 1
        for musica in lista_musicas:
            print(x, " - ", musica)
            x += 1
            deletar_musica = int(input("Digite o numero da musica para apagar: "))
            lista_musicas.pop(deletar_musica - 1)
    elif opcao == 4:
        print("============")
        x = 1
        for musica in lista_musicas:
            print(x, " - ", musica)
            x += 1
            atualizar_musica = int(input("Digite o numero da musica para atualizar: "))
            nova_musica = str(input("Digite a nova musica: "))
            lista_musicas[atualizar_musica - 1] = nova_musica
    elif opcao == 5:
        print("saindo...")
    else:
        print("Essa opçãoo é invalida tente novamente😫")