from django.contrib import admin
from .models import Summarizer
# Register your models here.

@admin.register(Summarizer)
class SummarizerAdmin(admin.ModelAdmin):
    list_display = ['id', 'mytext', 'myword', 'summarize', 'sumword']
