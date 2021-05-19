from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Tweet
from .forms import PhotoForm
# Create your views here.


def home(request):
    tweets = Tweet.objects.order_by('created_at').reverse().all()[:5]
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('body') and request.POST.get('image'):
            post = Tweet()
            post.name = request.POST.get('name')
            post.body = request.POST.get('body')
            post.image = request.POST.get('image')
            post.created_at = request.POST.get('created_datetime')
            post.save()
    return render(request, 'blog/twitter.html', {'tweets': tweets})


def tweetEdit(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    # context = {}
    return render(request, 'blog/tweetEdit.html')

def tweetDelete(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    tweets.delete()
    return HttpResponseRedirect('/home')

# def tweetLike(request):
    # return redirect({'tweets': tweets})
