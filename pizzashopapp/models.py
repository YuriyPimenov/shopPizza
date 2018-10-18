from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop',verbose_name='Владелец')
    name = models.CharField(max_length=100,verbose_name='Название пиццерии')
    phone = models.CharField(max_length=100,verbose_name='Телефон')
    address = models.CharField(max_length=100,verbose_name='Адрес')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False,verbose_name='Логотип')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE, verbose_name='Пиццерия')
    name = models.CharField(max_length=100,verbose_name='Название пиццы')
    short_description = models.CharField(max_length=100,verbose_name='Описание')
    price = models.IntegerField(default=0,verbose_name='Цена')
    image = models.ImageField(upload_to='pizza_images/', blank=False,verbose_name='Изображение')

    def __str__(self):
        return self.name