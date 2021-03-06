from django.urls import path
from .views import *

urlpatterns = [
   path('uchot_id2/', SSUchotApiView.as_view()),  #sinov


    path('uchot_api/', UchotApiView.as_view()),

    path('uchot_api_tekshirish/', UchotTekshirishGet.as_view()),
    path('uchot_turi/', UchotTuriListView.as_view()),
    path('uchot_mahalla/', MahallaOPListView.as_view()),
    path('uchot_tash_yosh/', UchotAgeList.as_view()),


    path('uchot1/', UchotTashkilotApiView1.as_view()),  # uchotga olinganlarni ko'rish
    # path('uchot/', UsmirUchotView.as_view()),
    # path('one/',one),
    # path('fuqaro_search/', FuqaroUchotSearch.as_view()),
    path('uchototchot/', Ruyxatdanutgani.as_view()),


    path('opaholi/', OpAholiKuchaBuyichaList.as_view()),

    path('uchotfilter/', UchotListFilter.as_view()),

    path('uchottashkilot/', UchotTashkilotBuyichaList.as_view()),
    path('uchottuman/', MyPeopleViloyatAllOrm.as_view()),
    path('bruyxatdanutgani/', BruyxatdanutganiList.as_view()),







]
