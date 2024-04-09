from django.db import models
from django_quill.fields import QuillField
from django.utils import timezone

# Create your models here.

class QuillPost(models.Model):
    title = models.CharField(null=True, max_length=150, unique=True)
    image_url = models.URLField(null=True)
    description = models.CharField(null=True, max_length=200, unique=True)
    content = QuillField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title