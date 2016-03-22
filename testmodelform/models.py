from django.db import models
from django.core.urlresolvers import reverse

TITLE_CHOICES = (
    ('MR',  'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS',  'Ms.'),
)

class Author(models.Model):
    name       = models.CharField(max_length=30)
    title      = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('testmodelform:author_list')

class Book(models.Model):
    name    = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author,related_name='list')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('testmodelform:book_list')
