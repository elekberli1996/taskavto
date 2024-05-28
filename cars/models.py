from django.db import models

# Create your models here.

class Cars(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    marka = models.CharField(max_length = 150)
    model = models.CharField(max_length = 150)
    description = models.TextField()
    added_date = models.DateTimeField( auto_now_add=True)
    
    
    
    
