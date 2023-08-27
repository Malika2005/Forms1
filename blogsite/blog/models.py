from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=60)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} - {self.title} - {self.likes}'

    def get_absolute_url(self):
        return reverse('post_detail.html', args=(self.pk, ))
