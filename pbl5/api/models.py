from django.db import models

# Create your models here.
class hr(models.Model):
  id = models.IntegerField(primary_key=True)
  value = models.FloatField()
  date_posting = models.DateField(max_length=255)
  def __str__(self):
    return str(self.value)