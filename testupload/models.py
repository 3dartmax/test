from django.db import models
from django.conf import settings

class Notice(models.Model):
    author       = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 1대1 중복허용 안됨.
    title        = models.CharField(max_length=50)
    content      = models.TextField()
    photo        = models.ImageField(blank=True, null=True)                                 # pip install Pillow
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def username(self):
        return self.author.username
    def imagename(self):
        texts  = self.photo.url.split('/')
        length = len(texts)
        return texts[length - 1]
    def imageurl(self):
        return self.photo.url
    def imagewidth(self):
        return self.photo.width
    def imageheight(self):
        return self.photo. height


class Board(models.Model):
    title        = models.CharField(max_length=30)
    content      = models.TextField()
    upload       = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def filename(self):
        texts  = self.upload.url.split('/')[-1]
        if len(texts) > 0:
            return texts[0]
        else:
            return ''
    def fileurl(self):
        return self.upload.url


class Product(models.Model):
    image     = models.ImageField(upload_to='product/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, editable=False)  # editable = false : db추가시 표시하지 않는다.
    def save(self, *args, **kwargs):
        self.image_url = 'http://localhost:8000/media/product/{0}'.format(self.image.url.split('/')[-1])
        super(Product, self).save()
