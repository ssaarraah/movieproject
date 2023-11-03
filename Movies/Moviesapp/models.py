from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200)

    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to="Photos")

    def __str__(self):
        return self.name