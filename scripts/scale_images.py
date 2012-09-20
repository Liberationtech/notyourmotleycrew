from notyourmotleycrew.content.models import NYMCImage
def run():
    images = NYMCImage.objects.all()
    for image in images:
        print "-"*100
        image.scale_images()

