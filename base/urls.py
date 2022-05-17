# ready modules
from django.urls import URLPattern, path,include

# my modules
from base.views import *

urlpatterns = [
    path("",homepage,name="home_url")
]