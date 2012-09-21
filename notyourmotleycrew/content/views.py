# Create your views here.


from django.template import Context

from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from notyourmotleycrew.content.forms import ImageForm
from notyourmotleycrew.content.forms import SignForm
from notyourmotleycrew.content.models import NYMCImage
from notyourmotleycrew.content.models import Sign
from notyourmotleycrew.content.models import image_file_name
from notyourmotleycrew.content.models import BANNED
from notyourmotleycrew.settings import MEDIA_ROOT
from os import makedirs
from os.path import dirname
from os.path import exists
from os.path import join
from subprocess import PIPE
from subprocess import Popen
from django.shortcuts import redirect
#import datetime

def thanks(reques):
    return render_to_response("thanks.html")

def sign(request, **kwargs):

    #If it's a post we're 
    #import pdb; pdb.set_trace()
    if request.method == 'POST': # If the form has been submitted...
        print request
        sign_form = SignForm(request.POST)
        if sign_form.is_valid():
            newsign = Sign()
            newsign.text = sign_form.data["text"]
            newsign.save()
            return redirect("/sign/%s" %(newsign.pk,))
    else:
        
        sign  = Sign.objects.get(id=int(kwargs['id']))
        
        #these heuristics where tested agains goole-chrome on linux

        font_size = int(118.0 - 0.37*len(sign.text))
        return render_to_response("sign.html", {'sign':sign, 'font_size':font_size})

def sign_pdf(request, **kwargs):
    template = get_template("sign.html")
    sign  = Sign.objects.get(id=int(kwargs['id']))
    
    renderedhtml = template.render(Context({'sign':sign}))

    process = Popen(["/usr/bin/wkhtmltopdf-i386 - - ",], shell=True, stdout=PIPE, stdin=PIPE)
    pdf = process.communicate(renderedhtml.encode("utf-8"))[0]
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=print_me.pdf'
    #pdfoutput = pdf.read()

    #print pdfoutput
    response.write(pdf)
    return response

def single_image(request, **kwargs):
    image = NYMCImage.objects.get(id=int(kwargs['id']))
    return render_to_response("single_image.html", {'image':image})

def home(request):
    template = "home.html"
    images = NYMCImage.objects.exclude(status=BANNED).exclude(image800="").order_by('-timestamp')
    return render_to_response(template, {'images':images})

def about(request):
    template = "about.html"
    return render_to_response(template, {})

#def contribute(request):
    #template = "contribute.html"
    #return render_to_response(template, {})

def handle_file_upload(form, f):

    #make a new image
    newimage = NYMCImage()

    #get the filename
    fn = image_file_name(f, f.name)
    fullpath = join(MEDIA_ROOT, fn)
    path = dirname(fullpath)

    #make sure that path is in place
    if not exists(path):
        makedirs(path)

    #write the file
    outputfile = open(fullpath, 'wb+')
    for chunk in f.chunks():
        outputfile.write(chunk)
    outputfile.close()   
    
    newimage.image = fn
    newimage.caption = form.data["caption"]
    newimage.save()

    #import pdb; pdb.set_trace() 


def contribute(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ImageForm(request.POST, request.FILES) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            handle_file_upload(form, request.FILES['image'])
        
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ImageForm() # An unbound form
        sign_form = SignForm()
        
    signs  = Sign.objects.filter(authorized=True)
    #return render_to_response(request, 'contribute.html', { 'form': form, }, context_instance=RequestContext(request))
    return render_to_response('contribute.html', { 'form': form, 'signs' : signs, 'sign_form':sign_form }, context_instance=RequestContext(request))
