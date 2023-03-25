from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view


from airline_server.views import PlaceCreateView, PlaceDeleteView, PlaceDetailView, PlaceListView, PlaceUpdateView
from airline_server.views import RouteCreateView, RouteDeleteView, RouteDetailView, RouteListView, RouteUpdateView
from airline_server.views import SearchList
from airline_server.views.flight_views import FlightList, FlightCreateView, FlightDeleteView
from airline_server.views import UserListView, UserDetailView, UserUpdateView, UserDeleteView
from airline_server.views.route_views import RouteListViewWithPlaces

urlpatterns = [
    path('admin/', admin.site.urls),

    # Place crud urls
    path('api/place/', PlaceCreateView.as_view(), name='place-create'),
    path('api/place/<uuid:id>/', PlaceDetailView.as_view(), name='place-detail'),
    path('api/place/<uuid:id>/', PlaceUpdateView.as_view(), name='place-update'),
    path('api/place/<uuid:id>/', PlaceDeleteView.as_view(), name='place-delete'),
    path('api/place/all/', PlaceListView.as_view(), name='place-all'),

    # Route crud urls
    path('api/route/', RouteCreateView.as_view(), name='route-create'),
    path('api/route/<uuid:id>/', RouteDetailView.as_view(), name='route-detail'),
    path('api/route/<uuid:id>/', RouteUpdateView.as_view(), name='route-update'),
    path('api/route/<uuid:id>/', RouteDeleteView.as_view(), name='route-delete'),
    path('api/route/all/', RouteListView.as_view(), name='route-all'),
    path('api/route/all/places/', RouteListViewWithPlaces.as_view(), name='route-all-places'),

    # Flight Search
    path('api/search/', SearchList.as_view(), name='search-flights'),


    # Flight
    path('api/flight/all', FlightList.as_view(), name='fight-all'),
    path('api/flight/', FlightCreateView.as_view(), name='fight-create'),
    path('api/flight/delete/', FlightDeleteView.as_view(), name='fight-delete'),

    # User views
    path('api/user/all', UserListView.as_view(), name='user-all'),
    path('api/user/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
    path('api/user/<uuid:id>/', UserUpdateView.as_view(), name='user-update'),
    path('api/user/<uuid:id>/', UserDeleteView.as_view(), name='user-delete'),

    # Auth views
    path('api/accounts/', include('allauth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
    path('api/auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),


]
