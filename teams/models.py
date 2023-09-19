from django.db import models


class Team(models.Model):
    image = models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    google_plus_link = models.URLField(blank=True, null=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
