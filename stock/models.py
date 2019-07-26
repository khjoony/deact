from django.db import models

# Create your models here.
class Kospi(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Kosdak(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    sector = models.TextField(null=True)
    feature = models.TextField(null=True)

    def __str__(self):
        return self.name