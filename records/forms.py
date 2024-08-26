"""
Record management forms.

CreateRecordForm: Create new record.
SearchRecordForm: Search for record.
"""
from django import forms
from records.models import Record


class CreateRecordForm(forms.ModelForm):
    """
    Form to create new academic training record.
    User(fk) -> Record .
    """
    class Meta:
        """
        Form presentation settings.
        """
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
    """
    Form to search for record.
    Dynamically searches based on text input.
    """
    query = forms.CharField(
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )

    class Meta:
        """
        Form presentation settings.
        """
        model = Record
        fields = []
