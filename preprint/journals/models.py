from django.db import models

class Journal(models.Model):
    policy_choices = (
        ('OK', 'No restrictions'),
        ('MAYBE', 'Some caveats apply - see notes'),
        ('PROBNOT', 'Discouraged - see notes'),
        ('NO', 'Specifically disallowed'),
    )

    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    preprint_policy = models.CharField(choices=policy_choices, max_length=10)
    notes = models.TextField()

    def __unicode__(self):
        return self.name


