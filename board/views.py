from django.shortcuts import render
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Post, PostForm, Emergency, Information
from django.contrib.auth import logout
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

ROOT_URL = env('ROOT_URL')

def index(request):
    post_list = Post.objects.order_by('-date_created')[:10]
    post_list_all = Post.objects.order_by('-date_created')
    emergency = Emergency.objects.order_by('-date_created')[0]   # this will find the most recent iteration of the emergency msg
    infotext = Information.objects.order_by('-date_modified')[0] # again, this will find the most recent iteration of infotext. Not really neccessary since we aren't iterating over the db anyway, but still a safe-to-have. [0] doesn't work since Emergency object is not iterable.
    url = ROOT_URL
    template = loader.get_template('board/index.html')
    context = {
        'url': url if request.user.is_authenticated else [],
        'post_list': post_list if request.user.is_authenticated else [],
        'infotext': infotext if request.user.is_authenticated else [],
        'emergency': emergency if request.user.is_authenticated else [],
    }
    return render(request, 'board/index.html', context)

def all(request):
    post_list_all = Post.objects.order_by('-date_created')
    emergency = Emergency.objects.order_by('-date_created')[0]
    template = loader.get_template('board/all.html')
    url = ROOT_URL
    context = {
        'url': url if request.user.is_authenticated else [],
        'post_list_all': post_list_all if request.user.is_authenticated else [],
        'emergency': emergency if request.user.is_authenticated else [],
    }
    return render(request, 'board/all.html', context)

def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404(NOT_FOUND_ERROR)
    url = ROOT_URL
    template = loader.get_template('board/post.html')
    emergency = Emergency.objects.order_by('-date_created')[0]
    context = {
        'post': post if request.user.is_authenticated else [],
        'url': url if request.user.is_authenticated else [],
        'emergency': emergency if request.user.is_authenticated else [],
    }
    return render(request, 'board/post.html', context)

def manage(request):
    url = ROOT_URL
    infotext = Information.objects.order_by('-date_modified')[:1]
    emergency = Emergency.objects.order_by('-date_created')[0]
    template = loader.get_template('board/manage.html')
    context = {
        'url': url if request.user.is_authenticated else [],
        'infotext': infotext if request.user.is_authenticated else [],
        'emergency': emergency if request.user.is_authenticated else [],
    }
    return render(request, 'board/manage.html', context)

def push(request):                          # https://docs.djangoproject.com/en/3.1/topics/forms/#the-view
    if request.method == 'POST':            # test whether this is a POST method request => process form data
        form = PostForm(request.POST)       # create form instance => populate with form data
        if form.is_valid():                 # validation
            p = form.save()
            p.content = form.cleaned_data['content']
            p.save()
            return HttpResponseRedirect('/manage/push/pipeline/')
    else: # if its a GET method then we create a blank form
        form = PostForm()
    context = {
        'form': form if request.user.is_authenticated else [],
    }
    return render(request, 'board/push.html', context)

def pipeline(request):
    post = Post.objects.order_by('-date_created')[0]
    context = {
        'post': post if request.user.is_authenticated else [],
    }
    return render(request, 'board/pipeline.html', context)

def logoutUser(request):
    logout(request)
    context = {}
    return render(request, 'board/logout.html', context)


def pipeline(request):
    post = Post.objects.order_by('-date_created')[0]
    context = {
        'post': post if request.user.is_authenticated else [],
    }
    return render(request, 'board/pipeline.html', context)