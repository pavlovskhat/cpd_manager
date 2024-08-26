"""
User management views.

UserLoginView: User login.
UserRegistrationView: User registration.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegistrationForm


class UserLoginView(LoginView):
    """
    User login view.
    """
    def get_success_url(self):
        """
        Generates URL redirect.

        :return: Success URL pattern.
        """
        return reverse_lazy("records:index")

    def form_invalid(self, form):
        """
        Custom form validation.

        :param form: Login form.
        :return: context with updated error message.
        """
        form.add_error(None, "")
        form.errors.clear()
        messages.error(
            self.request,
            "Invalid username or password. Please try again."
        )
        return self.render_to_response(self.get_context_data(form=form))


class UserRegistrationView(CreateView):
    """
    User registration view.s
    """
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("records:index")

    def form_valid(self, form):
        """
        If the form data is validated:
        Writes User object to database.
        Logs the user in.
        Redirects to the records index page.
        :param form: User registration form.
        :return: Records index page.
        """
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
