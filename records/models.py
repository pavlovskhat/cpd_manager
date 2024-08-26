"""
Database models related to upskilling records.
"""
from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    """
    Model representing user records.
    ==================================
    Attributes
    ==================================
    institution: Where upskilling was completed.
    course: Subject of upskilling.
    completion_date: Date of completion.
    certification: Record of upskilling.
    user: User who upskilled.
    """
    institution = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    completion_date = models.DateField()
    certification = models.FileField(upload_to="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_upload_path(self, file_name):
        return f"user_{self.user.username}/{file_name}"

    def save(self, *args, **kwargs):
        if not self.certification.name.startswith("user_"):
            self.certification.name = self.get_upload_path(
                self.certification.name
            )
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Console display string.
        :return: Object information string.
        """
        return f"{self.institution}, {self.course}, {self.completion_date}"
