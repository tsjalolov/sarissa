from django.urls import path
from .views import *

urlpatterns = [
    path('uchot_id/', UchotApiView.as_view()),

    path('uchot_turi/', UchotTashkilotApiView.as_view()),
    # path('uchot/', UsmirUchotView.as_view()),
    # path('one/',one),


    # path('fuqaro_search/', FuqaroUchotSearch.as_view()),

]
