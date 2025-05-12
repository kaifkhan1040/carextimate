from django.contrib import admin
from .models import CarCompany, CarModel, Trim,ServiceCategory,ServiceItem,TrimServicePrice
from .forms import CarCompanyForm, CarModelForm, TrimForm

admin.site.register(CarCompany)
admin.site.register(CarModel)
# admin.site.register(Trim)
admin.site.register(ServiceCategory)
admin.site.register(ServiceItem)
# Register your models here.
class TrimServicePriceInline(admin.TabularInline):
    model = TrimServicePrice
    extra = 1

@admin.register(Trim)
class TrimAdmin(admin.ModelAdmin):
    inlines = [TrimServicePriceInline]