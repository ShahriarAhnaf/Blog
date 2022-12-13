"""
We need to map the URL for the views we made above. When a user makes a request for a page on your web app, 
the Django controller takes over to look for the corresponding view via the urls.py file, 
and then return the HTML response or a 404 not found error, if not found.
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
