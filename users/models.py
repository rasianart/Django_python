from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=256, blank=False, null=False)

    title = models.CharField(max_length=256, blank=False, null=False)

    language = models.CharField(max_length=256, blank=False, null=False)

    snippet = models.CharField(max_length=1000, blank=False, null=False)

    description = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        """ Sensible string representation of a user."""
        return "{0} {1} | {2}".format(self.name, self.title,
                self.description)
