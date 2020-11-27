from disaster_broadcaster.filepaths.FilePath import FilePath
from disaster_broadcaster.models.User import User
from disaster_broadcaster.models.Country import Country
from django.db import models

class Post(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
  content = models.CharField(max_length=1024, blank=True, default=None)
  media = models.FileField(upload_to=FilePath.post_upload, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
