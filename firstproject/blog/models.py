from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    link_field = models.URLField(max_length=200, default='DEFAULT LINK')
    image = models.ImageField(upload_to='static/images', default='default.jpg')

    def __str__(self):
        return self.title


    def get_url_post(self):
        return f'/blog/detail/{self.id}'
