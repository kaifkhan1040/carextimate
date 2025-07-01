from django.shortcuts import render
from customadmin.models import CarCompany, CarModel, Trim, ServiceCategory, ServiceItem, TrimServicePrice,Country, Tyre

import json
# Create your views here.
def index(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    car_brands_grouped = chunked(car, 4)
    return render(request,'web/index.html',{'car_brands_grouped':car_brands_grouped})

def deepseek(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    car_brands_grouped = chunked(car, 4)
    return render(request,'web/deepseek.html',{'car_brands_grouped':car_brands_grouped})
def dropdown(request):
    car=CarCompany.objects.all()
    def chunked(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    car_brands_grouped = chunked(car, 4)
    if request.method=="POST":
        print("run pos")
        country=request.POST.get("country")
        print('country:',country)
        can=request.POST.get("can")
        print(' can:', can)
        model=request.POST.get("model")
        print('model:',model)
        trim=request.POST.get("trim")
        print('trim:',trim)
        tire= Tyre.objects.filter(trim=trim).first()
    return render(request,'web/tire-dropdown.html',{'car_brands_grouped':car_brands_grouped,"tire": tire})
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
    country=Country.objects.all()
    return render(request,'web/tire.html',{'car_brands_grouped':car_brands_grouped,'country':country})


def load_exchange_rates(file_path='exchange_rates.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def convert_currency(amount_in_inr, to_currency, rates):
    rate = rates.get(to_currency.upper())
    if rate:
        return amount_in_inr * rate
    else:
        return "Currency not supported."

# Load rates from JSON
rates = load_exchange_rates()

# Convert example
amount = 1000
currency = 'EUR'
converted = convert_currency(amount, currency, rates)
print(f"{amount} INR = {converted:.2f} {currency}")




