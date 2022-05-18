from rest_framework import serializers

from fuqaro_uchot.models import *
from .models import *

""" Manzillar """


class DavlatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davlat
        fields = "__all__"


'''sinov'''
class ViloyatSinovSerializer(serializers.ModelSerializer):

    class Meta:
        model = Viloyat
        fields = ("id", "name", "davlat")


class ViloyatListSerializer(serializers.ModelSerializer):
    davlat = DavlatListSerializer()

    class Meta:
        model = Viloyat
        fields = '__all__'


class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = ['id', 'name', ]


class TumanListSerializer(serializers.ModelSerializer):
    viloyat_id = ViloyatSerializer()

    class Meta:
        model = Tuman
        fields = '__all__'


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = ['id', 'name', ]


class MahallaListSerializer(serializers.ModelSerializer):
    tuman_id = TumanListSerializer()

    class Meta:
        model = Mahalla
        fields = '__all__'


class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = ['id', 'name', ]


class KuchaListSerializer(serializers.ModelSerializer):
    mahalla_id = MahallaListSerializer()


    class Meta:
        model = Kucha
        fields = '__all__'


class KuchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kucha
        fields = ['id', 'name', ]


""" Jins """


class JinsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jins
        fields = '__all__'


""" Millat """


class MillatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Millat
        fields = '__all__'


""" Fuqaro Detail Get"""


class FuqaroListSerializer(serializers.ModelSerializer):
    tug_joy_davlat_id = DavlatListSerializer()
    tug_joy_tuman_id = TumanSerializer()
    millat_id = MillatListSerializer()
    pass_kim_bergan_tuman_id = TumanSerializer()
    jins = JinsListSerializer()
    doimiy_viloyat = ViloyatSerializer()
    doimiy_tuman = TumanSerializer()
    doimiy_mahalla = MahallaSerializer()
    doimiy_kucha = KuchaSerializer()
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


class BoshqaManzilListSerializer(serializers.ModelSerializer):
    fuqaro_id = FuqaroSerializer()
    yashash_viloyat = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_tuman = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_mahalla = serializers.SlugRelatedField(slug_field='name', read_only=True)
    yashash_kucha = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Boshqa_manzili
        fields = "__all__"


""" Fuqarolik turi """


class FuqarolikTuriListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuqarolik_turi
        fields = "__all__"


""" Usmir """

class UsmirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usmir
        fields = "__all__"


class BazaUsmirSerializer(serializers.ModelSerializer):
    class Meta:
        model = BazaUsmir
        fields = "__all__"


class UsmirListSerializer(serializers.ModelSerializer):
    tug_joy_davlat_id = DavlatListSerializer()
    tug_joy_tuman_id = TumanSerializer()
    millat_id = MillatListSerializer()
    guvohnoma_kim_bergan_tuman_id = TumanSerializer()
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
        fields = "__all__"


""" Tashkilotlar """


class TashkilotTurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkilot_tur
        fields = "__all__"


class TashkilotListSerializer(serializers.ModelSerializer):
    tashkilot_turi = TashkilotTurListSerializer()
    tuman_id = TumanSerializer()

    class Meta:
        model = Tashkilot
        fields = "__all__"


class TashkilotQushimchaMalumotListSerializer(serializers.ModelSerializer):
    tashkilot_id = TashkilotListSerializer()

    class Meta:
        model = Tashkilot_qushimcha_malumot
        fields = "__all__"


class TashkilotTelListSerializer(serializers.ModelSerializer):
    tashkilot = TashkilotListSerializer()

    class Meta:
        model = Tashkilot_Tel
        fields = "__all__"


""" Mahalla OP """


class MahallaOPListSerializer(serializers.ModelSerializer):
    tashkilot = TashkilotListSerializer()
    mahalla = MahallaSerializer()

    class Meta:
        model = Mahalla_op
        fields = "__all__"
