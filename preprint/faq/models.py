from django.db import models

class FAQEntry(models.Model):
    q = models.TextField()
    a = models.TextField()

    def __unicode__(self):
        return self.q
