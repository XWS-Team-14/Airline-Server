from django.contrib import admin
from django.urls import include
from django.urls import path


from airline_server.views import PlaceCreateView, PlaceDeleteView, PlaceDetailView, PlaceListView, PlaceUpdateView
from airline_server.views import RouteCreateView, RouteDeleteView, RouteDetailView, RouteListView, RouteUpdateView
from airline_server.views import SearchList
from airline_server.views import UserListView, UserDetailView, UserUpdateView, UserDeleteView

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

    # Flight Search
    path('api/search/', SearchList.as_view(), name='search-flights'),

    # User views
    path('api/user/all', UserListView.as_view(), name='user-all'),
    path('api/user/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
    path('api/user/<uuid:id>/', UserUpdateView.as_view(), name='user-update'),
    path('api/user/<uuid:id>/', UserDeleteView.as_view(), name='user-delete'),

    # Auth views
    path('api/accounts/', include('allauth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),

]
