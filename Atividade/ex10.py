import requests

def identificar_zona(bairro):
    bairro = bairro.lower()
    
    zonas = {
        "Zona Norte": [
            "santana", "tucuruvi", "vila maria", "mandaqui", "jaçanã", "cachoeirinha",
            "lauzane paulista", "limão", "parada inglesa", "brasília", "vila medeiros",
            "jardim são paulo", "vila guilherme", "vila gustavo", "vila mazzei"
        ],
        "Zona Sul": [
            "santo amaro", "capão redondo", "campo limpo", "jabaquara", "grajaú",
            "interlagos", "vila mariana", "morumbi", "socorro", "ipanema", "pedreira",
            "vila das belezas", "pirituba", "vila andrade", "jardim são luis",
            "jardim angela", "cidade dutra", "americanópolis"
        ],
        "Zona Leste": [
            "itaquera", "penha", "são mateus", "vila prudente", "artur alvim",
            "mooca", "aricanduva", "sapopemba", "vila formosa", "vila carrão",
            "cidade tiradentes", "guaianases", "er melino matarazzo", "tatuapé",
            "cangaíba", "eng goulart", "patriarca", "anália franco", "vila domitila"
        ],
        "Zona Oeste": [
            "butantã", "pinheiros", "lapa", "perdizes", "rio pequeno", "jaguaré",
            "vila leopoldina", "vila sonia", "sumaré", "alto de pinheiros", "jardim paulista",
            "ceasa", "jaraguá", "pirituba", "cidade são domingos"
        ],
        "Zona Central": [
            "sé", "bela vista", "liberdade", "republica", "santa cecilia", "consolação",
            "higienópolis", "brás", "pari", "cambuci", "bom retiro", "avelino", "glicério"
        ]
    }

    for zona, bairros in zonas.items():
        for b in bairros:
            if b in bairro:
                return zona
    return "Zona não identificada"

cep = input("Digite o CEP do destino : ").replace("-", "").strip()

if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido.")
else:
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        elif dados.get("localidade", "").lower() != "são paulo":
            print(f"Destino: {dados.get('bairro', 'Bairro não informado')}, {dados.get('localidade')} - Fora da cidade de São Paulo.")
        else:
            bairro = dados.get("bairro", "Bairro não informado")
            zona = identificar_zona(bairro)
            print(f"Bairro: {bairro}, {zona} de São Paulo.")

    except:
        print("Erro ao consultar o CEP.")