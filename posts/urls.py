from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),  # '' --> signifies that it is the root page of the website; views.index--> signifies that when the user is at this patthh it needs to look into the views folder with index function
    path('post/<str:pk>', views.post, name = 'post')
]
