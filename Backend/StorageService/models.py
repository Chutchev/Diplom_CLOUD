from django.db import models
from LoginService.models import Profile


# Create your models here.
class File(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(default='None', upload_to='', )

    def __str__(self):
        return self.file.name

    @property
    def name(self):
        return str(self.file.name).split('/')[-1]

    @property
    def path(self):

        return self.file.storage

