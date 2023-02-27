from django.shortcuts import render
import requests
import json

# Create your views here.
CRPTO_NEWS_API = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
CRPTO_PRICE_API = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS," \
                  "LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD"


def home(request):

    price_response = requests.get(CRPTO_PRICE_API)
    price_data = json.loads(price_response.content)

    newa_response = requests.get(CRPTO_NEWS_API)
    news_data = json.loads(newa_response.content)
    context = {
        'price_data': price_data,
        'news_data': news_data
    }
    return render(request, 'crypto/home.html', context)


def prices(request):
    context = {'notfound': 'Enter a crypto currency symbol into the form above...'}

    if request.method == "POST":
        quote = request.POST['quote'].upper()
        crypto_response = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD")
        cypto_data = json.loads(crypto_response.content)
        context = {
            'quote': quote,
            'cypto_data': cypto_data,
        }
    return render(request, 'crypto/prices.html', context)
