from django.db import models
class Userprofile(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=40)
	email = models.EmailField()
	
	isA = models.CharField(max_length = 3)
	isB = models.CharField(max_length = 3)
	isC = models.CharField(max_length = 3)
	isD = models.CharField(max_length = 3)
	isE = models.CharField(max_length = 3)
	isF = models.CharField(max_length = 3)
	isG = models.CharField(max_length = 3)
	isH = models.CharField(max_length = 3)
	isI = models.CharField(max_length = 3)

