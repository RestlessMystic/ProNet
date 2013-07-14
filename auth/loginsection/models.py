from django.db import models
class Userprofile(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=40)
	email = models.EmailField()
