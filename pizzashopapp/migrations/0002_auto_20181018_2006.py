# Generated by Django 2.0.5 on 2018-10-18 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название пиццы')),
                ('short_description', models.CharField(max_length=100, verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='pizza_images/', verbose_name='Изображение')),
            ],
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='logo',
            field=models.ImageField(upload_to='pizzashop_logo/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название пиццерии'),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizzashop', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizzashop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop', verbose_name='Пиццерия'),
        ),
    ]
