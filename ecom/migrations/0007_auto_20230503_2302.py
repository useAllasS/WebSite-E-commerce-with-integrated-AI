# Generated by Django 3.0.5 on 2023-05-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20230430_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
