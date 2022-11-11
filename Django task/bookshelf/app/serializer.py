from .models import BookShelf
from rest_framework import serializers

class BookShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookShelf
        fields='__all__'