from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import registor
urlpatterns = [
    path('registor/',registor)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)