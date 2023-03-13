"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from airline_server.views import PlaceListView
from airline_server.views import PlaceDetailView
from airline_server.views import PlaceDeleteView
from airline_server.views import PlaceCreateView
from airline_server.views import PlaceUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Place crud urls
    path('place/', PlaceCreateView.as_view(), name='place-create'),
    path('place/<uuid:id>/', PlaceDetailView.as_view(), name='place-detail'),
    path('place/<uuid:id>/', PlaceUpdateView.as_view(), name='place-update'),
    path('place/<uuid:id>/', PlaceDeleteView.as_view(), name='place-delete'),
    path('place/all/', PlaceListView.as_view(), name='place-all')
]
