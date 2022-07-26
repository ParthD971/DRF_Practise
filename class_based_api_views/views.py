from django.http import Http404
from django.shortcuts import get_object_or_404
from guardian.shortcuts import assign_perm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Transformer, Book
from .serializers import TransformerSerializer, BookSerializer, SimpleBookSerializer

from rest_framework import mixins
from rest_framework import generics

from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, \
    IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet, ReadOnlyModelViewSet


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


# Generic AND Permissions
class TransformerList(generics.ListCreateAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer
    permission_classes = [AllowAny, ]
#     permission_classes = [IsAuthenticated, ]
#     permission_classes = [IsAuthenticatedOrReadOnly, ]
#     permission_classes = [IsAdminUser, ]
#     permission_classes = [DjangoModelPermissions, ]
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]
#     permission_classes = [DjangoObjectPermissions, ]
#
#     def perform_create(self, serializer):
#         instance = serializer.save()
#         assign_perm("delete_transformer", self.request.user, instance)


class TransformerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer
    permission_classes = [AllowAny, ]
#     permission_classes = [IsAuthenticated, ]
#     permission_classes = [IsAuthenticatedOrReadOnly, ]
#     permission_classes = [IsAdminUser, ]
#     permission_classes = [DjangoModelPermissions, ]
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]
#     permission_classes = [DjangoObjectPermissions, ]


# class BookViewSet(ViewSet):
#     queryset = Book.objects.all()
#
#     def list(self, request):
#         serializer = BookSerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         item = get_object_or_404(self.queryset, pk=pk)
#         serializer = BookSerializer(item)
#         return Response(serializer.data)


# class BookViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()


# class BookViewSet(GenericViewSet):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
#     # permission_classes = [DjangoObjectPermissions]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def list(self, request):
#         serializer = self.get_serializer(self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         item = self.get_object()
#         serializer = self.get_serializer(item)
#         return Response(serializer.data)
#
#     def destroy(self, request):
#         item = self.get_object()
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, ]


class TransformerViewSet(ModelViewSet):
    serializer_class = TransformerSerializer
    queryset = Transformer.objects.all()
    # permission_classes = [IsAuthenticated, ]


class BookBulkCreateUpdate(generics.GenericAPIView):
    serializer_class = SimpleBookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = self.get_serializer(self.get_queryset(), data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return self.bulk_update(request)

    def bulk_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        # restrict the update to the filtered queryset
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()),
            data=request.data,
            many=True,
            partial=partial,
        )
        validated_data = []
        errors = []
        serializers_list = []
        for item in request.data:
            item_serializer = self.get_serializer(
                Book.objects.get(id=item['id']),
                data=item,
                partial=partial,
            )
            if not item_serializer.is_valid(raise_exception=False):
                errors.append({item['id']: item_serializer.errors})
            else:
                validated_data.append(item_serializer.validated_data)
                serializers_list.append(item_serializer)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        serializer._validated_data = validated_data
        for _serializer in serializers_list:
            _serializer.save()
        return Response(validated_data, status=status.HTTP_200_OK)


