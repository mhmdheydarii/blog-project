from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Catgory(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

        

class Post(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    catgory = models.ManyToManyField(Catgory)
    # tag = 
    status = models.BooleanField(default=False)
    # comment = 
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']