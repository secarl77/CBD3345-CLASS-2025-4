import os
import requests

API_KEY = os.getenv("NEWS_API_KEY")  # El secreto vendrá del entorno

url = f"https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Top headlines:")
    for article in data["articles"][:5]:
        print("-", article["title"])
else:
    print("Error:", response.status_code, response.text)


# import requests
#
# API_KEY = "2d9974010ac74ae8b63951b588ac82a6"  # 👈 Coloca tu clave aquí como string
#
# url = "https://newsapi.org/v2/top-headlines"
# params = {
#     "country": "us",
#     "apiKey": API_KEY
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     data = response.json()
#     print("Top headlines:")
#     for article in data["articles"][:5]:
#         print("-", article["title"])
# else:
#     print("Error:", response.status_code, response.text)
