# myapp/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myapp'
