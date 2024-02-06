from django.urls import URLPattern, path
from . import views

urlpatterns = [path("", views.home_page, name="homepage")]
