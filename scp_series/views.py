from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Object
from .serializers import ObjectSerializer


class ObjectViews(generics.ListCreateAPIView):
  queryset = Object.objects.all()
  serializer_class = ObjectSerializer


class ObjectRetrieve(generics.RetrieveUpdateAPIView):
  queryset = Object.objects.all()
  serializer_class = ObjectSerializer
