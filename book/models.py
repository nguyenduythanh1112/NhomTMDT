from django.db import models
from django.db import models
from django.forms import DateField

class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=255)
    biography=models.TextField(max_length=255)
    def __str__(self):
        return self.name
class Publisher (models.Model,models.Manager):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=255)
    address=models.TextField(max_length=255)
    def __str__(self):
        return self.name
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=255)
    createAt=DateField()
    def __str__(self):
        return self.name
class Book(models.Model):
    ISBN=models.CharField(max_length=255, primary_key=True)
    title=models.TextField(max_length=255)
    numberOfPage=models.IntegerField()
    language=models.TextField(max_length=255)
    img=models.ImageField(upload_to = 'book/static/img', null=True, blank=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    category=models.ForeignKey(Category ,on_delete=models.CASCADE)
    author=models.ForeignKey(Author ,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class BookStats(models.Model):
    id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

