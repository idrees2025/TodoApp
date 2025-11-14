from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=222)
    Dsc=models.TextField()
    photo=models.ImageField(upload_to='photo')

    def __str__(self):
        return f'{self.id}'