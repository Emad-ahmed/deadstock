# Generated by Django 3.2.9 on 2023-11-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gulfapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exceldata',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='exceldata',
            name='product',
            field=models.CharField(max_length=500),
        ),
    ]
