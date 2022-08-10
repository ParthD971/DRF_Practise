import time

from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer

from .models import Transformer, Book


class TransformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transformer
        fields = ['url', 'name', 'alternate_mode', 'description', 'alive']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'name', 'published']


# class NameValidator(object):
#     def set_context(self, serializer_field):
#         """
#         This hook is called by the serializer instance,
#         prior to the validation call being made.
#         """
#         # Determine the existing instance, if this is an update operation.
#         self.instance = getattr(serializer_field.parent, 'instance', None)
#         if not self.instance:
#             # try to get user from professionals:
#             root_instance = getattr(serializer_field.root, 'instance', None)
#             self.instance = getattr(root_instance, 'user', None)
#
#     def __call__(self, value):
#         if self.instance and Book.objects.filter(name=value).exclude(id=self.instance.id).exists():
#             raise ValidationError('Name already exists.')
#
#         if not self.instance and Book.objects.filter(name=value).exists():
#             raise ValidationError('Username already exists.')


class SimpleBookSerializer(serializers.ModelSerializer):
    def validate_name(self, name):
        if self.context.get('name', None) and self.context.get('name').get(name) > 1:
            raise serializers.ValidationError("Name must be unique")
        return name

    class Meta:
        model = Book
        fields = ['id', 'name', 'published']
        unique_together = ("name",)


class BulkCreateBookSerializer(SimpleBookSerializer):
    pass


class UpdateListSerializer(serializers.ListSerializer):
    def update(self, instances, validated_data):
        instance_hash = {index: instance for index, instance in enumerate(instances)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        return result


class BulkUpdateBookSerializer(SimpleBookSerializer):
    name = serializers.CharField(max_length=255)

    def validate_name(self, name):
        name = super(BulkUpdateBookSerializer, self).validate_name(name)
        print('sasasa', self.context.get('name', None))
        if self.context.get('name', None) and self.context.get('name').get(name) > 1:
            raise serializers.ValidationError("Name must be unique")
        return name

    def validate_id(self, book_id):
        if book_id not in self.context.get('book_ids'):
            raise serializers.ValidationError("Id is not valid.")
        return book_id

    def create(self, validated_data):
        if self.context.get('book_ids', None):
            instance = Book.objects.get(id=validated_data['id'])
            return self.update(instance, validated_data)
        return super(SimpleBookSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.published = validated_data["published"]
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['id', 'name', 'published']
        list_serializer_class = UpdateListSerializer


class FooSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = Book
        fields = ('id', 'name', 'published')
        list_serializer_class = BulkListSerializer

