from curses.ascii import US
from rest_framework import serializers
from team.serializers import UserSerializer

from .models import Client, Note


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            'created_by',
            'created_at',
            'updated_at',
        )
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'created_at',
            'updated_at',
        )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
        )
