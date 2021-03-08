from django.urls import path
from .views import *

urlpatterns = [
    path("", SnackListView.as_view(), name="list"),
    path("content/<int:pk>/", SnackDetailView.as_view(), name="detail"),
    path("content/new/", SnackCreateView.as_view(), name="new"),
    path("content/<int:pk>/edit/", SnackUpdateView.as_view(), name="update"),
    path("content/<int:pk>/delete/", SnackDeleteView.as_view(), name="delete"),
]
