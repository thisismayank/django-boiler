from djongo import models

class Quiz(models.Model):
    teamNumber = models.CharField(max_length=255, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'quiz'  # This is optional but specifies the collection name in MongoDB

    def __str__(self):
        return self.title
