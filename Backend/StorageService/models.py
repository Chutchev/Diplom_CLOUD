from django.db import models
from LoginService.models import Profile


# Create your models here.
class File(models.Model):
    md5_hash = models.TextField()
    title = models.TextField()
    fullpath = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='files')
    url = models.TextField()
    file = models.FileField(default=True)

    def __str__(self):
        return self.title

