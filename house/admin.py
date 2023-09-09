from django.contrib import admin
from house.models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_on', )
