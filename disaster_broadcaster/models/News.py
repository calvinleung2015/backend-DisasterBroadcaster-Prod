from disaster_broadcaster.filepaths.FilePath import FilePath
from disaster_broadcaster.models.Disaster import Disaster
from disaster_broadcaster.models.Country import Country
from django.db import models

class News(models.Model):
  country_id = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
  disaster_id = models.ForeignKey(Disaster, on_delete=models.CASCADE, blank=True, null=True)
  url = models.URLField()
  date_created = models.DateTimeField(null=True)
  date_added = models.DateTimeField(auto_now_add=True, null=True)
  headline = models.CharField(max_length=500)
  content = models.TextField()
  media = models.ImageField(upload_to=FilePath.news_upload, null=True)
