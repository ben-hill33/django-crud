from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Snack
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class SnackListView(ListView):
    template_name = "list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "new.html"
    model = Snack
    fields = ["name", "description", "purchaser"]


class SnackUpdateView(UpdateView):
    template_name = "update.html"
    model = Snack
    fields = ["name", "description"]


class SnackDeleteView(DeleteView):
    template_name = "delete.html"
    model = Snack
    success = reverse_lazy("list")
