from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from notyourmotleycrew.settings import MEDIA_URL

STATUS_CHOICES = (
        ('NOTCHECKED', 'Not checked yet'),
        ('BANNED', 'Banned'),
        ('APPROVED', 'Approved'),
        )

class NYMCImage(models.Model):
    caption = models.CharField(max_length=500)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NOTCHECKED')
    timestamp = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%y%m%d_%H%M") 

    def get_absolute_url(self):
        return MEDIA_URL + self.image.name
