"""
User management forms.

UserRegistrationForm: User registration form.
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """
    User registration form.
    """
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        """
        Initializing custom form properties.
        """
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
