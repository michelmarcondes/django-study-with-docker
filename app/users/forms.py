from operator import contains
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

        print(self.fields.items())

        for name, field in self.fields.items():
            if str(name).find('password') > -1:
                field.widget.attrs.update({'placeholder': '••••••••'})

            field.widget.attrs.update({'class': 'input input--text'})
