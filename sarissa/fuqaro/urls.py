from django.urls import path
from .views import *

urlpatterns = [
    # path('',index),
    # path('',second_index),
    path('davlat/', DavlatListView.as_view()),  # manzil
    path('viloyat/', ViloyatListView.as_view()),  # manzil
    path('tuman/', TumanListView.as_view()),  # manzil
    path('mahalla/', MahallaListView.as_view()),  # manzil
    path('kucha/', KuchaListView.as_view()),  # manzil

    path('boshqa_manzil/', BoshqaManzilListView.as_view()),  # boshqaManzil

    path('jins/', JinsListView.as_view()),  # jins

    path('millat/', MillatListView.as_view()),  # millat

    path('fuqaro/', FuqaroListView.as_view()),  # fuqaro
    path('fuqarolik_turi/', FuqarolikTuriListView.as_view()),  # fuqaro_tur

    path('usmir/', UsmirListView.as_view()),  # usmir

    path('chet_el_fuqaro/', ChetElFuqarosiListView.as_view()),  # ChetEl_Fuqaro

    path('mkb10/', mkb10ListView.as_view()),  # mkb10

    path('tashkilot_tur/', TashkilotTurListView.as_view()),  # tashkilot_tur
    path('tashkilot/', TashkilotListView.as_view()),  # tashkilotlar
    path('tashkilot_qushimcha_malumot/', TashkilotQushimchaMalumotListView.as_view()),  # tashkilotlar_Qushimcha_Malumot
    path('tashkilot_tel/', TashkilotTelListView.as_view()),  # tashkilot_tel

    path('mahalla_op/', MahallaOPListView.as_view()),

]