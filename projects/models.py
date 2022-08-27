from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    learn_description = models.TextField(null=True, blank=True)
    stack = models.TextField(null=True, blank=True)
    source_link = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
