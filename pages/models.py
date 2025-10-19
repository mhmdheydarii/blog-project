from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    author = models.CharField() 
    # catgory = 
    # tag = 
    status = models.BooleanField(default=False)
    # comment = 
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']