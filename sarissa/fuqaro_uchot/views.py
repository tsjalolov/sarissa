from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, filters

from fuqaro.views import PageSizeControl
from .serializers import *
from fuqaro.views import CustomDjangoModelPermissions

'''
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


 # id yuborganda uchotga olinganligini olib natija qaytaradi 
'''
'''

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


 # uchotga olish  


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



#  name = Firuz
# viloyay = buxor
# dekarater
# @api_view(['get','POST'])
# def get_one(request):
#     return Response({'message':'one'})
#
#
# @api_view(['delete'])
# def get_two(request):
#     return Response({'message':'1111'})

'''
'''

{
    "fuqaro": 32010,
    "usmir": null,
    "chetel_fuqaro": null,
    "fuqaro_turi_id":1,
    "kucha_id": 52,
    "uchot_turi_id":3
} yuqoridagi json keladi uchotga olish tashklilot va user id o'zi oladi'   '''

class UchotApiView(generics.CreateAPIView):
    # def post_func(self, human_id, fuqaro_turi_id):
    #     pass
    queryset = Uchot.objects.all()
    serializer_class = UchotListSerializer
    permission_classes = [CustomDjangoModelPermissions, ]

    #  pagination_class = PageSizeControl

    def frank_func(self, human_uchot, uchot_seriazlizer, tur_id, my_request):
        if len(human_uchot) == 0:
            print(uchot_seriazlizer.is_valid())
            if uchot_seriazlizer.is_valid():
                uchot_seriazlizer.save(
                    # status=my_request.data['status'],
                    tashkilot_id_id=my_request.user.tashkilot_id,
                    add_user_id_id=my_request.user.id
                )
                return Response({'status_message': 'bazag kiritildi 111', 'data': uchot_seriazlizer.data})
            print(uchot_seriazlizer.errors)
            return Response({'errors': uchot_seriazlizer.errors, }, status=status.HTTP_400_BAD_REQUEST)
        elif len(human_uchot) == 1:
            for elem in human_uchot.values():
                if (elem['uchot_turi_id_id'] != 1) and (elem['uchot_turi_id_id'] != tur_id) and (tur_id != 1):
                    if uchot_seriazlizer.is_valid():
                        uchot_seriazlizer.save(
                            tashkilot_id_id=my_request.user.tashkilot_id,
                            add_user_id_id=my_request.user.id
                        )
                        return Response({'data': uchot_seriazlizer.data, 'status': 4,
                                         'status_message': 'uchotga olingan, yana uchotga olish mumkin mmmm'},
                                        status=status.HTTP_200_OK)
                return Response({'status': 5,
                                 'status_message': 'uchotga olib bolmaydi 1'}, status=status.HTTP_200_OK)
            return Response({'message': 'yoq'})

        elif len(human_uchot) > 1:
            return Response({'status_message': 'uchotga olib bolmaydi 2 tadan kup', 'status': 5})
        return Response({'message': 'error 111'})

    def create(self, request, *args, **kwargs):

        uchot_seriazlizer = UchotListSerializer(data=request.data)
        fuqaro_turi_id = request.data['fuqaro_turi_id']

        fuqaro = request.data['fuqaro']
        usmir = request.data['usmir']
        chetel = request.data['chetel_fuqaro']
        human_arr = [fuqaro, usmir, chetel]
        second_arr = []

        for idx, elem in enumerate(human_arr):
            if elem != None:
                second_arr.append(elem)
        if len(second_arr) > 1:
            return Response({'message': '1 > kup'})
        elif len(second_arr) == 0:
            return Response({'message': 'xich kim yuq'})
        else:

            if fuqaro_turi_id == 1 and (request.data['fuqaro'] is not None):
                fuqaro_uchot = Uchot.objects.filter(fuqaro_id=request.data['fuqaro'])
                print('fuqaro')
                return self.frank_func(fuqaro_uchot, uchot_seriazlizer, request.data['uchot_turi_id'], request)

            elif (fuqaro_turi_id == 2) and (request.data['usmir'] is not None):
                usmir_uchot = Uchot.objects.filter(usmir_id=request.data['usmir'])
                print('usmir')
                return self.frank_func(usmir_uchot, uchot_seriazlizer, request.data['uchot_turi_id'], request)

            elif (fuqaro_turi_id == 3) and (request.data['chetel_fuqaro'] is not None):
                chetel_uchot = Uchot.objects.filter(chetel_fuqaro_id=request.data['chetel_fuqaro'])
                print('chetel')
                return self.frank_func(chetel_uchot, uchot_seriazlizer, request.data['uchot_turi_id'], request)

            else:
                return Response({'message': 'error 222'})




'''{
    "fuqaro": 32010,
    "usmir": null,
    "chetel_fuqaro": null,
    "fuqaro_turi_id":1,
    "kucha_id": 52,
    "uchot_turi_id":3
}'''


#    fuqaro_turi yuborilganda shu tashkilotning o'ziga tegishli fuqarolar ro'yxati chiqadi
class UchotTashkilotApiView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Uchot.objects.all()
    serializer_class = UchotListSerializer
    permission_classes = [DjangoModelPermissions, ]
    pagination_class = PageSizeControl

    #
    def uchot_tash_func(self, fuqaro_turi_id, tashkil_turi):
        uchot = Uchot.objects.filter(Q(fuqaro_turi_id=fuqaro_turi_id) & Q(tashkilot_id=tashkil_turi))
        uchut_q = self.paginate_queryset(uchot)
        uchot_serializer = UchotListSerializer(uchut_q, many=True)

        return Response({'message': fuqaro_turi_id, 'data': uchot_serializer.data, 'count': uchot.count()},
                        status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        users = request.user
        if request.query_params and request.query_params['fuqaro_turi']:
            try:
                tur_id = int(request.query_params['fuqaro_turi'])
            except ValueError:
                return Response({'message': 'parametrga xatolik buldi'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if tur_id == 1:
                    return self.uchot_tash_func(1, users.tashkilot_id)
                elif tur_id == 2:
                    return self.uchot_tash_func(2, users.tashkilot_id)
                elif tur_id == 3:
                    return self.uchot_tash_func(3, users.tashkilot_id)
                else:
                    return Response({'message': 'parametr mavjud emas'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            fuqaro = Uchot.objects.filter(Q(fuqaro_turi_id=1) & Q(tashkilot_id=users.tashkilot_id)).count()
            usmir = Uchot.objects.filter(Q(fuqaro_turi_id=2) & Q(tashkilot_id=users.tashkilot_id)).count()
            chetel = Uchot.objects.filter(Q(fuqaro_turi_id=3) & Q(tashkilot_id=users.tashkilot_id)).count()
            return Response({
                'message': 'parametr yoq',
                'fuqaro': fuqaro,
                'usmir': usmir,
                'chet el': chetel
            }, status=status.HTTP_200_OK)



