from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Cars(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    marka = models.CharField(max_length = 150)
    model = models.CharField(max_length = 150)
    description = RichTextField()
    added_date = models.DateTimeField( auto_now_add=True)
    photo = models.FileField(upload_to='photo',blank=True,null=True)

class Comment(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    car=models.ForeignKey(Cars,on_delete=models.CASCADE,verbose_name="masin",related_name="comments")
    comment_content=RichTextField()
    added_date = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"{self.comment_content}"



    
    
    
