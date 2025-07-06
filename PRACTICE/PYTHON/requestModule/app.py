import requests

def getNews():
    data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=f38c648292e342dbaaa44169f0f1486b')
    return data.json()


data = getNews()

for i in range(10):
    print(data["articles"][i])


