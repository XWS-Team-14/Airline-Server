from allauth.account.views import ConfirmEmailView
from django.contrib import admin
from django.urls import path, include, re_path

from airline_server.views import UserListView, UserDetailView, UserUpdateView, UserDeleteView
from airline_server.views.auth_views import RegisterView

from django.urls import path, re_path

urlpatterns = [
    path('api/admin/', admin.site.urls),

    # User views
    path('api/user/all', UserListView.as_view(), name='user-all'),
    path('api/user/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
    path('api/user/<uuid:id>/', UserUpdateView.as_view(), name='user-update'),
    path('api/user/<uuid:id>/', UserDeleteView.as_view(), name='user-delete'),

    # Auth views
    # path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('accounts/', include('allauth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
]
