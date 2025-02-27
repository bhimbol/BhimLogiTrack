from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    tag = models.CharField(max_length=20, default='other')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
