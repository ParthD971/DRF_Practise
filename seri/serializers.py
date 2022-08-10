import time

from rest_framework import serializers
from seri.models import Account, TestUser, Album, Track


class TestUserSerializer(serializers.ModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(source='account', queryset=Account.objects.all())

    class Meta:
        model = TestUser
        fields = ('id', 'username', 'first_name', 'last_name', 'accounts')
        depth = 3


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='account-detail',
        lookup_field='account_name'
    )

    users = serializers.HyperlinkedRelatedField(
        view_name='testuser-detail',
        lookup_field='username',
        many=True,
        read_only=True
    )

    class Meta:
        model = Account
        fields = ('url', 'id', 'account_name', 'users')
        depth = 3


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    tracks = TrackSerializer(many=True)
    track_count = serializers.SerializerMethodField()

    def get_track_count(self, obj):
        return obj.tracks.count()

    class Meta:
        model = Album
        fields = ('id', 'album_name', 'artist', 'tracks', 'track_count')



