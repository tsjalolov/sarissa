from django.urls import path
from .views import *

urlpatterns = [
    path('uchot_id/', UchotApiView.as_view()),
    path('uchot_olish/', UchotAddApiView.as_view()),

    path('uchot_turi/', UchotTuriListView.as_view()),
    # path('uchot/', UsmirUchotView.as_view()),
    # path('one/',one),
    path('uchot_filter/', UchotAPIList.as_view()),

    # path('fuqaro_search/', FuqaroUchotSearch.as_view()),

]
