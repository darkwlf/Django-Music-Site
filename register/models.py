from django.db import models

class User(models.Model):

    username = models.CharField(max_length=50, default='username')

    email = models.CharField(max_length=220, default='email')

    phone_number = models.IntegerField(default='091234567')

    name = models.CharField(max_length=60, default='name')

    passsword = models.CharField(max_length=300, default='password')