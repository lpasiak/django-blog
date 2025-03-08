from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # if it was, auto_now_add=True it wouldn't be able to be updated 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted, his posts will be deleted as well

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

    # Setting a redirect, get_absolute_url method (IntegrityError)
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
