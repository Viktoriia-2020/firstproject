from django.contrib import admin


# Register your models here.
from property.models import Property


class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'price')
    list_display_links = ('title', )
    list_editable = ('price', )
    list_filter = ('update', 'timestamp')


admin.site.register(Property, PropertyModelAdmin)