from knox import views as knox_views
from django.urls import path
from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]
