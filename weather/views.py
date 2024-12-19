from django.shortcuts import render
import requests



# API key
# api = "3323adf9d1f1d730cbb272ce4bfa9e32"
# base_url = "https://api.openweathermap.org/data/2.5/weather"


# Create your views here.
def report(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET.get('city')
        api = "3323adf9d1f1d730cbb272ce4bfa9e32"
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            'q' : city,
            'appid' : api,
            'units' : 'metric'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:  
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon'],  
            }
        else:
            weather_data = {'error': f"City '{city}' not found or invalid API key."}
    
    return render(request, 'weather/index.html', {'weather_data': weather_data})
