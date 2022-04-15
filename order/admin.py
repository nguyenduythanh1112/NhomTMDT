from django.contrib import admin
from order import models

admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.Payment)
admin.site.register(models.Shipment)
admin.site.register(models.Cash)
admin.site.register(models.Check_Payment)
admin.site.register(models.Credit)
admin.site.register(models.Paypal)