from django.urls import path

from accounts.views import SignUpView, dashboard as edit_user


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('edit/', edit_user, name='edit_user'), 
]