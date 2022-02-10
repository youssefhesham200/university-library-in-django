from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import User, Student, Owner, FormBook
from django import forms


class StudentSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    phoneNumber = forms.CharField(required=True)
    identification = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True) :
        user = super(StudentSignUpForm, self).save(commit=False)
        user.is_student = True
        user.name = self.cleaned_data['name']
        user.phoneNumber = self.cleaned_data['phoneNumber']
        user.identification = self.cleaned_data['identification']
        if commit:
            user.save()
            student = Student.objects.create(user=user)
            student.save()
        return user


class OwnerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    phoneNumber = forms.CharField(required=True)
    identification = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super(OwnerSignUpForm, self).save(commit=False)
        user.is_owner = True
        user.is_staff = True
        user.name = self.cleaned_data['name']
        user.phoneNumber = self.cleaned_data[ 'phoneNumber' ]
        user.identification = self.cleaned_data['identification']
        if commit:
            user.save()
            owner = Owner.objects.create(user=user)
            owner.save()
        return user


class AddForm(forms.ModelForm):
    class Meta:
        model = FormBook
        fields = '__all__'
        widget = forms.TextInput(attrs={'placeholder': 'Enter your first name'})


class ChangeUser(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'username',
            'name',
            'phoneNumber',
            'identification',
        }


class Addextend(forms.ModelForm):
    class Meta:
        model = FormBook
        fields = {
            'returning',
        }