# Generated by Django 4.1.7 on 2023-02-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default='', upload_to='auth/images'),
        ),
    ]
