from import_export import resources
from .models import Workout

class WorkoutResource(resources.ModelResource):
    class Meta:
        model = Workout
        import_id_fields = ['wid']
        exclude = ['wid', 'pid']