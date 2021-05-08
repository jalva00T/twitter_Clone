from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('tweetAdd/', views.home, name='tweetAdd'),
    path('tweetEdit/', views.tweetEdit, name='tweetEdit'),
    path('tweetDelete/<int:tweet_id>/', views.tweetDelete, name='tweetDelete')
]

