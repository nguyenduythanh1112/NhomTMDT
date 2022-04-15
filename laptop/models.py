from django.db import models
from unicodedata import name
from django.db import models

class LaptopBrand(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    createAt=models.DateField()
    def __str__(self):
        return self.name
class Producer(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    address=models.TextField()
    def __str__(self):
        return self.name
class Laptop(models.Model):
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
    speaker=models.TextField()
    type=models.TextField()
    webCam=models.TextField()
    keyborad=models.TextField()
    touchID=models.TextField()
    img=models.ImageField()
    laptopBrand=models.ForeignKey(LaptopBrand,on_delete=models.CASCADE)
    producer=models.ForeignKey(Producer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class LaptopStats(models.Model):
    ID=models.IntegerField(primary_key=True)
    barcode=models.TextField()
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    laptop=models.ForeignKey(Laptop ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)