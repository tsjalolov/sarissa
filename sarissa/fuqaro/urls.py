from django.urls import path
from .views import *

urlpatterns = [
    # path('',index),
    # path('',second_index),
    path('davlat/', DavlatListView.as_view()),  # manzil davlat  №1
    path('viloyat/', ViloyatListView.as_view()),   # manzil viloyat  №2
    path('tuman/', TumanListView.as_view()),  # manzil tuman №3
    path('tumandavlat/', TumanDavlatBilanListView.as_view()),  # manzil tuman №3
    path('mahalla/', MahallaListView.as_view()),  # manzil mahalla №4
    path('kucha/', KuchaListView.as_view()),  # manzil kucha  №5

    path('boshqa_manzil/', BoshqaManzilListView.as_view()),  # manzil boshqa manzil  №6

    path('jins/', JinsListView.as_view()),  # jins          # jins  №7

    path('millat/', MillatListView.as_view()),  # millat      # millat  №8

    path('fuqarolik_turi/', FuqarolikTuriListView.as_view()),  # fuqaro_tur №9

    path('FuqaroAlohidaList/', FuqaroAlohidaListView.as_view()),  # fuqaro_tur №9

    path('fuqaro/', FuqaroListView.as_view()),  # fuqaro       # fuqaro №10
    path('fuqarocreate/', FuqaroCreate.as_view()),  # fuqaro       # fuqaro №10


    path('usmir/', UsmirListView.as_view()),  # usmir            # usmir   №11

    # path('chet_el_fuqaro/', ChetElFuqarosiListView.as_view()),  # ChetEl_Fuqaro

    path('mkb10/', mkb10ListView.as_view()),  # mkb10

    path('tashkilot_tur/', TashkilotTurListView.as_view()),  # tashkilot_tur
    path('tashkilot/', TashkilotListView.as_view()),  # tashkilotlar
    path('tashkilot_qushimcha_malumot/', TashkilotQushimchaMalumotListView.as_view()),  # tashkilotlar_Qushimcha_Malumot
    path('tashkilot_tel/', TashkilotTelListView.as_view()),  # tashkilot_tel

    path('uchot_tash_yosh/', MahallaOpTumanListView.as_view()),   #tanlash uchun   op ga mahalla qo'shish uchun o'zinng tumanining mahallalarini chiqarish
    path('mahalla_op_add/', MahallaOpPsotListView.as_view()),   #  qo'shish uchun
    path('mahalla_op/', MahallaOPListView.as_view()),   #  o'ziga biriktirilgan mahallalar ro'yxati
    path('mahalla_op_del/<int:pk>/', MahallaOPDeletePost.as_view()),    # o'ziga biriktirilgan mahallalardan birini o'chirish


]