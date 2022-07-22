from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Transformer
from .serializers import TransformerSerializer

from rest_framework import mixins
from rest_framework import generics

from rest_framework.permissions import DjangoModelPermissions


# Simple APIView
# class TransformerList(APIView):
#     """
#     List all Transformers, or create a new Transformer
#     """
#
#     def get(self, request, format=None):
#         transformers = Transformer.objects.all()
#         serializer = TransformerSerializer(transformers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TransformerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TransformerDetail(APIView):
#     """
#     Retrieve, update or delete a transformer instance
#     """
#
#     def get_object(self, pk):
#         # Returns an object instance that should
#         # be used for detail views.
#         try:
#             return Transformer.objects.get(pk=pk)
#         except Transformer.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer,
#                                            data=request.data,
#                                            partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         transformer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GenericAPIView and mixins
# class TransformerList(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       generics.GenericAPIView):
#     queryset = Transformer.objects.all()
#     serializer_class = TransformerSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class TransformerDetail(mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.GenericAPIView):
#     queryset = Transformer.objects.all()
#     serializer_class = TransformerSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Generic
class TransformerList(generics.ListCreateAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer
    permission_classes = [DjangoModelPermissions, ]


class TransformerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer
    permission_classes = [DjangoModelPermissions, ]
