from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path("", views.home, name="home"),
    path('details/<statename>', views.details, name='details'),
    path("state/create", views.StateCreateView.as_view(), name="statecreate"),
    path("attraction/create", views.AttractionCreateView.as_view(), name="attractioncreate"),
]