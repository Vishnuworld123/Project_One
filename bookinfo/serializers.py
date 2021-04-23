from bookinfo.models import Book, Dreamreal
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['is_deleted']

class DreamrealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dreamreal
        exclude = ['is_deleted']
