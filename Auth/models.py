from django.db import models

# Create your models here.




class UserII(models.Model):
    password = models.TextField()
    username = models.CharField(max_length = 30)
    phonenumber = models.TextField()
    adress = models.TextField()








