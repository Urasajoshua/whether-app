from django.shortcuts import render
import urllib
import json

def index(request):
    if request.method == "POST":
        city=request.POST.get('city')
        api_url=urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=63c41ac247956b75d1b2b08196a5d2c5').read()
        api_2=json.loads(api_url)
        print(api_2)

        data = {
            'city':city,
            'whether_description':api_2['weather'][0]['description'],
            'whether_temperature':api_2['main']['temp'],
            'whether_humidity':api_2['main']['humidity'],
            'whether_pressure':api_2['main']['pressure'],
        }
    else:
        data = {
            'city':None,
            'whether_description':None,
            'whether_temperature':None,
            'whether_humidity':None,
            'whether_pressure':None,
        }

    return render(request,'index.html',{'data':data})
