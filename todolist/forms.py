from django import forms

class FormForTask(forms.Form):
    title = forms.CharField(label='Judul Task', max_length=100)
    description = forms.CharField(label='Deskripsi Task', max_length=200)
