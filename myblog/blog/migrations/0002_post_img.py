# Generated by Django 4.2.13 on 2024-05-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
