from distutils.command.upload import upload
from django.db import models
from django.forms import DateField

class Item(models.Model):
    id=models.AutoField(primary_key=True)
    barcode=models.TextField(max_length=1000)
    price=models.FloatField()
    discount=models.FloatField()
    def __str__(self):
        return self.barcode


class BookItem(Item,models.Model):
    id=models.AutoField(primary_key=True)
    bookFile=models.TextField(max_length=1000)
    book=models.OneToOneField(Book,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
class ClothesItem(models.Model):
    id=models.AutoField(primary_key=True)
    clothes=models.OneToOneField(Clothes,on_delete=models.CASCADE)
    def __str__(self):
        return self.barcode

class LaptopItem






class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField();
    customer=models.ForeignKey()
    def __str__(self):
        return self.name

