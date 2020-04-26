from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import Workout, Profile, User, Exercise, Cardio, Strength, Hiit
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/profile.html'

class CreateUserView(LoginRequiredMixin, CreateView):
    model =  User
    fields = ('first_name', 'last_name', 'email')

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['user', 'birthday', 'body_weight', 'best_lift']
    template_name = 'hoosworkinout/user_form.html'
    def get_success_url(self):
        return reverse('home');

class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ('comment', 'name', 'date')

    #This function automatically associates the new workout with the logged user.
    def form_valid(self, form):
       candidate = form.save(commit=False)
       candidate.user = User.objects.filter(username=self.request.user.username)[0]
       candidate.save()
       return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')


#Generic exercise view - not really used
class CreateExerciseView(CreateView):
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
to the second one to create the cardio, strenght, or hiit model.

The get_form() overrride allows you to filter the dropdowns for wid and eid in
those forms. Below, it is used to only show the workouts and exercises associated with
the username of the currently logged user.

The form_valid() override allows to automatically save the workout or exercise to
the currently logged user. This eliminates the need to select yourself from the
dropdown and improves security by making sure you can't select other users.


'''
class CreateCardioExerciseView(CreateView):
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

class CardioHelper(CreateView):
    model = Cardio
    fields = ('eid', 'duration', 'distance', 'calories_burned', 'peak_heartrate')
    template_name = "hoosworkinout/cardio_form.html"

    def get_form(self, *args, **kwargs):
        form = super(CardioHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')

class CreateStrengthExerciseView(CreateView):
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

class StrengthHelper(CreateView):
    model = Strength
    fields = ('eid', 'weight', 'category', 'sets')
    template_name = "hoosworkinout/strength_form.html"

    def get_form(self, *args, **kwargs):
        form = super(StrengthHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')

class CreateHIITExerciseView(CreateView):
    model = Exercise
    fields = ('wid', 'comment', 'name')

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

class HIITHelper(CreateView):
    model = Hiit
    fields = ('eid', 'distance', 'calories_burned', 'peak_heartrate', 'rest_interval', 'work_interval')
    template_name = "hoosworkinout/hiit_form.html"

    def get_form(self, *args, **kwargs):
        form = super(HIITHelper, self).get_form(*args, **kwargs)
        form.fields['eid'].queryset = Exercise.objects.filter(user_id = self.request.user.profile.user_id)
        return form

    def get_success_url(self):
        return reverse('home')


def load_profile_page(request, uname):
    current_user = User.objects.filter(username = uname)
    current_workouts = Workout.objects.filter(username=uname)
    allUsers = User.objects.all()
    context = {
        "current_user" : current_user,
        "current_workouts" : current_workouts,
        "allProfiles" : allUsers,
        }
    return render(request, 'hoosworkinout/home.html', context)

def authenticate(request):
#Check to see if this is a new user
#If it is, create a new user model and save it to the database
    get_email = request.user.email
    at_symbol_index = get_email.find('@')
    username = get_email[:at_symbol_index]

    initialized = False
    all_users = User.objects.all()

    for user in all_users:
        if user.username == username:
            initialized = True
    if initialized == False:

        new_user.save()

    return redirect('/load_profile_page/'+username)
