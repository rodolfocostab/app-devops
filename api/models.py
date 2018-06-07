from django.db import models


class Post(models.Model):
    component_name = models.CharField(max_length=200)
    inicio_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.inicio_date >= timezone.now() - datetime.timedelta(days=1)
