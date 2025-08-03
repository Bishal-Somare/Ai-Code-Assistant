from django import forms


class ProblemForm(forms.Form):
    problem = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Ask your problem'}))