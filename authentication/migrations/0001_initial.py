# Generated by Django 4.1.7 on 2023-02-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=30)),
            ],
        ),
    ]
