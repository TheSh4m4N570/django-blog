from django.db import models


# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=150, default='About')
    about_text = models.TextField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.about_title


class SocialMedia(models.Model):
    social_platform = models.CharField(max_length=100, unique=True)
    social_link = models.URLField(unique=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.social_platform

