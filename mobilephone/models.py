from django.db import models
from unicodedata import name
from django.db import models
from laptop.models import Producer
class MobilePhoneBrand(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    createAt=models.DateField()
    def __str__(self):
        return self.name

class MobilePhone(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    color=models.TextField()
    material=models.TextField()
    CPU=models.TextField()
    RAM=models.TextField()
    GPU=models.TextField()
    OS=models.TextField()
    screenSize=models.FloatField()
    storage=models.TextField()
    battery=models.TextField()
    weight=models.FloatField()
    warrantyPeriod=models.TextField()
    touchID=models.TextField()
    sims=models.TextField()
    frontCamera=models.TextField()
    rearCamera=models.TextField()
    img=models.ImageField()
    mobilePhoneBrand=models.ForeignKey(MobilePhoneBrand,on_delete=models.CASCADE)
    producer=models.ForeignKey(Producer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class MobilePhoneStats(models.Model):
    ID=models.IntegerField(primary_key=True)
    barcode=models.TextField()
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    mobilePhone=models.ForeignKey(MobilePhone ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)