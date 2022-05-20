# ready modules
from django.urls import URLPattern, path,include

# my modules
from base.views import *

app_name = 'post'

urlpatterns = [
    path("",homepage,name="home_url"),
    path("create/",createpage,name="create_url"),
    path("update/<str:pk_post_update>",updatepage,name="update_url"),
    path("delete/<str:pk_post_delete>",deletepage,name="delete_url"),
    path("detail/<str:pk_post_detail>",detailpage,name="detail_url"),
]