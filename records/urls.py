"""
URL patterns dispatcher related to
user management.

index: Lists your records.
all_records: Lists all records.
records: Record detailed view.
create: Create new record.
update: Update existing record.
delete: Delete record.
"""
from django.urls import path
from . import views

app_name = "records"
urlpatterns = [
    path("", views.ViewYourRecords.as_view(), name="index"),
    path("all_records/", views.ViewAllRecords.as_view(), name="all_records"),
    path("record/<int:pk>/", views.ViewRecord.as_view(), name="record"),
    path("record/create/", views.CreateRecord.as_view(), name="create"),
    path("record/update/<int:pk>/", views.UpdateRecord.as_view(), name="update"),
    path("record/delete/<int:pk>/", views.DeleteRecord.as_view(), name="delete"),
]
