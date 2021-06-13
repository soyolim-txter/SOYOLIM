from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # https: // wayhome25.github.io / django / 2017 / 05 / 06 / django - form /
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable text-left',
                                                           'style':'height:auto; text-align:left'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']