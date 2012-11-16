# Create your views here.
#import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from notyourmotleycrew.content.forms import ImageForm
from notyourmotleycrew.content.forms import SignForm
from notyourmotleycrew.content.models import APPROVED
from notyourmotleycrew.content.models import BANNED
from notyourmotleycrew.content.models import NYMCImage
from notyourmotleycrew.content.models import Post
from notyourmotleycrew.content.models import Sign
from notyourmotleycrew.content.models import image_file_name
from notyourmotleycrew.settings import MEDIA_ROOT
from notyourmotleycrew.timelinejs.models import Timeline
from os import makedirs
from os.path import dirname
from os.path import exists
from os.path import join
from subprocess import PIPE
from subprocess import Popen

def thanks(reques):
    return render_to_response("thanks.html")

def sign(request, **kwargs):

    #If it's a post we're 
    #import pdb; pdb.set_trace()
    if request.method == 'POST': # If the form has been submitted...
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

def intervention(request, **kwargs):
    post = Post.objects.get(slug = kwargs['slug'])
    template = "post.html"
    return render_to_response(template, {'post': post})

def interventions(request):
    posts = Post.objects.all().order_by("-timestamp")
    template = "posts.html"
    
    return render_to_response(template, {'posts': posts})

def home(request):
    template = "home.html"
    images = NYMCImage.objects.filter(status=APPROVED).exclude(image800="").order_by('-timestamp')

 
    result = []
    for image in images:
        result.append(image)
    julian = result.pop()
    result.insert(0,julian)
    images = result

    paginator = Paginator(images, 5) # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        images_on_page  = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images_on_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images_on_page = paginator.page(paginator.num_pages)

    #return render_to_response(template, {'images':images})
    return render_to_response(template, {'images': images_on_page})

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
    print form.data["email"]
    newimage.email = form.data["email"]
    newimage.save()

    #import pdb; pdb.set_trace() 

def timeline_data(request):

    timeline = Timeline.objects.all()[0]
    json = timeline.get_json()
    return HttpResponse(json, mimetype='application/json')

def get_md(templatename):
    template = get_template(templatename)
    return template.render(Context())

def thedebate(request):
    return render_to_response('thedebate.html', {})

def english_summary_of_the_swedish_debate(request):
    #instead of getting the md ourselves let's have django do it
    md = get_md("markdown/english_summary_of_the_swedish_debate.md")
    return render_to_response("markdown_base.html", {'md':md})

def contribute(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ImageForm(request.POST, request.FILES) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            handle_file_upload(form, request.FILES['image'])
        
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ImageForm() # An unbound form
        
    signs  = Sign.objects.filter(authorized=True)
    #return render_to_response('contribute.html', { 'form': form, 'signs' : signs, 'sign_form':sign_form }, context_instance=RequestContext(request))
    return render_to_response('contribute.html', { 'form': form, 'signs' : signs, }, context_instance=RequestContext(request))
