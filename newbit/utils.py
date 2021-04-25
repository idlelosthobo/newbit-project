import requests


nyt_api_key = 'fVcqRCgZMed4C2m8GaQeNKH79PlAQSER'
nyt_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


def get_news(topic: str):

    querystring = {
        "begin_date": "20200101",
        "end_date": "20200131",
        "q": topic,
        'page': 0,
        "api-key": nyt_api_key,
    }

    json = requests.request("GET", nyt_url, params=querystring).json()

    headlines = ''

    for article in json['response']['docs']:
        headlines += article['headline']['main']

    print(headlines)

    return headlines