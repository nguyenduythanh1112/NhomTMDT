from django.db import models
class ClothesBrand(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    createAt=models.DateField()
    def __str__(self):
        return self.name
class Clothes(models.Model):
    ID=models.IntegerField(primary_key=True)
    type=models.TextField(max_length=255)
    description=models.TextField()
    material=models.TextField(max_length=255)
    color=models.TextField(max_length=255)
    gender=models.TextField(max_length=255)
    size=models.TextField(max_length=255)
    name=models.TextField(max_length=255)
    season=models.TextField(max_length=255)
    img=models.ImageField(upload_to = 'pictures', null=True, blank=True)
    clothesBrand=models.ForeignKey(ClothesBrand,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class ClothesStats(models.Model):
    ID=models.IntegerField(primary_key=True)
    barcode=models.TextField()
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    clothes=models.ForeignKey(Clothes ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)