from django.db import models

class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name       = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
        return self.name;
# >>> p = Person(name="Fred Flintstone", shirt_size="L")
# >>> p.save()
# >>> p.shirt_size
# 'L'
# >>> p.get_shirt_size_display()
# 'Large'


class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.instrument


class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    artist       = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars    = models.IntegerField()
    def __str__(self):
        return self.name


class Fruit(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.name
# >>> fruit = Fruit.objects.create(name='Apple')
# >>> fruit.name = 'Pear'
# >>> fruit.save()
# >>> Fruit.objects.values_list('name', flat=True)
# ['Apple', 'Pear']


class PersonEx(models.Model):
    # verbose_name = 자세한 필드 이름
    first_name = models.CharField("'Person's first name", max_length=30)
    last_name  = models.CharField(verbose_name="'Person's last name", max_length=30)
