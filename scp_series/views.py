from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework import generics, permissions
from .models import Object
from .serializers import ObjectSerializer
from .permissions import IsOwnerOrReadOnly


class ObjectViews(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  queryset = Object.objects.all()
  serializer_class = ObjectSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class ObjectRetrieve(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  queryset = Object.objects.all()
  serializer_class = ObjectSerializer