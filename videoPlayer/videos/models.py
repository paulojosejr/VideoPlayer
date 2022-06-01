from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    arquivos_de_video = models.FileField(upload_to='uploads/arquivos_de_video', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    dataDePostagem = models.DateTimeField(default=timezone.now)