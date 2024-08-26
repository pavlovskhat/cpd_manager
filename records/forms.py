"""
Forms related to record management.
"""
from django import forms
from records.models import Record


class CreateRecordForm(forms.ModelForm):
    """
    Form to create new academic training record.
    User(fk) -> Record .
    """
    class Meta:
        model = Record
        exclude = ["user"]
        labels = {
            "institution": "Where did you complete the training/course?",
            "course": "Training/Course Name",
            "completion_date": "Date Completed",
            "certification": "Certificate/Diploma PDF"
        }
        widgets = {
            "completion_date": forms.DateInput(attrs={"type": "date"}),
        }


class SearchRecordForm(forms.ModelForm):
    query = forms.CharField(
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )

    class Meta:
        model = Record
        fields = []
