"""
Forms related to user management.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):

    """
    A form that creates User class objects.
    username: Unique constraint, not null.
    email: Email constraint, not null.
    password1: Min 8 chars, unique.
    password2: Validate with password1.
    """
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "usable_password" in self.fields:
            del self.fields["usable_password"]
        self.fields["username"].label = "Username"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"
        self.fields["username"].widget.attrs = {"placeholder": "Username"}
        self.fields["password1"].widget.attrs = {"placeholder": "Password"}
        self.fields["password2"].widget.attrs = {"placeholder": "Password"}
        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
