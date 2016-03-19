from django.db import models
from django.conf import settings

class Person(models.Model):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 1대1 즉 절대 중복되지 못한다.
    title = models.CharField(max_length=30)
    log   = models.TextField()
    def __str__(self):
        return self.title
    def username(self):
        return self.user.username
# >>> from django.contrib.auth.models import User
# >>> user = User.objects.get(id=1)
# >>> user.username
# 'admin'
# >>> data = Person.objects.create(user=user, title='first error', log='^^~~~;;;')
# >>> data.save()
# >>> data.username()
# 'admin'