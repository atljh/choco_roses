from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('client/create/', views.CreateClientView.as_view(), name='create-client'),
    path('client/<int:pk>/', views.DetailClientView.as_view(), name='detail-client'),
    path('client/<int:pk>/update/', views.UpdateClientView.as_view(), name='update-client'),
    path('client/<int:pk>/delete/', views.DeleteClientView.as_view(), name='delete-client'),
]
