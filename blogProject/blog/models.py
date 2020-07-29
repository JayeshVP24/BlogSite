from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def approveComments(self):
        return self.comments.filter(approvedComments = True)

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments') 
    author = models.CharField(max_length=200)
    text = models.TextField()
    createDate = models.DateField(default=True)
    approvedComments = models.BooleanField(default=False)

    def approve(self):
        self.approvedComments = True
        self.save()

    def get_absolute_url(self):
        return reverse('postList', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text