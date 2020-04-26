# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    body_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    best_lift = models.IntegerField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        db_table = 'profile'


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, db_column='username')
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

#    def __str__(self):
#        return self.name

    class Meta:
        db_table = 'plan'



class Workout(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, db_column='username')
    wid = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    pid = models.ForeignKey(Plan, on_delete = models.CASCADE, db_column='pid', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workout'

class Location(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'location'


class WorkedOutAt(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, db_column='username')
    wid = models.ForeignKey(Workout, on_delete = models.CASCADE, db_column='wid')
    lid = models.ForeignKey(Location, on_delete = models.CASCADE, db_column='lid')


    class Meta:
        db_table = 'worked_out_at'

class Exercise(models.Model):
    user = models.ForeignKey(User,  on_delete = models.CASCADE, db_column='username')
    wid = models.ForeignKey(Workout,  on_delete = models.CASCADE, db_column='wid')
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'exercise'



class Cardio(models.Model):
    eid = models.OneToOneField(Exercise, on_delete = models.CASCADE, db_column='eid', primary_key=True)
    duration = models.IntegerField()
    distance = models.DecimalField(max_digits=4, decimal_places=1)
    calories_burned = models.IntegerField(blank=True, null=True)
    peak_heartrate = models.IntegerField(blank=True, null=True)



    class Meta:
        db_table = 'cardio'


class Hiit(models.Model):
    eid = models.OneToOneField(Exercise, on_delete = models.CASCADE, db_column='eid', primary_key=True)
    distance = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    name = models.CharField(max_length=16)
    calories_burned = models.IntegerField()
    peak_heartrate = models.IntegerField()
    rest_interval = models.IntegerField()
    work_interval = models.IntegerField()

    class Meta:
        db_table = 'hiit'

class Strength(models.Model):
    eid = models.OneToOneField(Exercise, on_delete = models.CASCADE, db_column='eid', primary_key=True)
    weight = models.IntegerField()
    category = models.CharField(max_length=24)
    sets = models.IntegerField()

    class Meta:
        db_table = 'strength'

class Reps(models.Model):
    id = models.IntegerField(primary_key=True)
    eid = models.ForeignKey(Exercise, on_delete = models.CASCADE, db_column='eid')
    numbers = models.IntegerField()

    class Meta:
        db_table = 'reps'
