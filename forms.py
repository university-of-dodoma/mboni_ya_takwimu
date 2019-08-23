from django import forms
from .models import Dataset, Question, Post1

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class DatasetForm(forms.ModelForm):

    class Meta:
        model = Dataset
        fields = ('title','scope','cvs_filePath')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text','pub_date')

class Post1Form(forms.ModelForm):
    class Meta:
        model = Post1
        fields = ('question_text','pub_date','cvs_path')