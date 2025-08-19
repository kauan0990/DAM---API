Cardapio = {
    100: {"Nome": "Cachorro Quente", "Preco": 1.20},
    101: {"Nome": "Bauru Simples", "Preco": 1.30},
    102: {"Nome": "Bauru com ovo", "Preco": 1.50},
    103: {"Nome": "Hambúrguer", "Preco": 1.20},
    104: {"Nome": "Cheeseburguer", "Preco": 1.30},
    105:  {"Nome": "Refrigerante", "Preco": 1.00}

}


Cachorro_Quente = 0
Bauru_Simples = 0
Bauru_com_ovo = 0
Hambúrguer = 0
Cheeseburguer = 0
Refrigerante = 0

Total = 0
Comprar = input("Deseja comprar? ")

while Comprar == "Sim":
    Codigo = int(input("Informe o codigo do produto: "))
    Quantidade = int(input("Informe a quantidade: "))

    if Codigo == 100: 
        Cachorro_Quente += Cardapio[100]["Preco"]*Quantidade
    elif  Codigo == 101: 
        Bauru_Simples += Cardapio[101]["Preco"]*Quantidade
    elif  Codigo == 102: 
        Bauru_com_ovo += Cardapio[102]["Preco"]*Quantidade
    elif  Codigo == 103: 
        Hambúrguer += Cardapio[103]["Preco"]*Quantidade
    elif  Codigo == 104: 
        Cheeseburguer += Cardapio[104]["Preco"]*Quantidade
    elif  Codigo == 105: 
        Refrigerante += Cardapio[105]["Preco"]*Quantidade

    Comprar = input("Deseja continuar comprando? ")


Valor_Produto = print(f"Cachorro Quente: {Cachorro_Quente}, Bauru Simples: {Bauru_Simples}, Bauru com ovo: {Bauru_com_ovo} Hambúrguer: {Hambúrguer}, Cheeseburguer: {Cheeseburguer}, Refrigerante: {Refrigerante}")
Total = print(f"Valor Total: {Cachorro_Quente+Bauru_Simples+Bauru_com_ovo+Hambúrguer+Cheeseburguer+Refrigerante}")