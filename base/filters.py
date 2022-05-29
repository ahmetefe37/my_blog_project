from dataclasses import field
import django_filters
from django_filters import CharFilter

from .models import Post

class PostFilter(django_filters.FilterSet):
    searched_text = CharFilter(field_name="searched_text",lookup_expr="icontains")
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["status","date_created","date_updated","slug","image_post"]