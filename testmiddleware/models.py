from django.db import models
from django.db.models.base import ModelState
from datetime import datetime

class Memo(models.Model):
    title        = models.CharField(max_length=30)
    content      = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def getdict(self):
        return self.__dict__
    def getfields(self):
        fields = { 'id' : self.__dict__['id'], }
        for key in self.__dict__.keys():
            value = self.__dict__[key]
            if key != 'id':
                if isinstance(value, datetime):
                    fields[key] = '{0}-{1}-{2} {3}:{4}:{5}'.format(value.year, value.month, value.day, value.hour, value.minute, value.second)
                elif isinstance(value, ModelState) == False:
                    fields[key] = value
                else:
                    print('[ Skip ] Key({0}), type({1})', key, type(value))
        return fields
