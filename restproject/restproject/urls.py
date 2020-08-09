from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippet/', include('snippets.urls'),name="SnippetApp")
]
