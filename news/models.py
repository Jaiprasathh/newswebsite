from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categories(models.Model):
    category=models.CharField(max_length=50)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    #To display the content as a string instead of an object
    def __str__(self):
        return self.category
    
status_choices=[
    ('Published', 'Published'),
    ('Drafted', 'Drafted')
]

class articles(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    image=models.ImageField(upload_to='media')
    category=models.ForeignKey (categories,on_delete=models.CASCADE)
    author=models.ForeignKey (User,on_delete=models.CASCADE)
    short_description=models.CharField(max_length=10000)
    detail_description=models.TextField(max_length=1000000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=status_choices)
    is_trending=models.BooleanField(default=False)