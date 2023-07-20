from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_text/<str:message>', views.get_text, name='get_text'),
]