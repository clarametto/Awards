from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create models here.
class Category(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=500,  null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

  