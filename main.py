import requests

api_key = "9f22eeb787744f579c6d55b43ef95b99"

url =("https://newsapi.org/v2/everything?q=tesla"\
      "&from=2024-11-15&sortBy=publishedAt&"\
      "apiKey=9f22eeb787744f579c6d55b43ef95b99")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])