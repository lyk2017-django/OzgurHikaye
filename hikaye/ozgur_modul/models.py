from django.db import models

# Create your models here.
class Storys(models.Model):
    story_title = models.CharField(max_length=200)
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "#{id} {text} ".format(id=self.id, text=self.story_title)


class Contributions(models.Model):
    story = models.ForeignKey("Storys")
    contribution_text = models.TextField()
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "#{id} {text} ".format(id=self.id, text=self.contribution_text)

