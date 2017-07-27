from django.db import models

# Create your models here.
class Storys(models.Model):
    """Hikayelerin başlıklarını ve diğer bilgilerini bu tabloda saklayacağız."""
    story_title = models.CharField(max_length=200)
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "#{id}-{text} ".format(id=self.id, text=self.story_title)

    class Meta:
        verbose_name="Başlık"
        verbose_name_plural = "Başlıklar"



class Contributions(models.Model):
    """Her bir hikayeye giriHikayelerin başlıklarını ve diğer bilgilerini bu tabloda saklayacağız."""
    story = models.ForeignKey("Storys")
    contribution_text = models.TextField()
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "#{id}-{text} ".format(id=self.id, text=self.contribution_text)

    class Meta:
        verbose_name="Katkı"
        verbose_name_plural = "Katkılar"

