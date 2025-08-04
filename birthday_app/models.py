from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Timer(models.Model):
    release_time = models.DateTimeField()
    paragraph_text = models.TextField()
    letter_text = models.TextField()
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def clean(self):
        if Timer.objects.exists() and not self.pk:
            raise ValidationError("Only one Timer instance is allowed.")
