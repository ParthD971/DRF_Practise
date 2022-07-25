from rest_framework import serializers
from seri.models import Account, TestUser


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
