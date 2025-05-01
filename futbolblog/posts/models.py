from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('lpf', 'Liga Profesional'),
        ('pbn', 'Primera Nacional'),
        ('int', 'Internacional'),
        ('arg', 'Seleccion'),
        ('lib', 'Libertadores'),
        ('sud', 'Sudamericana'),
        ('mun', 'Mundial 2026'),
        ('muc', 'Mundial de Clubes'),
        ('other', 'Otros'),
    ]
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = RichTextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    def __str__(self):
        return self.title