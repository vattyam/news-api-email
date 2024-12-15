import requests
import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "vattyam.sandeep@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "vattyam.sandeep@gmail.com"
    context = ssl.create_default_context()

#    message = """\
#    Subject : Hi!
#    Hi!
#    How are you?
 #   Bye!
 #   """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)


api_key = "9f22eeb787744f579c6d55b43ef95b99"

topic = "tesla"

url ="https://newsapi.org/v2/everything?"\
      f"q={topic}"\
      "&from=2024-11-15&sortBy=publishedAt&"\
      "apiKey=9f22eeb787744f579c6d55b43ef95b99&"\
      "language=en"

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)

# Access the article titles and descriptions
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)