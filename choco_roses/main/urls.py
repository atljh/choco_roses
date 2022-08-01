from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base, name='main-url'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)