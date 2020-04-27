from import_export import resources
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout

class WorkoutResource(resources.ModelResource):
    class Meta:
        model = Workout
        import_id_fields = ['wid']
        exclude = ['wid', 'pid', 'user']