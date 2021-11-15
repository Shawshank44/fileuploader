from django.db import models

# Create your models here.


class User_files(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='img',blank=True)
    myfile = models.FileField(upload_to='doc',blank=True)
    # date = models.DateField()