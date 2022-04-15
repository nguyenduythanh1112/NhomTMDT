from django.contrib import admin
from mobilephone import models
admin.site.register(models.MobilePhone)
admin.site.register(models.MobilePhoneBrand)
admin.site.register(models.MobilePhoneStats)