from django.db import models

# Create your models here.

class Authentication(models.Model):
    person_id = models.AutoField
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.userName

class Notice(models.Model):
    date = models.DateField(auto_now_add= True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "notice/images", default="")

    def __str__(self):
        return self.title

        