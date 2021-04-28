from django.urls import path
from .views import ObjectViews, ObjectRetrieve

urlpatterns = [
  path('objects/', ObjectViews.as_view()),
  path('objects/<int:pk>/', ObjectRetrieve.as_view()),
]
