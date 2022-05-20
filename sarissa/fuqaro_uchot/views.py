import django_filters
from django.http.response import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from fuqaro.views import PageSizeControl
from .models import *
from .serializers import *


class UchotTuriListView(generics.ListAPIView):
    queryset = UchotTuri.objects.all()
    serializer_class = UchotTuriListSerializer


class UchotListView(APIView):

    def get(self, request):
        fuqaro_id = request.query_params['fuqaro_id']
        fuqaro_turi = request.query_params['fuqaro_turi']

        print(fuqaro_id, '   ', fuqaro_turi)
        return Response({'ss': 'aa'})


class UchotAPIList(generics.ListAPIView):
    serializer_class = UchotListSerializer
    pagination_class = PageSizeControl

    def get_queryset(self):
        tashkilot_nomi = self.request.user.tashkilot
        uchot = Uchot.objects.filter(tashkilot_id=tashkilot_nomi)
        if uchot:
            return uchot


class UsmirUchotView(APIView):

    def post(self, request):
        # usmir_id = request.query_params['usmir_id']
        uchot = Uchot.objects.all()
        print(uchot)
        fuqaro = Fuqaro.objects.all()[:10]
        serializer1 = FuqaroSerializer(fuqaro, many=True)
        serializer = UchotListSerializer(uchot, many=True)
        return Response({'ss': serializer.data})
        # if uchot:
        #     uchot_turi = uchot.values()[0]['uchot_turi_id_id']
        #
        #     uchot_serializer = UchotListSerializer(uchot[0])
        #     if uchot_turi == 4:
        #         return Response(
        #             {'status': 'uchotga olib bo`lmaydi 1', 'status_kod': 1, 'uchot_fuqaro': uchot_serializer.data})
        #     elif uchot_turi == 5:
        #         return Response({'status': 'uchotga olingan, yana uchotga olish mumkin 3 ga', 'status_kod': 2,
        #                          'uchot_fuqaro': uchot_serializer.data})
        #     elif uchot_turi == 6:
        #         return Response({'status': 'uchotga olingan, yana uchotga olish mumkin 2 ga', 'status_kod': 3,
        #                          'uchot_fuqaro': uchot_serializer.data})
        #
        # return Response({'status': 'uchotga olinmagan', 'status_kod': 3})



'''  id yuborganda uchotga olinganligini olib natija qaytaradi '''
class UchotApiView(APIView):



    def get(self, request):

        human_id = request.query_params['human_id']
        fuqaro_turi_id = request.query_params['fuqaro_turi_id']
        try:
            (int(fuqaro_turi_id) and int(human_id))

        except ValueError  as e:
            return Response({'message': 'parametrlar xato kiritilgan'})
        else:
            if fuqaro_turi_id == '1':
                fuqaro_uchot = Uchot.objects.filter(fuqaro_id=human_id)

                if fuqaro_uchot:
                    uchot_turi_id = fuqaro_uchot.values()[0]['uchot_turi_id_id']
                    serializer_fuqaro = UchotListSerializer(fuqaro_uchot, many=True)
                    if len(fuqaro_uchot) > 1:
                        return Response({'data': serializer_fuqaro.data, 'fuqaro': 'fuqaro', 'status': 5,
                                         'status_message': 'uchotga olib bolmaydi'}, status=status.HTTP_200_OK)
                    elif len(fuqaro_uchot) == 1:
                        for elem in fuqaro_uchot.values():
                            if elem['uchot_turi_id_id'] != 1:
                                return Response({'data': serializer_fuqaro.data, 'fuqaro': 'fuqaro', 'status': 4,
                                                 'status_message': 'uchotga olingan, yana uchotga olish mumkin'},
                                                status=status.HTTP_200_OK)
                            return Response({'data': serializer_fuqaro.data, 'fuqaro': 'fuqaro', 'status': 5,
                                             'status_message': 'uchotga olib bolmaydi'}, status=status.HTTP_200_OK)

                return Response({'message': 'fuqaro id yoq'}, status=status.HTTP_404_NOT_FOUND)


            elif fuqaro_turi_id == '2':
                usmir_uchot = Uchot.objects.filter(usmir_id=human_id)
                if usmir_uchot:
                    serializer_usmir = UchotListSerializer(usmir_uchot, many=True)
                    return Response({'data': serializer_usmir.data, 'fuqaro': 'usmir', 'status': 4,
                                     'status_message': 'uchotga olingan, yana uchotga olish mumkin'},
                                    status=status.HTTP_200_OK)
                return Response({'message': 'usmir id yoq'}, status=status.HTTP_404_NOT_FOUND)

            elif fuqaro_turi_id == '3':
                chetel_uchot = Uchot.objects.filter(chetel_fuqaro_id=human_id)
                if chetel_uchot:
                    serializer_chetl = UchotListSerializer(chetel_uchot, many=True)
                    return Response({'data': serializer_chetl.data, 'fuqaro': 'chet el', 'status': 4,
                                     'status_message': 'uchotga olingan, yana uchotga olish mumkin'},
                                    status=status.HTTP_200_OK)
                return Response({'message': 'chetel id yoq'}, status=status.HTTP_404_NOT_FOUND)

            return Response({'fuqaro': 'yoq'})

''' uchotga olish  '''

class UchotAddApiView(APIView):

    def post(self, request):
        # fuqaro_id = request.query_params['human_id']
        fuqaro_turi_id = request.query_params['fuqaro_turi_id']
        # kucha_id = request.query_params['kucha_id']
        # uchot_turi = request.query_params['uchot_turi']

        try:
            (int(fuqaro_turi_id) and int(fuqaro_turi_id))
            # fuqaro_turi = Fuqarolik_turi.objects.get(

        except Exception  as e:

            return Response({'message': 'parametrlar xato kiritilgan'})

        else:
            return Response({'message': 'bor'})

        # return Response({'message': 'parametrlar xato kiritilgan'})
















# dekarater
# @api_view(['get','POST'])
# def get_one(request):
#     return Response({'message':'one'})
#
#
# @api_view(['delete'])
# def get_two(request):
#     return Response({'message':'1111'})