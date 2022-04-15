from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    phone=models.TextField(max_length=255)
    sex=models.TextField(max_length=255)
    dateOfBirth=models.DateField()
    def __str__(self):
        return str(self.id)

class Account(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.TextField(max_length=255)
    password=models.TextField(max_length=255)
    role=models.TextField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class FullName(models.Model):
    id=models.AutoField(primary_key=True)
    fullName=models.TextField(max_length=255)
    lastName=models.TextField(max_length=255)
    firtName=models.TextField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullName

class Address(models.Model):
    id=models.AutoField(primary_key=True)
    number=models.TextField(max_length=255)
    street=models.TextField(max_length=255)
    district=models.TextField(max_length=255)
    city=models.TextField(max_length=255)
    country=models.TextField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.number + "-" + self.street + "-" + self.city + "-" + self.country 

class CustomerNew(Customer,models.Model):
    #id=models.AutoField(primary_key=True)
    registered=models.DateField()
    note=models.TextField(max_length=255)
    def __str__(self):
        return self.id

class CustomerMember(Customer,models.Model):
    #id=models.AutoField(primary_key=True)
    card=models.TextField(max_length=255)
    MemberGrade=models.IntegerField()
    def __str__(self):
        return self.id