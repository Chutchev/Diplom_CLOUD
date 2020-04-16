from django.db import models
from LoginService.models import Profile


# Create your models here.
class File(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(default='None', upload_to='files')

    def __str__(self):
        return self.file.name

