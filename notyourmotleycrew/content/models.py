from django.db import models

from os.path import exists
# Create your models here.
from os.path import dirname
from os.path import basename
from django.db import models
from datetime import datetime
from notyourmotleycrew.settings import MEDIA_URL
from notyourmotleycrew.settings import MEDIA_ROOT
import string
import random
from os.path import join
from os import makedirs

NOTCHECKED = 'NOTCHECKED'
BANNED = 'BANNED'
APPROVED = 'APPROVED'

STATUS_CHOICES = (
        (NOTCHECKED, 'Not checked yet'),
        (BANNED, 'Banned'),
        (APPROVED, 'Approved'),
        )

def image_file_name(instance, originalfilename):
    datestr = datetime.now().strftime("%y%m%d_%H%M")
    fn = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
    extension = originalfilename.split('.')[-1]
    
    return join("images", datestr, fn + '.' + extension)

class NYMCImage(models.Model):
    caption = models.CharField(max_length=500)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NOTCHECKED')
    timestamp = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to=image_file_name)
    image200 = models.ImageField(upload_to=image_file_name, null=True)
    image400 = models.ImageField(upload_to=image_file_name, null=True)
    image600 = models.ImageField(upload_to=image_file_name, null=True)
    image800 = models.ImageField(upload_to=image_file_name, null=True)
    image1000 = models.ImageField(upload_to=image_file_name, null=True)

    def get_file_name_for_resolution(self, resolution):
        path = dirname(self.image.name)
        base = basename(self.image.name)
        return join(path, str(resolution), base)

    def scale_image(self, target_image, resolution):
        #import Image
        from PIL import Image
        if not target_image:
            print "there is no ", resolution
            target_image.name = self.get_file_name_for_resolution(resolution)
            
            original = Image.open(self.image.path)
           
            orig_width, orig_height = original.size
            new_width = resolution
            new_height = int((1.0 * new_width * orig_height) / orig_width)
            size = (new_width, new_height)
            newimage = original.resize(size, Image.ANTIALIAS)
            path = dirname(target_image.path)
            if not exists(path):
                makedirs(path)

            newimage.save(target_image.path)
            print target_image.path
            print target_image.name
            self.save()

    def scale_images(self):
        
        
        self.scale_image(self.image200, 200)
        self.scale_image(self.image400, 400)
        self.scale_image(self.image600, 600)
        self.scale_image(self.image800, 800)
        self.scale_image(self.image1000, 1000)
    
    def get_absolute_url(self):
        result = "/single_image/%s" % (self.id,)
        print result
        return result
        #return MEDIA_URL + self.image.name

    def get_the_image_url(self):
        return MEDIA_URL + self.image.name

    def get_the_image_url_200(self):
        return MEDIA_URL + self.image200.name

    def get_the_image_url_400(self):
        return MEDIA_URL + self.image400.name

    def get_the_image_url_600(self):
        return MEDIA_URL + self.image600.name

    def get_the_image_url_800(self):
        return MEDIA_URL + self.image800.name

    def get_the_image_url_1000(self):
        return MEDIA_URL + self.image1000.name

class Sign(models.Model):
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(default=datetime.now)
    authorized = models.BooleanField(default=False)

    
