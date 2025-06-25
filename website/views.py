from django.shortcuts import render
from customadmin.models import CarCompany, CarModel, Trim, ServiceCategory, ServiceItem, TrimServicePrice,Country

import json
# Create your views here.
def index(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    car_brands_grouped = chunked(car, 4)
    return render(request,'web/index.html',{'car_brands_grouped':car_brands_grouped})

def service(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    category=ServiceCategory.objects.all()

    car_brands_grouped = chunked(car, 4)
    country=Country.objects.all()
    return render(request,'web/service.html',{'car_brands_grouped':car_brands_grouped,'car':car,
                                            'category':category,'country':country})

def about(request):
    return render(request,'web/new.html')

def tire(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    car_brands_grouped = chunked(car, 4)
    return render(request,'web/tire.html',{'car_brands_grouped':car_brands_grouped})


# def load_exchange_rates(file_path='exchange_rates.json'):
#     with open(file_path, 'r') as f:
#         return json.load(f)

# def convert_currency(amount_in_inr, to_currency, rates):
#     rate = rates.get(to_currency.upper())
#     if rate:
#         return amount_in_inr * rate
#     else:
#         return "Currency not supported."

# # Load rates from JSON
# rates = load_exchange_rates()

# # Convert example
# amount = 1000
# currency = 'EUR'
# converted = convert_currency(amount, currency, rates)
# print(f"{amount} INR = {converted:.2f} {currency}")




