from notyourmotleycrew.content.models import NYMCImage
def run():
    images = NYMCImage.objects.all()
    for image in images:
        image.scale_images()

