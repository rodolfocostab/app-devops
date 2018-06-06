from tastypie.utils.timezone import now
from django.contrib.auth.models import Name
from django.db import models


class Post(models.Model):
    name = models.ForeignKey(Name)
    date_created = models.DateTimeField(default=now)
    status = models.CharField(max_length=200)
