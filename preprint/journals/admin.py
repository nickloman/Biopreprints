
from django.contrib import admin
from preprint.journals.models import Journal

class JournalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Journal, JournalAdmin)

