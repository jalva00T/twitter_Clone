from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from .models import Tweet
from .forms import PhotoForm
from datetime import datetime
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.


def home(request):
    # If the method is POST
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/home')

        else:
            # No, show error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all the posts, limit = 8
    tweets = Tweet.objects.order_by('created_at').reverse().all()[:10]
    # tweet_paginator = Paginator(tweets, 4)
    # page = tweet_paginator.get_page(1)

    # Show
    return render(request, 'blog/twitter.html', {'tweets': tweets,})


# ///// EDIT /////


def tweetEdit(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    print(tweets)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=tweets)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    else:
        # Show editting screen
        form = PhotoForm
        return render(request, 'blog/tweetEdit.html',
                      {'tweet': tweets, 'form': form})


# ///// DELETE /////

def tweetDelete(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    tweets.delete()
    return HttpResponseRedirect('/home')


# ///// LIKES /////

def tweetLike(request, tweet_id):
  # Get requested tweet
    tweet = Tweet.objects.get(id=tweet_id)
  # Add count
    new_like_count = tweet.like_count + 1
    tweet.like_count = new_like_count
  # Save
    print(tweet.like_count)
    tweet.save()
    return HttpResponseRedirect('/home')

def tweetLikeSubtract(request, tweet_id):
  # Get requested tweet
    tweet = Tweet.objects.get(id=tweet_id)
  # Subtract count
    new_like_count = tweet.like_count - 1
    tweet.like_count = new_like_count
  # Save
    tweet.save()
    return HttpResponseRedirect('/home')