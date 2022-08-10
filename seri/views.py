from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from seri.models import Account, TestUser, Album, Track
from seri.serializers import AccountSerializer, TestUserSerializer, AlbumSerializer, TrackSerializer


class SerializerView(APIView):
    def get(self, request):
        return Response({'sasasasas'})


class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_name'


class TestUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = TestUser.objects.all()
    serializer_class = TestUserSerializer


class TestUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestUser.objects.all()
    serializer_class = TestUserSerializer
    lookup_field = 'username'


class AlbumViewset(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class TrackViewset(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

