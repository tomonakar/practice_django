from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day


class AddView(generic.CreateView):
    model = Day
    # fiels = '__all__'  # model = Day の代わりにこの書き方も可能. つまり CreateViewを使う場合は, forms.pyが無くても大丈夫.
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')  # /diary/


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day
