# Generated by Django 5.1.3 on 2024-11-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='code',
            field=models.IntegerField(null=True, verbose_name='code'),
        ),
    ]
