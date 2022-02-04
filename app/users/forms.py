from operator import contains
from unittest import skip
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill

#this class inherit all from UserCreationForm class
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # print(self.fields.items())

        for name, field in self.fields.items():
            if str(name).find('password') > -1:
                field.widget.attrs.update({'placeholder': '••••••••'})

            field.widget.attrs.update({'class': 'input input--text'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email', 'username', 'location', 'bio', 
        'short_intro', 'profile_image', 'social_github', 'social_linkedin', 
        'social_twitter', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if str(name).find('password') > -1:
                field.widget.attrs.update({'placeholder': '••••••••'})

            field.widget.attrs.update({'class': 'input input--text'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})