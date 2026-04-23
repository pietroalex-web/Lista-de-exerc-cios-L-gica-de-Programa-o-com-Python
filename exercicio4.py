nome = input("Nome completo: ")
cpf = input("CPF: ")
cargo = input("Cargo: ")
loja = input("Loja/Filial: ")

salario_base = float(input("Salário base (R$): "))
vendas = int(input("Quantidade de carros vendidos: "))
porcentagem = float(input("Percentual de comissão (ex: 7): "))
vale_transporte = float(input("Valor Vale-Transporte: "))
vale_alimentacao = float(input("Valor Vale-Alimentação: "))

comissao_por_carro = salario_base * (porcentagem / 100)
total_comissao = comissao_por_carro * vendas
total_receber = salario_base + total_comissao + vale_transporte + vale_alimentacao


print("==========================")
print(nome, "|", cpf)
print(cargo, "|", loja)
print("==========================")
print("SALÁRIO BASE DO FUNCIONÁRIO: R$", salario_base)
print("QUANTIDADE DE carros VENDIDOS NO MÊS:", vendas)
print("PERCENTUAL DE COMISSÃO POR VEÍCULO VENDIDO:", porcentagem, "%")
print("VALOR EM REAIS (R$) GANHO DE COMISSÃO: R$", total_comissao)
print("VALOR EM REAIS (R$) GANHO DE VALE TRANSPORTE: R$", vale_transporte)
print("VALOR EM REAIS (R$) GANHO DE VALE ALIMENTAÇÃO: R$", vale_alimentacao)
print("VALOR EM REAIS (R$) TOTAL À RECEBER: R$", total_receber)