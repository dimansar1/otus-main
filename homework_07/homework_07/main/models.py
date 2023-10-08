from django.db import models

# Create your models here.
class Video(models.Model):
    # id = Column(Integer, primary_key=True)
    name = models.CharField(max_length = 100)
    link = models.TextField()
    watch = models.TextField(null = True)
