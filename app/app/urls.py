from django.contrib import admin
from django.urls import include
from django.urls import path

from airline_server.views import UserListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('api/admin/', admin.site.urls),

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
