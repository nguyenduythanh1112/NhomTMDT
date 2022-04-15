from django.contrib import admin
from laptop import models
# Register your models here.
admin.site.register(models.Laptop)
admin.site.register(models.LaptopBrand)
admin.site.register(models.LaptopStats)