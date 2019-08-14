from django.urls import path
from .views import Search,start

urlpatterns = [
    path('', start.as_view(), name='start'),
    path('search/', Search.as_view(), name='search_result'),
]
