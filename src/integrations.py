import requests

def get_weather(city="Rio de Janeiro"):
    url = f"https://wttr.in/{city}?format=3"
    try:
        return requests.get(url).text
    except:
        return "Erro ao buscar clima."