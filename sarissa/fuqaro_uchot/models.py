from django.db import models
from fuqaro.models import *

# Create your models here.


""" Uchotga olish """

'''o'tgan'''
class UchotTuri(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UchotTuri'
        verbose_name_plural = 'UchotTurlari'

'''o'tgan'''
class Uchot(models.Model):
    status = models.BooleanField(default=True)
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro Id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir Id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro Id', blank=True, null=True)
    tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Tashkilot Id')
    fuqaro_turi_id = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik turi Id')
    kucha_id = models.ForeignKey(Kucha, on_delete=models.PROTECT, verbose_name='Biriktirilgan kucha Id')
    uchot_turi_id = models.ForeignKey(UchotTuri, on_delete=models.PROTECT, verbose_name='Uchot Turi Id')
    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='User Id', related_name='customuserss')
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Uchot'
        verbose_name_plural = 'Uchotdagilar'


'''o'tgan'''
class uchot_takror_shir_fuqaro(models.Model):
    status = models.BooleanField(default=True)
    fuqaro = models.ForeignKey(Fuqaro_Jshir_Takror, on_delete=models.PROTECT, verbose_name='Fuqaro Id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir Id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro Id', blank=True, null=True)
    tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Tashkilot Id')
    fuqaro_turi_id = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik turi Id')
    kucha_id = models.ForeignKey(Kucha, on_delete=models.PROTECT, verbose_name='Biriktirilgan kucha Id')
    uchot_turi_id = models.ForeignKey(UchotTuri, on_delete=models.PROTECT, verbose_name='Uchot Turi Id')
    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='User Id', related_name='+')
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fuqaro_id

    class Meta:
        verbose_name = 'Uchot'
        verbose_name_plural = 'Uchotdagilar'



class UchotChiqarishSababi(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Uchot chiqarish sababi'
        verbose_name_plural = 'Uchot chiqarish sabablari'


class Uchot_chiqarish(models.Model):
    status = models.BooleanField(default=True)
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro Id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir Id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro Id', blank=True, null=True)
    tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Tashkilot Id')
    fuqaro_turi_id = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik turi Id')
    kucha_id = models.ForeignKey(Kucha, on_delete=models.PROTECT, verbose_name='Biriktirilgan kucha Id')
    uchot_turi_id = models.ForeignKey(UchotTuri, on_delete=models.PROTECT, verbose_name='Uchot Turi Id')
    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='User Id', related_name='+')
    qushulgan_sana = models.DateTimeField(blank=True, null=True)
    yangilangan_sana = models.DateTimeField(blank=True, null=True)


    uchotdan_chiqqan_sana = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    uchotdan_chiqargan_user = models.ForeignKey(CustomUser, verbose_name="Kirituvchi", on_delete=models.PROTECT, related_name='+')
    uchotdan_chiqarish_sababi = models.ForeignKey(UchotChiqarishSababi, on_delete=models.PROTECT,
                                                  verbose_name='Uchotdan chiqarish sababi')
    uchotdan_chiqarish_sababi_text = models.CharField(max_length=200, blank=True, null=True)

    # def __str__(self):
    #     return self.fuqaro_id

    class Meta:
        verbose_name = 'Uchotdan chiqarish'
        verbose_name_plural = 'Uchotdan chiqarishlar'
