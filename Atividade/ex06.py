Porcentagem = 0.015

Salario_inicial = int(input("Informe salario: "))

Salario_atual = (Salario_inicial * Porcentagem) + Salario_inicial

Ano = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014
]

for i in range(len(Ano)):
    if Ano[i] == 1996:
        print(f"{Salario_atual:.2f} - {Ano[i]}")
    else:
        Porcentagem *= 2 
        Salario_atual += (Salario_atual*Porcentagem)+Salario_atual
        print(f"{Salario_atual:.2f} - {Ano[i]}")