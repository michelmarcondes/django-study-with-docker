from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        #fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    #override class constructor
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        #customizing field manual method
        # self.fields['title'].widget.attrs.update({'class':'input'})

        #customizing field dinamically
        for name, field in self.fields.items():
            field.widget.attrs. update({'class':'input'})
