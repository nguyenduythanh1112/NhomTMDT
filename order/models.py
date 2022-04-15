from select import select
from django.db import models
from unicodedata import name

# Create your models here.
class Order(models.Model):
    id=models.AutoField( primary_key=True)
    date=models.DateField()
    status=models.TextField()
    def __str__(self):
        return self.id

class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    totalPrice=models.FloatField()
    created=models.DateField()
    def __str__(self):
        return self.id       

class Shipment(models.Model):
    id=models.AutoField(primary_key=True)
    selectship=models.TextField()
    codeship=models.TextField()
    address = models.TextField()
    def __str__(self):
        return self.id 

class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.IntegerField()    
    def __str__(self):
        return self.id 
    
class Cash(Payment,models.Model):
    CashTendered= models.FloatField()
    book=models.OneToOneField(Book,on_delete=models.CASCADE)