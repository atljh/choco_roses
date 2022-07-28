from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Client
from .forms import CreateClientForm, UpdateClientForm
from django.contrib import messages



class HomeView(ListView):
    model = Client
    template_name = "index.html"


class SearchResultsView(ListView):
    template_name = "search_results.html"
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            results = Client.objects.filter(
                Q(name__icontains=query)
                | Q(pk__icontains=query)
                | Q(phone__icontains=query)
                | Q(address__icontains=query)
                | Q(email__icontains=query)
            )
            return results


class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    template_name = "create_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client created.")
        return reverse("crm:detail-client", args=[self.object.id])


class DetailClientView(DetailView):
    model = Client
    template_name = "detail_client.html"


class UpdateClientView(UpdateView):
    model = Client
    form_class = UpdateClientForm
    template_name = "update_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client updated.")
        return reverse("crm:detail-client", args=[self.object.id])


class DeleteClientView(DeleteView):
    model = Client
    template_name = "delete_client.html"

    def get_success_url(self):
        messages.success(self.request, "Client deleted.")
        return reverse("crm:index")