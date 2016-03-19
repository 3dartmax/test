from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title        = models.CharField(max_length=100)
    content      = models.TextField()
    image        = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post    = models.ForeignKey(Post)
    message = models.TextField()
    def __str__(self):
        return self.message
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.post_id])
