""" Usmir Uchot Serializer """
from rest_framework import serializers
from .models import *
from fuqaro.serializers import *


class UchotTuriListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UchotTuri
        fields = '__all__'


class UchotListSerializer(serializers.ModelSerializer):
    # fuqaro = FuqaroSerializer()
    # usmir = UsmirSerializer()

    # creat
    # tashkilot_id = serializers.SlugRelatedField(slug_field='nomi', read_only=True)
    # kucha_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # uchot_turi_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # add_user_id = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Uchot
        exclude = ('add_user_id', 'tashkilot_id')

    def validate_kucha_id(self, data):
        if data.id == None:
            raise serializers.ValidationError('')
        return data

    def validate_uchot_turi_id(self, data):
        if data.id == None:
            raise serializers.ValidationError('')
        return data

    def validate_fuqaro_turi_id(self, data):
        if data.id == None:
            raise serializers.ValidationError('')
        return data