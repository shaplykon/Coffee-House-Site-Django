from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from accounts.models import Account

class Coffee(models.Model):
    name = models.CharField(max_length=30, default='')
    coffee_picture = models.ImageField(blank=True, null=True)
    gluten_free = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    favourite = models.ManyToManyField(Account, related_name='coffee_favourite', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_coffee', args=[str(self.id)])


class Tea(models.Model):
    name = models.CharField(max_length=30, default='')
    tea_picture = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=0)
    favourite = models.ManyToManyField(Account, related_name='tea_favourite', blank=True)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=30, default='')
    price = models.FloatField(default=0)
    dessert_picture = models.ImageField(blank=True, null=True)
    calorific = models.FloatField(default=0)
    favourite = models.ManyToManyField(Account, related_name='desserts_favourite', blank=True)

    def __str__(self):
        return self.name
