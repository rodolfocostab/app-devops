from django.db import models
from tastypie.utils.timezone import now


class Inicio(models.Model):
    component_name = models.CharField(max_length=200)
    inicio_date = models.DateTimeField(default=now)
    def was_published_recently(self):
        return self.inicio_date >= timezone.now() - datetime.timedelta(days=1)
