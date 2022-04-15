from distutils.command.upload import upload
from django.db import models
from django.forms import DateField
from customer.models import Customer
from book.models import Book
from clothes.models import Clothes

class Item(models.Model):
    id=models.AutoField(primary_key=True)
    barcode=models.TextField(max_length=1000)
    price=models.FloatField()
    discount=models.FloatField()
    def __str__(self):
        return self.barcode
class LineItem(models.Model):
    id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()

class BookItem(Item,models.Model):
    # id=models.AutoField(primary_key=True)
    bookFile=models.TextField(max_length=1000)
    book=models.OneToOneField(Book,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
class ClothesItem(Item,models.Model):
    # id=models.AutoField(primary_key=True)
    clothes=models.OneToOneField(Clothes,on_delete=models.CASCADE)
    def __str__(self):
        return self.barcode
class LaptopItem(Item,models.Model):
    # id=models.AutoField(primary_key=True)
    guarantee=models.TextField()
    installment=models.TextField()
    def __str__(self):
        return str(self.id)
class MobilePhoneItem(Item,models.Model):
    # id=models.AutoField(primary_key=True)
    guarantee=models.TextField()
    installment=models.TextField()
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField();
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Rating(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)