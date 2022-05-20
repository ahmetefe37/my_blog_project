# ready modules
from django.urls import URLPattern, path,include

# my modules
from base.views import *

urlpatterns = [
    path("",homepage,name="home_url"),
    path("create/",createpage,name="create_url"),
    path("update/",updatepage,name="update_url"),
    path("delete/",deletepage,name="delete_url"),
    # path("detail/<str:pk_post>",detailpage,name="detail_url"),

    path("detail/<str:pk_post>",detailpage,name="detail_url"),
]