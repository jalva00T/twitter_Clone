from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweetEdit/<int:tweet_id>', views.tweetEdit, name='tweetEdit'),
    path('tweetDelete/<int:tweet_id>', views.tweetDelete, name='tweetDelete'),
    path('tweetLike/<int:tweet_id>', views.tweetLike, name='tweetLike'),
    path('tweetLikeSubtract/<int:tweet_id>', views.tweetLikeSubtract, name='likeSubtract')
]

