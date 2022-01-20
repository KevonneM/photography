from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title