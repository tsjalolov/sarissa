""" Usmir Uchot Serializer """
from rest_framework import serializers
from .models import *
from fuqaro.serializers import *


class UchotTuriListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UchotTuri
        fields = '__all__'


class UchotListSerializer(serializers.ModelSerializer):
    fuqaro = FuqaroSerializer()
    usmir = UsmirSerializer()
    chetel_fuqaro = ChetElFuqarosiListSerializer()

    # creat
    # tashkilot_id = serializers.SlugRelatedField(slug_field='nomi', read_only=True)
    kucha_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    uchot_turi_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
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


class MahallaOPKuchaSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} --> {}'.format(obj.mahalla_id, obj.name)

    class Meta:
        model = Kucha
        fields = ['id', 'full_name', ]


class SinovUchotListSerializer(serializers.ModelSerializer):
    if UsmirSerializer():
        fuqaro = FuqaroSerializer()
    # usmir = UsmirSerializer()
    # chetel_fuqaro =ChetElFuqarosiListSerializer()



    kucha_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    uchot_turi_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # add_user_id = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Uchot
        exclude = ('add_user_id', 'tashkilot_id')


class MyPeopleViloyatAllOrmSerializer(serializers.ModelSerializer):
    tuman_id = serializers.IntegerField()
    tuman_name = serializers.CharField()
    fuqarolar_soni = serializers.IntegerField()
    usmirlar_soni = serializers.IntegerField()
    chetlar_soni = serializers.IntegerField()
    jami = serializers.IntegerField()
    class Meta:
        model = Uchot
        fields = ('tuman_id', 'tuman_name', 'fuqarolar_soni', 'usmirlar_soni', 'chetlar_soni', 'jami')

class UchotTashkilotlarBuyichaSerializer(serializers.ModelSerializer):
    tashkilott_id = serializers.IntegerField()
    tashkilot_name = serializers.CharField()
    fuqarolar_soni = serializers.IntegerField()
    usmirlar_soni = serializers.IntegerField()
    chetlar_soni = serializers.IntegerField()
    jami = serializers.IntegerField()
    malumot = serializers.IntegerField()
    class Meta:
        model = Uchot
        fields = ('tashkilott_id', 'tashkilot_name', 'fuqarolar_soni', 'usmirlar_soni', 'chetlar_soni', 'jami','malumot')

class OpAholiKuchaBuyichaSerializer(serializers.ModelSerializer):
    kuchaa_id = serializers.IntegerField()
    fuqarolar_soni = serializers.IntegerField()
    usmirlar_soni = serializers.IntegerField()
    chetlar_soni = serializers.IntegerField()
    jami = serializers.IntegerField()
    kuchaa_name = serializers.CharField()
    class Meta:
        model = Uchot
        fields = ('kuchaa_id',  'fuqarolar_soni', 'usmirlar_soni', 'chetlar_soni', 'jami','kuchaa_name')