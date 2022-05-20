from pip._internal.cli.cmdoptions import list_exclude
from rest_framework import serializers

from fuqaro_uchot.models import *
from .models import *

""" Manzillar """


class DavlatListSerializer(serializers.ModelSerializer):  # manzil davlat  №1
    class Meta:
        model = Davlat
        fields = "__all__"


class ViloyatListSerializer(serializers.ModelSerializer):  # manzil viloyat  №2

    class Meta:
        model = Viloyat
        fields = ("id", "name")


''' tuman '''


class TumanListSerializer(serializers.ModelSerializer):  # manzil tuman №3
    class Meta:
        model = Tuman
        fields = ['id', 'name', ]


''' mahalla '''


class MahallaListSerializer(serializers.ModelSerializer):  # manzil tuman №4
    class Meta:
        model = Mahalla
        fields = ['id', 'name', ]


class KuchaListSerializer(serializers.ModelSerializer):  # manzil kucha  №5
    mahalla_id = MahallaListSerializer()

    class Meta:
        model = Kucha
        fields = '__all__'


""" Jins """


class JinsListSerializer(serializers.ModelSerializer):  # jins  №7
    class Meta:
        model = Jins
        fields = ['id', 'name', ]


""" Millat """


class MillatListSerializer(serializers.ModelSerializer):  # millat  №8
    class Meta:
        model = Millat
        fields = '__all__'


""" Fuqaro Detail Get"""


class FuqaroListSerializer(serializers.ModelSerializer):
    tug_joy_davlat_id = DavlatListSerializer()
    tug_joy_tuman_id = TumanListSerializer()
    millat_id = MillatListSerializer()
    pass_kim_bergan_tuman_id = TumanListSerializer()
    jins = JinsListSerializer()
    doimiy_viloyat = ViloyatListSerializer()
    doimiy_tuman = TumanListSerializer()
    doimiy_mahalla = MahallaListSerializer()
    doimiy_kucha = KuchaListSerializer()
    add_user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Fuqaro
        fields = "__all__"


""" Fuqaro list Boshqa Manzil uchun  """


class FuqaroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuqaro
        fields = ['id', 'jshir', 'familiya', 'ism', 'sharif', ]


class BazaFuqaroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baza_Fuqaro
        fields = '__all__'


""" Boshqa Manzil """


class BoshqaManzilListSerializer(serializers.ModelSerializer):  # manzil boshqa manzil  №6
    fuqaro_id = FuqaroSerializer()
    yashash_viloyat = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_tuman = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_mahalla = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_kucha = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Boshqa_manzili
        fields = "__all__"


""" Fuqarolik turi """


class FuqarolikTuriListSerializer(serializers.ModelSerializer):  # fuqaro_tur №9
    class Meta:
        model = Fuqarolik_turi
        fields = "__all__"


""" Usmir """


class UsmirSerializer(serializers.ModelSerializer):
    tug_joy_davlat_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tug_joy_tuman_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    millat_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    guvohnoma_kim_bergan_tuman_id = serializers.SlugRelatedField(slug_field='name', read_only=True)
    jins = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Usmir
        exclude = ('add_user', 'qushulgan_sana', 'yangilangan_sana', 'migrant',)


class BazaUsmirSerializer(serializers.ModelSerializer):
    class Meta:
        model = BazaUsmir
        fields = "__all__"


class UsmirListSerializer(serializers.ModelSerializer):
    tug_joy_davlat_id = DavlatListSerializer()
    tug_joy_tuman_id = TumanListSerializer()
    millat_id = MillatListSerializer()
    guvohnoma_kim_bergan_tuman_id = TumanListSerializer()
    jins_id = JinsListSerializer()
    add_user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Usmir
        fields = "__all__"


""" ChetEL Fuqarosi """


class ChetElFuqarosiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChetElFuqarosi
        fields = '__all__'


""" mkb10 """


class mkb10ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = mkb10
        fields = ('id', 'r', 'name')

""" Tashkilotlar """


class TashkilotTurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkilot_tur
        fields = "__all__"


class TashkilotListSerializer(serializers.ModelSerializer):
    tashkilot_turi = TashkilotTurListSerializer()
    tuman_id = TumanListSerializer()

    class Meta:
        model = Tashkilot
        fields = "__all__"


class TashkilotQushimchaMalumotListSerializer(serializers.ModelSerializer):
    # tashkilot_id = TashkilotListSerializer()

    class Meta:
        model = Tashkilot_qushimcha_malumot
        fields = ('fuqarolari_soni', 'oila_soni', 'tashkilot_id',)


class TashkilotTelListSerializer(serializers.ModelSerializer):
    # tashkilot = TashkilotListSerializer()

    class Meta:
        model = Tashkilot_Tel
        fields = "__all__"


""" Mahalla OP """


class MahallaOPListSerializer(serializers.ModelSerializer):
    tashkilot = TashkilotListSerializer()
    mahalla = MahallaListSerializer()

    class Meta:
        model = Mahalla_op
        fields = "__all__"
