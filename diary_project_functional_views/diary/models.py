from django.db import models
from django.utils import timezone


class Day(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("タイトル", max_length=200)
    text = models.TextField("本文")
    date = models.DateTimeField("日付", default=timezone.now)
