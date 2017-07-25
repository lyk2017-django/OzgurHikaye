from django.db import models

# Create your models here.
class Storys(models.Model):
    storyTitle_ = models.CharField(max_length=200)
    createTime_ = models.DateField(auto_now_add=True)


class Contributions(models.Model):
    storyId_ = models.ManyToManyField("Storys")
    contributionText_ = models.TextField()
    createTime_ = models.DateField(auto_now_add=True)