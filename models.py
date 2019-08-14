from django.db import models

# Create your models here.

class Start(models.Model):
    class_name = models.CharField(max_length=40)
    prof_name=models.CharField(max_length=40)
    comment=models.TextField()

    def __str__(self):
        return self.class_name 
