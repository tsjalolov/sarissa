'''from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import GroupManager, Group, Permission
from .models import Tashkilot, CustomUser, CustomGroup
from django.contrib.auth.hashers import make_password

 userga parol yozish
def index(request):
    # polzovatel kiritish
    customer = CustomUser.objects.all().values()[0]
    tashkilotlar = Tashkilot.objects.all().values()
    groups = Group.objects.all().values()
    #  print(groups)
    for elem in tashkilotlar:
        CustomUser.objects.create(
            username=elem['login'],
            password=make_password(elem['parol']),
            tashkilot_id=elem['id'],
            is_superuser=False,
            is_staff=False,
            is_active=True
        )
    return HttpResponse('hello')
def second_index(request):
    all_cus = CustomUser.objects.count()
    # print(all_cus)
    customers = CustomUser.objects.all().values()[1:]
    # print((customers))
    for elem in customers:
        tashkilot_item = Tashkilot.objects.filter(id=elem['tashkilot_id']).values()
        for item in tashkilot_item:
            i = CustomGroup.objects.filter(tashkilot_turi_id=item['tashkilot_turi_id']).values()
            a = (elem['id'], 'q', i[0]['group_ptr_id'])
            print(a)

    return HttpResponse(a)
'''

import datetime
import django_filters
from django.db.models import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissions

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
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


""" Manzillar """


class DavlatListView(generics.ListAPIView):  # manzil davlat  №1
    queryset = Davlat.objects.all()
    serializer_class = DavlatListSerializer
    permission_classes = (IsAuthenticated,)


class ViloyatListView(APIView):  # manzil viloyat  №2
    permission_classes = (IsAuthenticated,)

    def get(self, request):
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


class TumanListView(APIView):  # manzil tuman  №3

    def get(self, request):

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


class MahallaListView(APIView):  # manzil mahalla №4
    def get(self, request):
        try:
            int(request.query_params['tuman_id'])
            tuman_id = int(request.query_params['tuman_id'])
            mahallalar = Mahalla.objects.filter(tuman_id=tuman_id)
            tumanlar = Tuman.objects.filter(id=tuman_id)

            if tuman_id != 255 and tumanlar:
                print(mahallalar, 'qqqqqqqqqqqqqqqq')
                if mahallalar:
                    print(mahallalar)
                    serializer = MahallaListSerializer(mahallalar, many=True)
                    return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Tuman id  da mahalla yoq'}, status=status.HTTP_404_NOT_FOUND)

            elif tuman_id == 255:
                boshqa_tuman = Mahalla.objects.filter(id=570)
                serializer = MahallaListSerializer(boshqa_tuman, many=True)
                return Response({'mahalla': serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Tuman id topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)


class KuchaListView(generics.ListAPIView):      # manzil kucha  №5
    # permission_classes = (DjangoModelPermissions,)
    def get(self, request):
        try:
            mahalla_id = int(request.query_params['mahalla_id'])
            kuchalar = Kucha.objects.filter(mahalla_id=mahalla_id)
            mahallalar = Mahalla.objects.filter(id=mahalla_id)

            if mahalla_id != 570 and mahallalar:
                if kuchalar:
                    serializer = KuchaSerializer(kuchalar, many=True)
                    return Response({'kucha': serializer.data}, status=status.HTTP_200_OK)
            elif mahalla_id == 570:
                boshqa_mahalla = Kucha.objects.filter(id=3297)
                serializer = KuchaSerializer(boshqa_mahalla, many=True)
                return Response({'kucha': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'mahalla id topilmadi'}, status=status.HTTP_404_NOT_FOUND)


        except:
            return Response({'message': 'Xato parametr kiritildi'}, status=status.HTTP_404_NOT_FOUND)


""" Boshqa manzil """


class BoshqaManzilListView(generics.ListAPIView):
    queryset = Boshqa_manzili.objects.all()
    serializer_class = BoshqaManzilListSerializer


""" Jins """


class JinsListView(generics.ListAPIView):
    queryset = Jins.objects.all()
    serializer_class = JinsListSerializer


""" Millat """


class MillatListView(generics.ListAPIView):
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


""" Fuqarolar """


class FuqaroListView(APIView):

    def get(self, request):

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

                    return Response({'baza_status': 1, 'jshir': jshir}, status=status.HTTP_204_NO_CONTENT)

            return Response({'message': 'uzunlik xato'})  # jsir 14 emas

        except:
            return Response({'message': 'xato jshir'})


""" Fuqarolik turi """


class FuqarolikTuriListView(generics.ListAPIView):
    queryset = Fuqarolik_turi.objects.all()
    serializer_class = FuqarolikTuriListSerializer


""" Usmir """


class UsmirListView(APIView):

    # def get(self, request):
    #     return Response({'user': 'sss'})

    def get(self, request):
        try:
            guvohnoma_seriya = request.query_params['seriya']
            guvohnoma_raqam = int(request.query_params['raqam'])
            usmir = Usmir.objects.filter(Q(guvohnoma_seriya=guvohnoma_seriya) & Q(guvohnoma_raqam=guvohnoma_raqam))
            baza_usmir = BazaUsmir.objects.filter(
                Q(guvohnoma_seriyasi=guvohnoma_seriya) & Q(guvohnoma_raqami=guvohnoma_raqam))
            if usmir:
                serializer_usmir = UsmirSerializer(usmir, many=True)
                return Response({'baza_status': 7, 'messenger': serializer_usmir.data}, status=HTTP_200_OK)
            elif baza_usmir:
                serializer_usmir = BazaUsmirSerializer(baza_usmir, many=True)
                return Response({'baza_status': 2, 'messenger': serializer_usmir.data}, status=HTTP_200_OK)

            else:
                return Response({'baza_status': 1, 'seriya': guvohnoma_seriya, 'raqam': guvohnoma_raqam, },
                                status=HTTP_204_NO_CONTENT)

        except:
            return Response({'messenger': 'xato parametr'}, status=HTTP_204_NO_CONTENT)


""" ChetEl Fuqarosi """


class ChetElFuqarosiListView(generics.ListCreateAPIView):
    queryset = ChetElFuqarosi.objects.all()
    serializer_class = ChetElFuqarosiListSerializer
    pagination_class = PageSizeControl


""" mkb10 """


class mkb10ListView(generics.ListAPIView):
    queryset = mkb10.objects.all()
    serializer_class = mkb10ListSerializer
    pagination_class = PageSizeControl


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


class MahallaOPListView(generics.ListAPIView):
    queryset = Mahalla_op.objects.all()
    serializer_class = MahallaOPListSerializer

# class tugsana(APIView):
#     def get(self, request):
#         # datetime taxlash
#         number = ChetElFuqarosi.objects.all().values('qushilgan_sana')
#         for son in number:
#             try:
#                 a = ChetElFuqarosi.objects.filter(qushilgan_sana=son['qushilgan_sana']).update(
#                     qushilgan_sana_2=datetime.datetime.fromtimestamp(son['qushilgan_sana'] / 1000))
#             except ValueError:
#                 print(a)
#                 pass
#         return HttpResponse('Hello')

# 2686
