from django.shortcuts import render

import requests
import json

# Create your views here.

def search(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = requests.get('https://api.openweathermap.org/data/2.5/weather?q='
                                         + city + '&units=metric&appid=55ab7837a8551d94192075e250396d68')
        list_of_data = source.json()


        print('List of data: ',list_of_data)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ',' +
                          str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']) + 'ºC',
            'min_temp': str(list_of_data['main']['temp_min']),
            'max_temp': str(list_of_data['main']['temp_max']),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon']
        }
        context={
            "weather":data
        }
        print('city: ',city)
        print('data: ',data)

    else:
        context={
        }

    return render(request, 'search.html',context)
    
# urls=f''https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=55ab7837a8551d94192075e250396d68'