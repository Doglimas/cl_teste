from django.db import models
from datetime import datetime


class Postagem (models.Model):
    username = models.CharField(max_length = 30)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 150)
    created_datetime = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.username
    
