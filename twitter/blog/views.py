from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tweet
# Create your views here.


def home(request):
    tweets = Tweet.objects.all()
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('body') and request.POST.get('image'):
            post = Tweet()
            post.name = request.POST.get('name')
            post.body = request.POST.get('body')
            post.image = request.POST.get('image')
            post.created_at = request.POST.get('created_datetime')
            post.save()
    return render(request, 'blog/twitter.html', {'tweets': tweets})


def tweetEdit(request):
    context = {}
    return render(request, 'blog/tweetEdit.html', context=context)


def tweetDelete(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    tweets.delete()
    return render(request, 'blog/twitter.html')
