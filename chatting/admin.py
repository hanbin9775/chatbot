from django.contrib import admin
from .models import chatting
# admin.site.register(chatting)

@admin.register(chatting)
class chattingAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat', 'pub_date']
    