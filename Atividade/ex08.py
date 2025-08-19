import requests

def buscar_dados_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()[0]

        nome = dados['name']['official']
        linguas = ", ".join(dados.get('languages', {}).values())
        regiao = dados.get('region', 'N/A')
        subregiao = dados.get('subregion', 'N/A')
        capital = ", ".join(dados.get('capital', ['N/A']))

        moedas = dados.get('currencies', {})
        if moedas:
            sigla_moeda = list(moedas.keys())[0]
            moeda_info = moedas[sigla_moeda]
            nome_moeda = moeda_info.get('name', 'N/A')
            simbolo_moeda = moeda_info.get('symbol', 'N/A')
        else:
            sigla_moeda = nome_moeda = simbolo_moeda = 'N/A'

        fronteiras = ", ".join(dados.get('borders', ['Nenhum']))

    
        print(f"Nome: {nome}")
        print(f"Línguas: {linguas}")
        print(f"Região: {regiao}")
        print(f"Sub-região: {subregiao}")
        print(f"Capital: {capital}")
        print(f"Moeda: {sigla_moeda} - {nome_moeda} ({simbolo_moeda})")
        print(f"Países que fazem fronteira: {fronteiras}")

    except:
        print("Erro ao buscar os dados do país.")

pais = input("Digite o nome do país: ").strip().lower()
buscar_dados_pais(pais)