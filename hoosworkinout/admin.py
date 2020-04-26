from django.contrib import admin
from .models import User, Workout, Location, WorkedOutAt, Exercise, Plan, Cardio, Hiit, Strength, Reps
# Register your models here.

admin.site.register(Workout)
admin.site.register(Location)
admin.site.register(WorkedOutAt)
admin.site.register(Exercise)
admin.site.register(Reps)
admin.site.register(Plan)
admin.site.register(Cardio)
admin.site.register(Hiit)
admin.site.register(Strength)
# admin.site.register(Athlete)
