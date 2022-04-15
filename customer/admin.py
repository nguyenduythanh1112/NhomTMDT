from pyexpat import model
from django.contrib import admin
from customer import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Account)
admin.site.register(models.FullName)
admin.site.register(models.Address)

admin.site.register(models.CustomerMember)
admin.site.register(models.CustomerMember)
