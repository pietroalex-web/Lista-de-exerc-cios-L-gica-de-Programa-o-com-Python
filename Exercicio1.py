nome = str(input("Nome do cliente: "))
valorTotal = 0.0
opcao = 1

while opcao == 1:
    print("\nO que você deseja?\n1 - Adicionar produto\n0 - Finalizar compra")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        valorProduto = float(input("Valor do produto: R$ "))
        valorTotal = valorTotal + valorProduto

    elif opcao == 0:
        print(nome, "você deve pagar R$", valorTotal)