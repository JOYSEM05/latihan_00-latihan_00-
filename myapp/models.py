from django.db import models

class StatusModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class JobTitle(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(
        StatusModel,
        related_name='job_titles',
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name  
