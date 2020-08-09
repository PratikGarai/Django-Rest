from django.urls import path
from . import views

app_name = 'SnippetApp'

urlpatterns = [
        path('',views.snippet_list, name="Snippet-List"),
        path('<int:pk>/', views.snippet_detail, name="Snippet-Detail"),
        ]
