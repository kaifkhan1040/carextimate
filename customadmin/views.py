from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .models import CarCompany,CarModel,Trim,ServiceItem,ServiceCategory,TrimServicePrice,Country,Tyre
from .forms import CarCompanyForm,CarModelForm,TrimForm,ServiceCategoryForm,ServiceItemForm,CountryForm,TyreForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'customadmin/index.html')

def car_list(request):
    car = CarCompany.objects.all()
    return render(request,'customadmin/carlist.html',{'car':car})

def add_carlist(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(CarCompany, id=id)
            form = CarCompanyForm(request.POST,instance=obj)
        else:
            form = CarCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Car Company has been Added successfully!')
            return redirect('customadmin:car_list')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(CarCompany, id=id)
            form = CarCompanyForm(instance=obj)
        else:
            form = CarCompanyForm()
    
    return render(request, 'customadmin/car_add.html', {'form': form,'obj':obj})

def delete_carlist(request,id=None):
    if id:
        obj = get_object_or_404(CarCompany, id=id)
        obj.delete()
        
        messages.success(request, f'Car Company has been removed successfully!')
        return redirect('customadmin:car_list')
  
def car_model_list(request):
    car=CarCompany.objects.all()
    obj=request.GET.get('search')
    if obj:
        if obj == 'all':
            carmodel = CarModel.objects.all()
        else:
            carmodel = CarModel.objects.filter(company=obj)
    else:
        carmodel = CarModel.objects.all()
    return render(request,'customadmin/carmodel.html',{'carmodel':carmodel,'car':car})

def add_carmodel(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(CarModel, id=id)
            form = CarModelForm(request.POST,instance=obj)
        else:
            form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Car Model has been Added successfully!')
            return redirect('customadmin:car_model_list')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(CarModel, id=id)
            form = CarModelForm(instance=obj)
        else:
            form = CarModelForm()
    
    return render(request, 'customadmin/car_model_add.html', {'form': form,'obj':obj})

def delete_carmodel(request,id=None):
    if id:
        obj = get_object_or_404(CarModel, id=id)
        obj.delete()
        
        messages.success(request, f'Car Model has been removed successfully!')
        return redirect('customadmin:car_model_list')
    
    
def trim(request):
    car = Trim.objects.all()
    print(car)
    return render(request,'customadmin/trim.html',{'car':car})

def add_trim(request,id=None):
    servicedata=None
    saved_model_id=None
    cat = ServiceCategory.objects.all()
    service_item = []

    # Prepare price lookup
    servicedata_dict = {}
    if id:
        obj = get_object_or_404(Trim, id=id)
        servicedata = TrimServicePrice.objects.filter(trim=obj)
        for s in servicedata:
            servicedata_dict[s.service_item_id] = {
                'min_price': s.min_price,
                'max_price': s.max_price
            }

    for i in cat:
        temp = {}
        temp['category'] = i.name
        items = ServiceItem.objects.filter(category=i.id)

        # Attach prices if available
        for item in items:
            price_data = servicedata_dict.get(item.id)
            if price_data:
                item.min_price = price_data['min_price']
                item.max_price = price_data['max_price']
            else:
                item.min_price = ''
                item.max_price = ''
        
        temp['item'] = items
        service_item.append(temp)
    if request.method == "POST":
        obj=None
        
        if id:
            obj = get_object_or_404(Trim, id=id)
            form = TrimForm(request.POST,instance=obj)
            saved_model_id = obj.model.id
            servicedata=TrimServicePrice.objects.filter(trim=obj).values('service_item_id', 'min_price', 'max_price')
        else:
            form = TrimForm(request.POST)
        if form.is_valid():
            tempsaved=form.save()
            service_ids = request.POST.getlist('service_item_id')
            min_costs = request.POST.getlist('min_cost')
            max_costs = request.POST.getlist('max_cost')
            for service_id, min_price, max_price in zip(service_ids, min_costs, max_costs):
                if min_price and max_price:
                    TrimServicePrice.objects.get_or_create(
                        trim=tempsaved,
                        service_item_id=service_id,
                        min_price=min_price,
                        max_price=max_price
                    )
            messages.success(request, f'Trim has been Added successfully!')
            return redirect('customadmin:trim')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(Trim, id=id)
            form = TrimForm(instance=obj)
            saved_model_id = obj.model.id
            servicedata = TrimServicePrice.objects.filter(trim=obj).values('service_item_id', 'min_price', 'max_price')
            print('servicedata',servicedata)
            
           
        else:
            form = TrimForm()
    
    return render(request, 'customadmin/trim_add.html', {'form': form,'obj':obj,'service_item':service_item,
                                                         'servicedata': servicedata,'saved_model_id': saved_model_id})

def delete_trim(request,id=None):
    if id:
        obj = get_object_or_404(Trim, id=id)
        obj.delete()
        
        messages.success(request, f'Trim has been removed successfully!')
        return redirect('customadmin:trim')
    
def get_model(request):
    category_id = request.GET.get('category_id')
    subcategories = CarModel.objects.filter(company=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

def get_car(request):
    category_id = request.GET.get('category_id')
    subcategories = CarCompany.objects.filter(country__code=category_id).values('id', 'name')
    symbole = Country.objects.get(code=category_id)
    return JsonResponse({'subcategories': list(subcategories),'symbole':symbole.symbole})

def get_trim(request):
    category_id = request.GET.get('category_id')
    subcategories = Trim.objects.filter(model=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

def get_trim_service(request):
    trim_id = request.GET.get('trim_id')
    servicedata_dict = {}
    service_item = []

    if trim_id:
        obj = get_object_or_404(Trim, id=trim_id)
        servicedata = TrimServicePrice.objects.filter(trim=obj)

        for s in servicedata:
            servicedata_dict[s.service_item_id] = {
                'min_price': str(s.min_price),
                'max_price': str(s.max_price)
            }

    categories = ServiceCategory.objects.all()

    for category in categories:
        temp = {}
        temp['name'] = category.name
        temp['image'] = category.image.url if category.image else None
        items = ServiceItem.objects.filter(category=category.id)

        item_list = []
        for item in items:
            price_data = servicedata_dict.get(item.id)
            item_info = {
                'name': item.name,
                'min_price': price_data['min_price'] if price_data else '',
                'max_price': price_data['max_price'] if price_data else ''
            }
            item_list.append(item_info)
        
        temp['items'] = item_list
        service_item.append(temp)

    return JsonResponse({'trimdata': service_item})
def servicecategory(request):
    car=ServiceCategory.objects.all()
    obj=request.GET.get('search')
    if obj:
        if obj == 'all':
            carmodel = ServiceCategory.objects.all()
        else:
            carmodel = ServiceCategory.objects.filter(company=obj)
    else:
        carmodel = ServiceCategory.objects.all()
    return render(request,'customadmin/servicecat.html',{'carmodel':carmodel,'car':car})

def add_servicecategory(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(ServiceCategory, id=id)
            form = ServiceCategoryForm(request.POST,request.FILES,instance=obj)
        else:
            form = ServiceCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Car Services category has been Added successfully!')
            return redirect('customadmin:servicecategory')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(ServiceCategory, id=id)
            form = ServiceCategoryForm(instance=obj)
        else:
            form = ServiceCategoryForm()
    
    return render(request, 'customadmin/servicecat_add.html', {'form': form,'obj':obj})

def delete_servicecategory(request,id=None):
    if id:
        obj = get_object_or_404(ServiceCategory, id=id)
        obj.delete()
        
        messages.success(request, f'Service Category has been removed successfully!')
        return redirect('customadmin:servicecategory')
    
   
def serviceitem(request):
    car=ServiceCategory.objects.all()
    obj=request.GET.get('search')
    if obj:
        if obj == 'all':
            carmodel = ServiceItem.objects.all()
        else:
            carmodel = ServiceItem.objects.filter(category=obj)
    else:
        carmodel = ServiceItem.objects.all()
    return render(request,'customadmin/serviceitem.html',{'carmodel':carmodel,'car':car})

def add_serviceitem(request,id=None):
    print('run')
    if request.method == "POST":
        print('post')
        print(request.POST)
        obj=None
        if id:
            obj = get_object_or_404(ServiceItem, id=id)
            form = ServiceItemForm(request.POST,instance=obj)
        else:
            form = ServiceItemForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Car Services Item has been Added successfully!')
            return redirect('customadmin:serviceitem')
        else:
            print('errr',form.errors)
            
            messages.error(request, f'{form.errors}')
    else:
        obj=None
        if id:
            obj = get_object_or_404(ServiceItem, id=id)
            form = ServiceItemForm(instance=obj)
        else:
            form = ServiceItemForm()
    
    return render(request, 'customadmin/serviceitem_add.html', {'form': form,'obj':obj})

def delete_serviceitem(request,id=None):
    if id:
        obj = get_object_or_404(ServiceItem, id=id)
        obj.delete()
        
        messages.success(request, f'Service Item has been removed successfully!')
        return redirect('customadmin:serviceitem')
    
   

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'customadmin/country.html', {'countries': countries})

def country_create(request):
    form = CountryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Country has been Created successfully!')
        return redirect('customadmin:country_list')
    else:
        messages.error(request, f'{form.errors}')
    return render(request, 'customadmin/country_form.html', {'form': form})

def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
        messages.success(request, f'Country Updated successfully!')
        return redirect('customadmin:country_list')
    else:
        messages.error(request, f'{form.errors}')
    return render(request, 'customadmin/country_form.html', {'form': form})

def country_delete(request, pk):
    if pk:
        obj = get_object_or_404(Country, id=pk)
        if obj:
            obj.delete()
            messages.success(request, f'Country has been removed successfully!')
        else:
            messages.error(request, f'{form.errors}')
        return redirect('customadmin:country_list')
    else:
        messages.error(request, f'{form.errors}')
        return redirect('customadmin:country_list')



def tyre(request):
    tyre = Tyre.objects.all()
    return render(request, 'customadmin/tyre.html', {'tyre': tyre})

def tyre_create(request):
    form = TyreForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Tyre has been Created successfully!')
        return redirect('customadmin:tyre')
    else:
        messages.error(request, f'{form.errors}')
    return render(request, 'customadmin/tyre_add.html', {'form': form})

def tyre_update(request, pk):
    tyre = get_object_or_404(Tyre, pk=pk)
    form = TyreForm(request.POST or None, instance=tyre)
    if form.is_valid():
        form.save()
        messages.success(request, f'Tyre Updated successfully!')
        return redirect('customadmin:tyre')
    else:
        messages.error(request, f'{form.errors}')
    return render(request, 'customadmin/tyre_add.html', {'form': form})

def tyre_delete(request, pk):
    if pk:
        obj = get_object_or_404(Tyre, id=pk)
        if obj:
            obj.delete()
            messages.success(request, f'Tyre has been removed successfully!')
        
        return redirect('customadmin:tyre')
    else:
        
        return redirect('customadmin:tyre')




