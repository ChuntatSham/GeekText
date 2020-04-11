from django.urls import path
from .views import (
    SignUpView,
    ProfileView,
    AddressView,
    AddressListView,
    AddressUpdateView,
    AddressDeleteView,
    CCardView,
    CCardListView,
    CCardUpdateView,
    CCardDeleteView,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView, name='signup'),
    path('profile/', ProfileView, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    # Address urls
    path('add-address/', AddressView, name='add_address'),
    path('address-management/<int:id>/update/', AddressUpdateView, name='address_update'),
    path('address-management/', AddressListView, name='address_management'),
    path('address-management/<int:id>/update/delete/', AddressDeleteView, name='address_delete'),
    # Credit cards urls
    path('add-card/', CCardView, name='add_card'),
    path('card-management/<int:id>/update/', CCardUpdateView, name='card_update'),
    path('card-management/', CCardListView, name='card_management'),
    path('card-management/<int:id>/update/delete/', CCardDeleteView, name='card_delete'),
]
