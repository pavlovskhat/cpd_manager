"""
Record management models.

Record: Academic upskilling model.
"""
from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    """
    Model representing academic upskilling
    records.

    :param: institution: Where upskilling was completed.
    :param: course: Subject of upskilling.
    :param: completion_date: Date of completion.
    :param: certification: Record of upskilling.
    :param: user: Record owner.
    """
    institution = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    completion_date = models.DateField()
    certification = models.FileField(upload_to="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_upload_path(self, file_name):
        """
        Constructs file upload path.

        :param: file_name: File name.
        :return: File upload path string.
        """
        return f"user_{self.user.username}/{file_name}"

    def save(self, *args, **kwargs):
        """
        Saves files with validated paths or
        requests a valid path.
        """
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
