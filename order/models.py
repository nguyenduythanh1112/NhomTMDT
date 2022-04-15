from django.db import models
from customer.models import Customer

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    totalPrice = models.FloatField()
    created = models.DateField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.id 

class Order(models.Model):
    id = models.AutoField( primary_key=True)
    date = models.DateField()
    status = models.TextField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)    
    def __str__(self):
        return self.id    

class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    selectship = models.TextField(max_length=255)
    codeship = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    def __str__(self):
        return self.id 
  
class Cash(Payment,models.Model):
    cashTendered= models.FloatField()
    #payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    
class Check_Payment(Payment,models.Model):
    name = models.TextField(max_length=255)
    bankID = models.TextField(max_length=255)
    #payment=models.ForeignKey(Payment,on_delete=models.CASCADE)

class Credit(Payment,models.Model):
    number = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    expdate = models.DateField()
    #payment=models.ForeignKey(Payment,on_delete=models.CASCADE)

class Paypal(Payment,models.Model):
    pass
