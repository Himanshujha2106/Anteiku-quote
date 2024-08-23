from django.shortcuts import render
import requests

def quote(request):
   

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
        "x-rapidapi-key": "7e1989c9cdmsh9c231d90f070b13p1e6a8ajsn662883381a57",
        "x-rapidapi-host": "quotes15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    quote_data=response.json()

    name = quote_data['originator']['name']
    description = quote_data['originator']['description']
    content = quote_data['content']

    
    return render(request, 'index.html', {'name': name,'description':description,'content': content})
