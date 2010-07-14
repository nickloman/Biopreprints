
from django.contrib import admin
from preprint.faq.models import FAQEntry

class FAQEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(FAQEntry, FAQEntryAdmin)

