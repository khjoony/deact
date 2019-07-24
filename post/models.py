from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()

    def __str__(self):
        """Representation of the model as string. """
        return self.title
        