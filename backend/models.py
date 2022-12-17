from django.db import models
import random


def generateunique() -> str:
    return random.randint(1000000, 9999999)


class Category(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz
        
    @property
    def ImageURL(self):
        try:
            return self.image.url
        except:
            return ''


class User(models.Model):
    user_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    lang = models.CharField(max_length=20, null=True, blank=True)
    order_type = models.CharField(max_length=25, null=True, blank=True)
    interests = models.ManyToManyField(to=Category)
    phone = models.CharField(max_length=20, null=True, blank=True)
    new_phone = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=20, null=True, blank=True)