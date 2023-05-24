from django.db import models
from django.conf import settings
# Create your models here.


class TODO(models.Model):
  title = models.CharField(max_length=64, null=False)
  is_complete = models.BooleanField(default=False)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="todo",
    null=True,
    blank=True,
  )
  created_At = models.TimeField(auto_now_add=True)
  updated_at = models.TimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.first_name} - {self.title}'