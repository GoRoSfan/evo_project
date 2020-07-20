import os

from django.db import models

from evo_project import settings


# Create your models here.


class TempFile(models.Model):
    file = models.FileField('temporary file', upload_to='', )
    life_time = models.DurationField('life time', )
    upload_time = models.DateTimeField(auto_now_add=True, )

    class Meta:
        verbose_name = 'Temporary file'
        verbose_name_plural = 'Temporary files'

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))

        super(TempFile, self).delete(*args, **kwargs)

    def __str__(self):
        return self.file.name
