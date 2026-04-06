from django.db import models
from django.conf import settings
from courses.models import Course


class Assignment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUBMITTED = 'submitted', 'Submitted'
        GRADED = 'graded', 'Graded'

    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.title} ({self.course.code})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('assignments:detail', args=[self.pk])

# Create your models here.
