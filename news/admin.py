from django.contrib import admin
from news.models import New

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'text')

admin.site.register(New, NewAdmin)

