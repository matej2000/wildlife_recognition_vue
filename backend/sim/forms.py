from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def save(self, commit=True) -> User:
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
    
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    file = forms.FileField()