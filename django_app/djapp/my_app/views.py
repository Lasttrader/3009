from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def get_predict(request):
    message = requests.post('http://127.0.0.1:5000/flskapi/v1/add_message/', 
                        json = {'X_get_age' : [10, 1, 0, 0, 1, 1, 0, 8, 3, 0, 0.12107185807539463, 0.3740520633526504, -0.1691938897666138, -0.5768294699140059, 2.9890440835684733, -0.3204128219555523]})
    print(message)
    if message.ok:
        print(message.json()) #возвращение прогноза
    return HttpResponse(f"Ваш прогшноз {message.json()}")