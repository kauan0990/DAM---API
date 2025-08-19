import requests

moeda = input("Digite a sigla da moedaEURer: ").strip().upper()
url = "https://api.exchangerate-api.com/v4/latest/BRL"

nomes_moedas = {
    "USD": "dólares americanos",
    "EUR": "euros",
    "GBP": "libras esterlinas",
    "ARS": "pesos argentinos",
    "JPY": "ienes japoneses",
    "CHF": "francos suíços",
    "CAD": "dólares canadenses",
    "AUD": "dólares australianos",
    "CNY": "yuans chineses"
}

try:
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()

    if moeda in dados["rates"]:
        taxa = dados["rates"][moeda]
        nome_moeda = nomes_moedas.get(moeda, moeda)
        print(f"O Real vale {taxa:.2f} {nome_moeda}.")
    else:
        print("Moeda não encontrada na base de dados.")
except:
    print("Erro ao acessar a API ou processar os dados.")