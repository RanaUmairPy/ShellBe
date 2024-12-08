from django.urls import path
from users.views import registor_view
urlpatterns = [
    path('registor/',registor_view)
]
