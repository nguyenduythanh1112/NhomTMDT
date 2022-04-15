from django.contrib import admin

# Register your models here.
from clothes import models
admin.site.register(models.Clothes)
admin.site.register(models.ClothesBrand)
admin.site.register(models.ClothesStats)