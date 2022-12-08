from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateField(auto_now=True)

class Team(models.Model):
    rasm = models.ImageField(upload_to='media')
    ism = models.CharField(max_length=50)
    ishi = models.CharField(max_length=50)
    matn = models.CharField(max_length=100)
    skype = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linked = models.CharField(max_length=200)


class Service(models.Model):
    rasmi = models.ImageField(upload_to='media')
    nomi = models.CharField(max_length=40)
    matni = models.CharField(max_length=100)

class Message(models.Model):
    ismi = models.CharField(max_length=50)
    mail = models.EmailField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)

