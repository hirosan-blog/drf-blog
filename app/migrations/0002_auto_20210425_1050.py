# Generated by Django 3.1.8 on 2021-04-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='イメージ画像'),
        ),
    ]
