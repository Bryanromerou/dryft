from django import forms
from .models import Profile , Post , City

class ProfileForm(forms.ModelForm):
    current_city = forms.ModelChoiceField(queryset=City.objects.all())
    class Meta:      
        model = Profile
        fields = ("name","profile_picture","current_city")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","content","date","city","image",)