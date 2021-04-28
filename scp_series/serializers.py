from rest_framework import serializers
from .models import Object


class ObjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Object
    fields = ["item", "object_class",
              "containment_procedures", "description", "additional"]
    read_only_fields = ['id']
