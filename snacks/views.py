from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class SnackListView(TemplateView):
    template_name = "snack-list.html"
    model = Snack


class SnackDetailView(TemplateView):
    template_name = "snack-detail.html"
    model = Snack


class SnackCreateView(TemplateView):
    template_name = "snack-create.html"
    model = Snack


class SnackUpdateView(TemplateView):
    template_name = "snack-update.html"
    model = Snack


class SnackDeleteView(TemplateView):
    template_name = "snack-delete.html"
    model = Snack
