from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class PreprintServer(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    fields_covered = models.ManyToManyField(Field)
    notes = models.TextField()

    def __unicode__(self):
        return self.name

