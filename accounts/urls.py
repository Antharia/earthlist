from django.urls import path

from .views import SignupPageView
from .views import dashboard_view


urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
