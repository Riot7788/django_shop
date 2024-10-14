from django.urls import path


from .views import (
    login,
    registration,
    profile,
    logout,
    users_cart,
)


urlpatterns = [
    path('login', login, name="login"),
    path('registration', registration, name="registration"),
    path('profile', profile, name="profile"),
    path('users_cart', users_cart, name="users_cart"),
    path('logout', logout, name="logout"),
]