""" Usmir Uchot Serializer """
from rest_framework import serializers
from .models import *
from fuqaro.serializers import *


class UchotTuriListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UchotTuri
        fields = '__all__'


class UchotListSerializer(serializers.ModelSerializer):
    # tashkilot_id = serializers.SlugRelatedField(slug_field='nomi', read_only=True)
    # kucha_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # uchot_turi_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # add_user_id = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Uchot
        fields = '__all__'
