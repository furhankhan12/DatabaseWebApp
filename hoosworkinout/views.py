from django.urls import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView
from .models import Workout, Profile, User, Exercise, Cardio, Strength, Hiit, Plan, Reps, Location, WorkedOutAt
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class WorkoutDetailView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = 'workouts'
    template_name = 'hoosworkinout/workout-detail.html'

    def get_queryset(self):
        return Workout.objects.filter(wid = self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(WorkoutDetailView, self).get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.filter(wid = self.kwargs.get('pk'))
        context['strengths'] = Strength.objects.all()
        context['cardios'] = Cardio.objects.all()
        context['hiits'] = Hiit.objects.all()
        context['reps'] = Reps.objects.all()
        context['locations'] = WorkedOutAt.objects.all()
        context['plans'] = Plan.objects.filter(user_id= self.request.user.id)

        return context

class DeleteWorkoutView(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = reverse_lazy('home')

class HomeView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'hoosworkinout/home.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['plans'] = Plan.objects.filter(user_id= self.request.user.id)
        context['locations'] = WorkedOutAt.objects.all()
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/profile.html'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['birthday', 'body_weight', 'best_lift']
    template_name = 'hoosworkinout/profile_form.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def form_valid(self, form):
        user = form.save(commit=False)
        form = form.cleaned_data
        user.profile.birthday = form['birthday']
        user.profile.best_lift = form['best_lift']
        user.profile.body_weight = form['body_weight']
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile');


class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ('pid', 'comment', 'name', 'date')

    def form_valid(self, form):
       candidate = form.save(commit=False)
       candidate.user = User.objects.filter(username=self.request.user.username)[0]
       candidate.save()
       return redirect(self.get_success_url())

    def get_form(self, *args, **kwargs):
       form = super(CreateWorkoutView, self).get_form(*args, **kwargs)
       form.fields['pid'].queryset = Plan.objects.filter(user_id = self.request.user.profile.user_id)
       return form


    def get_success_url(self):
        return reverse('set-location')

class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'address', 'phone']
    template_name = 'hoosworkinout/add_location_form.html'

    def form_valid(self, form):
       candidate = form.save(commit=False)
       candidate.user = User.objects.filter(id=self.request.user.id)[0]
       candidate.save()
       return redirect(self.get_success_url())

    def get_success_url(self):
         return reverse('home')



class AddLocationView(LoginRequiredMixin, CreateView):
    model = WorkedOutAt
    fields = ['wid', 'lid']
    template_name = 'hoosworkinout/location_form.html'

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(id=self.request.user.id)[0]
        candidate.save()
        return redirect(self.get_success_url())

    def get_form(self, *args, **kwargs):
       form = super(AddLocationView, self).get_form(*args, **kwargs)
       form.fields['wid'].queryset = Workout.objects.filter(user_id = self.request.user.profile.user_id)
       form.fields['lid'].queryset = Location.objects.filter(user_id = self.request.user.profile.user_id)
       return form

    def get_success_url(self):
        return reverse('home')



#Generic exercise view - not really used
class CreateExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('wid', 'comment', 'name')

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

'''
Each exercise form has TWO methods: One that creates the actual exercise model,
and a helper method that fills in the specific fields for that exercise (cardio,
strength, or hiit. This is because you can't really edit two models in the same
CreateView, so the first one creates the exercise model and then bounces you
to the second one to create the cardio, strength, or hiit model.

The get_form() overrride allows you to filter the dropdowns for wid and eid in
those forms. Below, it is used to only show the workouts and exercises associated with
the username of the currently logged user.

The form_valid() override allows to automatically save the workout or exercise to
the currently logged user. This eliminates the need to select yourself from the
dropdown and improves security by making sure you can't select other users.


'''
class CreateCardioExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('wid', 'comment', 'name')

    def get_form(self, *args, **kwargs):
        form = super(CreateCardioExerciseView, self).get_form(*args, **kwargs)
        form.fields['wid'].queryset = Workout.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('cardio')

class CardioHelper(LoginRequiredMixin, CreateView):
    model = Cardio
    fields = ('eid', 'duration', 'distance', 'calories_burned', 'peak_heartrate')
    template_name = "hoosworkinout/cardio_form.html"

    def get_form(self, *args, **kwargs):
        form = super(CardioHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')

class CreateStrengthExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('wid', 'comment', 'name')

    def get_form(self, *args, **kwargs):
        form = super(CreateStrengthExerciseView, self).get_form(*args, **kwargs)
        form.fields['wid'].queryset = Workout.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('strength')

class StrengthHelper(LoginRequiredMixin, CreateView):
    model = Strength
    fields = ('eid', 'weight', 'category', 'sets')
    template_name = "hoosworkinout/strength_form.html"

    def get_form(self, *args, **kwargs):
        form = super(StrengthHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('reps')

class AddRepsView(LoginRequiredMixin, CreateView):
    model = Reps
    fields = ('eid', 'numbers')
    template_name = "hoosworkinout/reps_form.html"

    def get_form(self, *args, **kwargs):
        form = super(AddRepsView, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')


class CreateHIITExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('wid', 'name', 'comment')

    def get_form(self, *args, **kwargs):
        form = super(CreateHIITExerciseView, self).get_form(*args, **kwargs)
        form.fields['wid'].queryset = Workout.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('hiit')

class HIITHelper(LoginRequiredMixin, CreateView):
    model = Hiit
    fields = ('eid', 'distance', 'calories_burned', 'peak_heartrate', 'rest_interval', 'work_interval')
    template_name = "hoosworkinout/hiit_form.html"

    def get_form(self, *args, **kwargs):
        form = super(HIITHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')


class CreatePlanView(LoginRequiredMixin, CreateView):
    model = Plan
    fields = ['name', 'description']

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')

def export1(self):
    if self.method == "GET":
        workouts = Workout.objects.filter(user = self.request.user.id)
        workout_list = serializers.serialize('json', workouts)
        return HttpResponse(workout_list, content_type="text/json-comment-filtered")

def export2(self):
    Workout = Workout.objects.filter(user=self.request.user.id)
    dataset = Workout.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response
