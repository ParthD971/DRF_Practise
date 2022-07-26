from rest_framework import serializers
from .models import Transformer, Book


class TransformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transformer
        fields = ['url', 'name', 'alternate_mode', 'description', 'alive']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'name', 'published']


class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'published']

