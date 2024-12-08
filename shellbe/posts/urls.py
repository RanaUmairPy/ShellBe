from django.urls import path
from posts.views import createposts_view
urlpatterns = [
    path('addpost/',createposts_view)
]
