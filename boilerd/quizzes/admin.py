from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('teamNumber', 'title', 'subtitle')

# from django.contrib import admin

# from .forms import QuizForm

# class QuizAdmin(admin.ModelAdmin):
#     form = QuizForm

#     # Define how to save, add views, etc., using the form to interact with MongoDB.

# admin.site.register(QuizAdmin)
