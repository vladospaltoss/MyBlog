from django.db import models

# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
