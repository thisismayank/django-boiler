from django import forms
from pymongo import MongoClient

class QuizForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, required=False)

    def save(self, *args, **kwargs):
        client = MongoClient('mongodb+srv://mayankar:TUxd6hA8KnW9xxAU@cluster0.7mktfiw.mongodb.net/sem-carbon-dev')
        db = client.your_db_name
        quizzes = db.quizzes
        quiz_data = {
            'title': self.cleaned_data['title'],
            'description': self.cleaned_data['description'],
        }
        if '_id' in kwargs:
            quizzes.update_one({'_id': kwargs['_id']}, {'$set': quiz_data})
        else:
            quizzes.insert_one(quiz_data)
