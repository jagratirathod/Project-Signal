from django.db import models
import uuid
import datetime

# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(primary_key=True,unique= True, default= uuid.uuid4)
    title = models.CharField(max_length= 100, null= True )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

        