from django.contrib import admin
from item import models

admin.site.register(models.Item)
admin.site.register(models.BookItem)
admin.site.register(models.ClothesItem)
admin.site.register(models.LaptopItem)
admin.site.register(models.MobilePhoneItem)
admin.site.register(models.Comment)
admin.site.register(models.Rating)
admin.site.register(models.LineItem)