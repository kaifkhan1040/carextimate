from django.db import models

SYMBOL_CHOICES = [
    ('$', '$'), 
    ('€', '€'), 
    ('£', '£'), 
    ('¥', '¥'), 
    ('¥元', '¥ / 元'), 
    ('₹', '₹'), 
    ('A$', 'A$'), 
    ('C$', 'C$'), 
    ('CHF', 'CHF'), 
    ('₽', '₽'), 
    ('₩', '₩'), 
    ('R$', 'R$'), 
    ('ZAR', 'R'), 
    ('Mex$', 'Mex$'), 
    ('NZ$', 'NZ$'), 
    ('S$', 'S$'), 
    ('HK$', 'HK$'), 
    ('SEK', 'kr (SEK)'), 
    ('NOK', 'kr (NOK)'), 
    ('DKK', 'kr (DKK)'), 
    ('₺', '₺'), 
    ('฿', '฿'), 
    ('RM', 'RM'), 
    ('Rp', 'Rp'), 
    ('₱', '₱'), 
    ('₪', '₪'), 
    ('SR', 'SR'), 
    ('E£', 'E£'), 
    ('₫', '₫'), 
    ('₦', '₦'),
]



# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)  # e.g., "IN", "US"
    symbole = models.CharField(max_length=5,choices=SYMBOL_CHOICES)

    def __str__(self):
        return self.name

class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')

    def __str__(self):
        return self.name
    

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name
  

    
    
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='service/')
    
    def __str__(self):
        return self.name

class ServiceItem(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
      
class Trim(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name='trim_models')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='trims')

    def __str__(self):
        return self.name
    
class TrimServicePrice(models.Model):
    trim = models.ForeignKey(Trim, on_delete=models.CASCADE, related_name='service_prices')
    service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE, related_name='trim_prices')
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('trim', 'service_item')

    def __str__(self):
        return f"{self.trim} - {self.service_item.name}: ₹{self.min_price} - ₹{self.max_price}"

    
  
class Tyre(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='tyre_country')
    name = models.CharField(max_length=100)
    company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name='tyre_models')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='tyre')
    trim = models.ForeignKey(Trim, on_delete=models.CASCADE, related_name='tyre_trim')
    width = models.FloatField()
    profile = models.FloatField()
    rim = models.FloatField()
    load = models.FloatField()
    speed = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} - {self.size}"
