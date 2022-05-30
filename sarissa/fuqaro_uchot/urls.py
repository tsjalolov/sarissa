from django.urls import path
from .views import *

urlpatterns = [
    path('uchot_id/', FuqaroUchotApi.as_view()),
    path('uchot_api/', UchotApiView.as_view()),

    path('uchot/', UchotTashkilotApiView.as_view()),  # uchotga olinganlarni ko'rish
    # path('uchot/', UsmirUchotView.as_view()),
    # path('one/',one),
    # path('fuqaro_search/', FuqaroUchotSearch.as_view()),

]
