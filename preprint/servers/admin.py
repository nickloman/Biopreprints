
from django.contrib import admin
from preprint.servers.models import PreprintServer, Field

class FieldAdmin(admin.ModelAdmin):
    pass
admin.site.register(Field, FieldAdmin)

class PreprintServerAdmin(admin.ModelAdmin):
    pass
admin.site.register(PreprintServer, PreprintServerAdmin)

