from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('teamNumber', 'title', 'subtitle')
