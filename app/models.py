from django.db import models
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    published_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title


class Specification(models.Model):
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.value}"
   
    
