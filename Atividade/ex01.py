# -- x1
# A = Alcool
# G = Gasolina
G = 2.50 
A = 1.90
comprador = input('A-álcool ou G-gasolina?')
litro = float(input('Quantos litros?'))

if comprador == "A-álcool":
    if litro <= 20:
        ValorDesconto = litro*A-(litro*A)/100*3
        print(f"O Valor total foi de: ${ValorDesconto}")
    else:
        ValorDesconto = litro*A-(litro*A*0.05)
        print(f"O Valor total foi de: ${ValorDesconto}")
elif comprador == "G-gasolina":
    if litro <= 20:
        ValorDesconto = litro*G-(litro*G*0.04)
        print(f"O Valor total foi de: ${ValorDesconto}")
    else:
        ValorDesconto = litro*G-(litro*G*0.06)
        print(f"O Valor total foi de: ${ValorDesconto}")