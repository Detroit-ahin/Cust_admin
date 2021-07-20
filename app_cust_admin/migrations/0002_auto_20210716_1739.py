# Generated by Django 3.0.6 on 2021-07-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cust_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_list',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user_list',
            name='fullname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_list',
            name='profession',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
