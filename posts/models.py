from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length= 300)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.marca