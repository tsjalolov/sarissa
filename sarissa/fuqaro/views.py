import datetime
import django_filters
from django.db.models import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions

from django_filters import rest_framework as filters
from django_filters import DateRangeFilter, DateFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class PageSizeControl(PageNumberPagination):
    '''aloxida ulash uchun'''
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


""" Manzillar """


class DavlatListView(generics.ListAPIView):  # manzil davlat  №1
    queryset = Davlat.objects.all()
    serializer_class = DavlatListSerializer
    permission_classes = (CustomDjangoModelPermissions,)


class ViloyatListView(generics.ListAPIView):  # manzil viloyat  №2
    permission_classes = (CustomDjangoModelPermissions,)
    serializer_class = ViloyatListSerializer
    queryset = Viloyat.objects.select_related('davlat')

    def list(self, request, *args, **kwargs):
        try:
            int(request.query_params['davlat_id'])
            id = int(request.query_params['davlat_id'])
            davlatlar = Davlat.objects.filter(id=id)
            if id > 1 and davlatlar:
                viloyat = Viloyat.objects.filter(id=15)
                serializer = ViloyatListSerializer(viloyat, many=True)

                return Response({'viloyat': serializer.data}, status=status.HTTP_200_OK)

            elif id == 1:
                viloyat = Viloyat.objects.filter(davlat_id=id)
                serializer = ViloyatListSerializer(viloyat, many=True)
                return Response({'viloyat': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'davlat id topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        except:

            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)


''' tayyor '''


class TumanListView(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):  # manzil tuman  №3
    queryset = Tuman.objects.all()
    serializer_class = TumanListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        try:
            int(request.query_params['viloyat_id'])
            viloyat_id = int(request.query_params['viloyat_id'])
            tumanlar = Tuman.objects.filter(viloyat_id=viloyat_id)
            viloyatlar = Viloyat.objects.filter(id=viloyat_id)

            if viloyat_id != 15 and viloyatlar:
                if tumanlar:
                    serializer = TumanListSerializer(tumanlar, many=True)
                    return Response({'tuman': serializer.data}, status=status.HTTP_200_OK)
            elif viloyat_id == 15:
                '''boshqa viloyat id sidan chiqarish'''
                tuman_boshqa = Tuman.objects.filter(viloyat_id=viloyat_id)
                serializer = TumanListSerializer(tuman_boshqa, many=True)
                return Response({'tuman': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Viloyat id topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        # jqwheuqwheq

        return Response({'message': 'post'})

    def destroy(self, request, *args, **kwargs):

        return Response({'message': 'dekter'})


# tuman davlat idi bilan saralash
class TumanDavlatBilanListView(generics.ListAPIView):  # manzil tuman  №3
    queryset = Tuman.objects.all()
    serializer_class = TumanListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        davlat_id = int(request.query_params['davlat_id'])
        viloyatlar = Viloyat.objects.filter(davlat=davlat_id)
        davlat = Davlat.objects.filter(id=davlat_id)
        # print(viloyatlar.values()[0]['id'])

        if davlat:
            if davlat_id == 1:
                massiv = []
                for x in viloyatlar.values():
                    massiv.append(x['id'])
                t = Tuman.objects.filter(viloyat_id__in=massiv)
                print(t)
                serializer = TumanListSerializer(t, many=True)
                return Response({'tumanlar': serializer.data}, status=status.HTTP_200_OK)

            else:
                tuman = Tuman.objects.filter(id=255)
                serializer = TumanListSerializer(tuman, many=True)
                return Response({'tumanlar': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'xato davlat_id kiritildi'}, status=status.HTTP_400_BAD_REQUEST)



    # # print(Tuman.objects.filter(viloyat_id=viloyatlar.values()[0][]))
    # tumanlar = Tuman.objects.filter(viloyat_id=viloyatlar)
    # # print(tumanlar,   'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
    #
    # serializer = TumanListSerializer(viloyatlar, many=True)
    # print(serializer.data)
    # return Response({'tuman': serializer.data}, status=status.HTTP_200_OK)


class MahallaListView(generics.ListAPIView):  # manzil mahalla №4
    queryset = Mahalla.objects.all()
    serializer_class = MahallaListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        try:
            int(request.query_params['tuman_id'])
            tuman_id = int(request.query_params['tuman_id'])
            mahallalar = Mahalla.objects.filter(tuman_id=tuman_id)
            tumanlar = Tuman.objects.filter(id=tuman_id)

            if tuman_id != 255 and tumanlar:
                print(mahallalar, 'qqqqqqqqqqqqqqqq')
                if mahallalar:
                    # print(mahallalar)
                    serializer = MahallaListSerializer(mahallalar, many=True)
                    return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)
                else:
                    mahallalar_tumanda_bulmasa = Mahalla.objects.filter(tuman_id=255)
                    serializer = MahallaListSerializer(mahallalar_tumanda_bulmasa, many=True)
                    return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)

            elif tuman_id == 255:
                boshqa_tuman = Mahalla.objects.filter(id=570)
                serializer = MahallaListSerializer(boshqa_tuman, many=True)
                return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Tuman id topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)


class KuchaListView(generics.ListAPIView):  # manzil kucha  №5
    permission_classes = (CustomDjangoModelPermissions,)
    queryset = Kucha.objects.all()
    serializer_class = KuchaListSerializer

    def list(self, request, *args, **kwargs):
        try:
            mahalla_id = int(request.query_params['mahalla_id'])
            kuchalar = Kucha.objects.filter(mahalla_id=mahalla_id)
            mahallalar = Mahalla.objects.filter(id=mahalla_id)

            if mahalla_id != 570 and mahallalar:
                if kuchalar:
                    serializer = KuchaListSerializer(kuchalar, many=True)
                    return Response({'kucha': serializer.data}, status=status.HTTP_200_OK)
            elif mahalla_id == 570:
                boshqa_mahalla = Kucha.objects.filter(id=3297)
                serializer = KuchaListSerializer(boshqa_mahalla, many=True)
                return Response({'kucha': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'mahalla id topilmadi'}, status=status.HTTP_404_NOT_FOUND)


        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)


""" Boshqa manzil """


class BoshqaManzilListView(generics.ListAPIView):  # manzil boshqa manzil  №6
    queryset = Boshqa_manzili.objects.all()
    serializer_class = BoshqaManzilListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        try:
            fuqaro_id = int(request.query_params['fuqaro_id'])
            boshqa_manzil = Boshqa_manzili.objects.filter(fuqaro_id=fuqaro_id)

        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)
        if boshqa_manzil:
            serializer = BoshqaManzilListSerializer(boshqa_manzil, many=True)
            return Response({'boshqa manzil': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'fuqaroning boshqa manzili yoq'}, status=status.HTTP_404_NOT_FOUND)


""" Jins """


class JinsListView(generics.ListAPIView):  # jins  №7
    queryset = Jins.objects.all()
    serializer_class = JinsListSerializer

    # def list(self, request, *args, **kwargs):
    #     users = request.user
    # print(users.tashkilot_id)


""" Millat """


class MillatListView(generics.ListAPIView):  # millat  №8
    queryset = Millat.objects.all()
    serializer_class = MillatListSerializer


""" Filterlar """


class SaleItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='qushulgan_sana', lookup_expr=('gte'))
    end_date = DateFilter(field_name='qushulgan_sana', lookup_expr=('lte'))
    date_range = DateRangeFilter(field_name='qushulgan_sana')

    class Meta:
        model = Fuqaro
        fields = ['qushulgan_sana', ]


class TashkilotFuqaroFilter(django_filters.FilterSet):
    class Meta:
        model = Fuqaro
        fields = ['add_user__tashkilot']


""" Fuqarolik turi """


class FuqarolikTuriListView(generics.ListAPIView):  # fuqaro_tur №9
    queryset = Fuqarolik_turi.objects.all()
    serializer_class = FuqarolikTuriListSerializer


""" Fuqarolar """

'''fuqaro id kelsa o`sha fuqaroni chiqaradi'''
class FuqaroAlohidaListView(generics.ListAPIView):  # fuqaro_tur №9
    queryset = Fuqaro.objects.select_related('doimiy_kucha','doimiy_tuman','doimiy_viloyat','jins','millat_id','fuqaro_tuman','tug_joy_davlat_id')

    def list(self, request, *args, **kwargs):
        try:
            id = int(request.query_params['id'])
        except ValueError:
            return Response({'message': 'parametrga xatolik buldi'}, status=status.HTTP_400_BAD_REQUEST)
        fuqaro = Fuqaro.objects.filter(id=id)

        if fuqaro:
            serializer_fuqaro = FuqaroAlohidaListSerializer(fuqaro, many=True)
            return Response({'fuqaro': serializer_fuqaro.data}, status=status.HTTP_200_OK)

        else:
            return Response({'fuqaro': 'Bu id  lik fuqaro yo`q'}, status=status.HTTP_200_OK)




class FuqaroListView(generics.ListAPIView):  # fuqaro №10
    queryset = Fuqaro.objects.all()
    serializer_class = FuqaroListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):

        try:
            jshir = int(request.query_params['jshir'])
            if len(str(jshir)) == 14:
                fuqaro = Fuqaro.objects.filter(jshir=jshir)
                if fuqaro:
                    '''fuqaro bazada bor'''
                    if fuqaro.values()[0]['status']:
                        return Response({'baza_status': 7, 'fuqaro_turi': 1, 'fuqaro_id': fuqaro.values()[0]['id']})

                    return Response({'baza_status': 6, 'fuqaro_turi': 1, 'fuqaro_id': fuqaro.values()[0]['id']})

                else:
                    bazafuqaro = Baza_Fuqaro.objects.filter(jshir=jshir)
                    if bazafuqaro:
                        serializer_fuqaro = BazaFuqaroSerializer(bazafuqaro[0])
                        return Response({'baza_status': 2, 'fuqaro': serializer_fuqaro.data}, status=status.HTTP_200_OK)

                    return Response({'baza_status': 1, 'jshir': jshir}, status=status.HTTP_200_OK)

            return Response({'message': 'uzunlik xato'}, status=status.HTTP_404_NOT_FOUND)  # jsir 14 emas

        except:
            return Response({'message': 'xato jshir'}, status=status.HTTP_404_NOT_FOUND)


class FuqaroCreate(generics.CreateAPIView):
    queryset = Fuqaro.objects.all()
    serializer_class = FuqaroPostSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(add_user=self.request.user)


""" Usmir """


class UsmirListView(generics.ListAPIView):  # usmir   №11
    queryset = Usmir.objects.all()
    serializer_class = UsmirListSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        try:
            guvohnoma_seriya = request.query_params['seriya']
            guvohnoma_raqam = int(request.query_params['raqam'])
            usmir = Usmir.objects.filter(Q(guvohnoma_seriya=guvohnoma_seriya) & Q(guvohnoma_raqam=guvohnoma_raqam))
            baza_usmir = BazaUsmir.objects.filter(
                Q(guvohnoma_seriyasi=guvohnoma_seriya) & Q(guvohnoma_raqami=guvohnoma_raqam))
            if usmir:
                serializer_usmir = UsmirSerializer(usmir, many=True)
                return Response({'baza_status': 7, 'fuqaro_turi': 2, 'messenger': serializer_usmir.data},
                                status=HTTP_200_OK)
            elif baza_usmir:
                serializer_usmir = BazaUsmirSerializer(baza_usmir, many=True)
                return Response({'baza_status': 2, 'fuqaro_turi': 2, 'messenger': serializer_usmir.data},
                                status=HTTP_200_OK)

            else:
                return Response({'baza_status': 1, 'seriya': guvohnoma_seriya, 'raqam': guvohnoma_raqam, },
                                status=HTTP_200_OK)

        except:
            return Response({'messenger': 'xato parametr'}, status=status.HTTP_404_NOT_FOUND)




'''usmir id kelsa o`sha usmirni chiqaradi'''
class UsmirAlohidaListView(generics.ListAPIView):  # fuqaro_tur №11
    queryset = Usmir.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            id = int(request.query_params['id'])
        except ValueError:
            return Response({'message': 'parametrga xatolik buldi'}, status=status.HTTP_400_BAD_REQUEST)
        usmir = Usmir.objects.filter(id=id)

        if usmir:
            print(usmir)
            serializer = UsmirIDListSerializer(usmir, many=True)
            return Response({'usmir': serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({'fuqaro': 'Bu id  lik usmir yo`q'}, status=status.HTTP_200_OK)

class UsmirCreate(generics.CreateAPIView):
    queryset = Usmir.objects.all()
    serializer_class = UsmirPostSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(add_user=self.request.user)




""" mkb10 """


class mkb10ListView(generics.ListAPIView):
    queryset = mkb10.objects.all()
    serializer_class = mkb10ListSerializer
    pagination_class = PageSizeControl
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['r', 'name']
    ordering_fields = ['name']


""" Tashkilotlar """


class TashkilotTurListView(generics.ListAPIView):
    queryset = Tashkilot_tur.objects.all()
    serializer_class = TashkilotTurListSerializer


class TashkilotListView(generics.ListAPIView):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotListSerializer
    pagination_class = PageSizeControl


class TashkilotQushimchaMalumotListView(generics.ListAPIView):
    queryset = Tashkilot_qushimcha_malumot.objects.all()
    serializer_class = TashkilotQushimchaMalumotListSerializer


class TashkilotTelListView(generics.ListAPIView):
    queryset = Tashkilot_Tel.objects.all()
    serializer_class = TashkilotTelListSerializer

''' op ga mahalla qo'shish uchun o'zinng tumanining mahallalarini chiqarish '''
class MahallaOpTumanListView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        tashkilot = Tashkilot.objects.get(id=self.request.user.tashkilot_id)
        tuman_id = tashkilot.tuman_id_id
        mahalla = Mahalla_op.objects.filter(tashkilot=self.request.user.tashkilot_id)
        massiv = []
        for x in mahalla.values():
            massiv.append(x['mahalla_id'])

        mahallalar = Mahalla.objects.filter(Q(tuman_id=tuman_id)&~Q(id__in = (massiv)))
        serializer = MahallaListSerializer(mahallalar, many=True)
        return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)

''' op ga mahalla qo'shish '''
class MahallaOpPsotListView(generics.CreateAPIView):
    queryset = Mahalla_op.objects.all()
    serializer_class = MahallaOPPostSerializer
    permission_classes = (CustomDjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(tashkilot_id=self.request.user.tashkilot_id)

'''#  o'ziga biriktirilgan mahallalar ro'yxati '''
class MahallaOPListView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        tashkilot = self.request.user.tashkilot_id
        mahallalar = Mahalla_op.objects.filter(tashkilot_id=tashkilot)
        serializer = MahallaOPListSerializer(mahallalar, many=True)
        return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)

''' op ga mahalla qo'shilganlarni o'chirish '''
class MahallaOPDeletePost(generics.DestroyAPIView):
    serializer_class = MahallaOPListSerializer
    queryset = Mahalla_op.objects.all()
    permission_classes = (CustomDjangoModelPermissions,)
