from django.db import models
from fuqaro.models import *

class Ulim(models.Model):
    # name = models.CharField(max_length=100)
    # status = models.BooleanField(default=True)
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro Id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir Id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro Id',
                                      blank=True, null=True)
    fuqaro_turi_id = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik turi Id')
    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='User Id')
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    uchotdan_chiqarish_sababi_text = models.CharField(max_length=250, blank=True, null=True)
    uchotdan_chiqarish_sababi_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT,
                                                           verbose_name='Hisobdan chiqarilgan sababi mkb10')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UchotTuri'
        verbose_name_plural = 'UchotTurlari'