from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Group(models.Model):
    name    = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')  # 다대다
    def __str__(self):
        return self.name

class Membership(models.Model):
    person        = models.ForeignKey(Person, on_delete=models.CASCADE)
    group         = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined   = models.DateField()
    invite_reason = models.CharField(max_length=64)
    def __str__(self):
        return self.invite_reason
# >>> from test2.models import Person, Group, Membership
# >>> from django.utils import timezone
# >>> ringo = Person.objects.create(name="Ringo Starr")
# >>> paul = Person.objects.create(name="Paul McCartney")
# >>> beatles = Group.objects.create(name="The Beatles")
# >>> m1 = Membership(person=ringo, group=beatles,
# ...      date_joined=timezone.now(),
# ...      invite_reason="Needed a new drummer.")
# >>> m1.save()
# >>> beatles.members.all()
# [<Person: Ringo Starr>]
# >>> ringo.group_set.all()
# [<Group: The Beatles>]
# >>> m2 = Membership.objects.create(person=paul, group=beatles,
# ...      date_joined=timezone.now(),
# ...      invite_reason="Wanted to form a band.")
# >>> beatles.members.all()
# [<Person: Ringo Starr>, <Person: Paul McCartney>]
# >>> ringo.membership_set.all()
# [<Membership: Membership object>]
# >>> beatles.membership_set.all()
# [<Membership: Membership object>, <Membership: Membership object>]
# >>> mfind = Membership.objects.get(person=ringo, group=beatles)
# >>> mfind.date_joined
# datetime.date(2016, 3, 14)
# >>> mfind.invite_reason
# 'Needed a new drummer.'
# >>> Person.objects.filter(group__name='The Beatles', membership__date_joined__gt=datetime.date(1961,1,1))
# [<Person: Ringo Starr>, <Person: Paul McCartney>]
