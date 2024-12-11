from django.urls import path
from post.views import createposts_view,post_display_view

urlpatterns = [
    path('createpost/',createposts_view,name="cpost"),
    path('postdisplay/',post_display_view,name="dpost")
]
