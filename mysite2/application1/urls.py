from django.urls import path 
from . import views


urlpatterns = [
    path("welcome/", views.welcome)
]
urlpatterns2 = [
    path("about/", views.welcome)
]
urlpatterns3 = [ 
     path("contacts/", views.welcome)
]

urlpatterns4 = [ 
     path("projects/", views.welcome)
]


urlpatterns5 = [ 
     path("shop/", views.welcome)
]
