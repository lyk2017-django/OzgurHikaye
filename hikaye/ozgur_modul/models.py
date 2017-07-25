from django.db import models

# Create your models here.
class Storys(models.Model):
    story_title = models.CharField(max_length=200)
    create_time = models.DateField(auto_now_add=True)


class Contributions(models.Model):
    story_id = models.ForeignKey("Storys")
    contribution_text = models.TextField()
    create_time = models.DateField(auto_now_add=True)