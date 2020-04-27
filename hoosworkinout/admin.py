from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .models import User, Profile, Workout, Location, WorkedOutAt, Exercise, Plan, Cardio, Hiit, Strength, Reps
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(Workout)
class WorkoutAdmin(ImportExportModelAdmin):
    class Meta:
        model = Workout
        import_id_fields = ['wid']

@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(ImportExportModelAdmin):
    pass

@admin.register(WorkedOutAt)
class WorkedOutAtAdmin(ImportExportModelAdmin):
    pass

@admin.register(Reps)
class RepAdmin(ImportExportModelAdmin):
    pass

@admin.register(Plan)
class PlanAdmin(ImportExportModelAdmin):
    pass

@admin.register(Cardio)
class CardioAdmin(ImportExportModelAdmin):
    pass

@admin.register(Hiit)
class HiitAdmin(ImportExportModelAdmin):
    pass

@admin.register(Strength)
class StrengthAdmin(ImportExportModelAdmin):
    pass

