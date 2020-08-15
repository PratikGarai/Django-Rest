#Django imports
from django.urls import path

#Rest Framework imports
from rest_framework.urlpatterns import format_suffix_patterns

#File imports
from . import views

app_name = 'SnippetApp'

urlpatterns = [
        # path('',views.snippet_list, name="Snippet-List"),
        # path('<int:pk>/', views.snippet_detail, name="Snippet-Detail"),
        path('',views.SnippetList.as_view(), name="SnippetList"),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
