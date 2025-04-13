import requests
query = input("What type of news are you interested in today?")
api = "e5a4cbfa17d2474dbe23f0eedd5bc87a"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-03-13&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1,article["title"], article["url"])
    print("\n**********************************\n")