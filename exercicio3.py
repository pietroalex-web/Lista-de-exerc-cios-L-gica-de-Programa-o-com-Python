produto = {
    "nome": "Banana",
    "descricao": "É uma Banana",
    "quantidade": 15,
    "valor_unitario": 1.00
}

def calcular_total():
    return produto["quantidade"] * produto["valor_unitario"]

def mostrar_status():
    print("\n--- STATUS DO ESTOQUE ---")
    print("Produto: {produto['nome']}")
    print("Desc: {produto['descricao']}")
    print("Qtd: {produto['quantidade']}")
    print("Preço Unitário: R$ {produto['valor_unitario']: }")
    print("VALOR TOTAL EM CAIXA: R$ {calcular_total(): }")
    print("------------------------")

while True:
    mostrar_status()
    print("\nO que vamos atualizar hoje?")
    print("1 - Nome | 2 - Descrição | 3 - Quantidade | 4 - Preço | 0 - Sair")
    
    escolha = input("Número: ")

    if escolha == "1":
        produto["nome"] = input("Novo nome do item: ")
    elif escolha == "2":
        produto["descricao"] = input("Nova descrição: ")
    elif escolha == "3":
        produto["quantidade"] = int(input("Nova quantidade no estoque: "))
    elif escolha == "4":
        produto["valor_unitario"] = float(input("Novo valor de venda: "))
    elif escolha == "0":
        print("Fechando o sistema.")
        break
    else:
        print("Opção inválida.")