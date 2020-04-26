from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from .models import Workout, Profile, User, Exercise, Cardio, Strength, Hiit
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/home.html'

'''
ListView creates a list called "object_list" that is available in the HTML.
All you have to have to do is loop through the object_list and display
the items you want. (Make sure to validate them with the current logged in user)
'''

class HomeListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'hoosworkinout/home.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/profile.html'

class CreateUserView(LoginRequiredMixin, CreateView):
    model =  User
    fields = ('first_name', 'last_name', 'email')

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['birthday', 'body_weight', 'best_lift']
    template_name = 'hoosworkinout/user_form.html'

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.filter(username=self.request.user.username)[0]  # use your own profile here
        candidate.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home');

class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ('comment', 'name', 'date')

    #This function automatically associates the new workout with the logged user.
    def form_valid(self, form):
       candidate = form.save(commit=False)
       candidate.user = User.objects.filter(username=self.request.user.username)[0]
       print(self.request.user.username)
       candidate.save()
       return redirect(self.get_success_url())

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
