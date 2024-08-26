"""
Views related to record management.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from records.models import Record
from records.forms import CreateRecordForm, SearchRecordForm
from django.contrib.auth.models import User


class ViewYourRecords(LoginRequiredMixin, ListView):
    template_name = "records/view_records.html"
    model = Record
    form_class = SearchRecordForm
    context_object_name = "records"

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = super().get_queryset().filter(user_id=user_id)
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get("query")
            if query:
                queryset = queryset.filter(
                    Q(institution__icontains=query) |
                    Q(course__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_view"] = False
        context["fields"] = [
            field.name for field in (Record._meta.get_fields())[1:-1]
        ]
        context["form"] = self.form_class(self.request.GET)
        return context


class ViewAllRecords(LoginRequiredMixin, ListView):
    template_name = "records/view_records.html"
    model = Record
    context_object_name = "records"
    form_class = SearchRecordForm

    def get_queryset(self):
        queryset = self.model.objects.select_related("user")
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get("query")
            if query:
                queryset = queryset.filter(
                    Q(institution__icontains=query) |
                    Q(course__icontains=query) |
                    Q(user__username__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_view"] = True
        context["fields"] = [
            field.name for field in (Record._meta.get_fields())[1:-1]
        ]
        context["fields"].insert(0, "employee")
        context["form"] = self.form_class(self.request.GET)
        return context


class ViewRecord(LoginRequiredMixin, DetailView):
    """
    View a specific record inheriting from
    the DetailView class.
    Redirects to the index page.
    """
    template_name = "records/view_record.html"
    model = Record
    context_object_name = "record"

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        context = super().get_context_data(**kwargs)
        context["username"] = user.username
        print(self.model.certification)
        return context


class CreateRecord(LoginRequiredMixin, CreateView):
    """
    Create a new academic record in the database
    inheriting from the CreatView class.
    Redirects to the index page.
    """
    model = Record
    form_class = CreateRecordForm
    template_name = "records/create_record.html"
    success_url = reverse_lazy("records:index")

    def form_valid(self, form):
        """
        Validates the form data.
        :param form: Create record form.
        :return: Redirect to index page.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateRecord(LoginRequiredMixin, UpdateView):
    """
    Update existing database records inheriting
    from the UpdateView class.
    Redirects to the index page.
    """
    template_name = "records/create_record.html"
    model = Record
    form_class = CreateRecordForm
    success_url = reverse_lazy("records:index")


class DeleteRecord(LoginRequiredMixin, DeleteView):
    """
    Delete existing database records inheriting
    from the DeleteView class.
    Redirects to the index page.
    """
    template_name = "records/delete_record.html"
    model = Record
    success_url = reverse_lazy("records:index")
    context_object_name = "record"
