from django.db import models
from fuqaro.models import *
from helper_app.models import *


# Create your models here.

'''o'tgan'''
class QandliDiabetRuyxat(models.Model):
    fuqaro_lik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro ID', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='Fuqaro ID', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='Chet el fuqarosi ID', blank=True, null=True)
    coviddan_keyin_kelib_chiqishi = models.BooleanField(default=False)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana')
    qandli_diabet_boshlangan_sana = models.DateField(verbose_name='Qandli diabet boshlangan sana', blank=True,
                                                     null=True)
    insulin_terapiya_boshlangan_sana = models.DateField(verbose_name='Insulin terapiya boshlangan sana', blank=True,
                                                        null=True)
    insulin_miqdori_h = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_r = models.DecimalField(verbose_name='Insulin miqdori r', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_30_70 = models.DecimalField(verbose_name='Insulin miqdori 30_70', max_digits=15, decimal_places=2,
                                                blank=True, null=True)
    analog_insulin_h = models.DecimalField(verbose_name='Analog Insulin h', max_digits=15, decimal_places=2, blank=True,
                                           null=True)
    analog_insulin_r = models.DecimalField(verbose_name='Analog Insulin r', max_digits=15, decimal_places=2, blank=True,
                                           null=True)
    tabletka_biguanid = models.DecimalField(verbose_name='Tabletka biguanid', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    tabletka_glibenklamid = models.DecimalField(verbose_name='Tabletka glibenklamid', max_digits=15, decimal_places=2,
                                                blank=True, null=True)
    tabletka_glimepirid = models.DecimalField(verbose_name='Tabletka glimepirid', max_digits=15, decimal_places=2,
                                              blank=True, null=True)
    tabletka_gliklazid = models.DecimalField(verbose_name='Tabletka gliklazid', max_digits=15, decimal_places=2,
                                             blank=True, null=True)
    tabletka_tiozolidindion = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=15, decimal_places=2,
                                                  blank=True, null=True)
    tabletka_boshqa_nomi = models.CharField(max_length=200, verbose_name='Boshqa Tabletka nomi', blank=True, null=True)
    ijtimoiy_holat = models.ForeignKey(IjtimoiyHolat, on_delete=models.PROTECT, verbose_name='Ijtimoiy Holat')
    nogironligi = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironligi')
    buyi = models.DecimalField(verbose_name='Bo`yi', max_digits=6, decimal_places=2)
    vazni = models.DecimalField(verbose_name='Vazni', max_digits=6, decimal_places=2)
    bel_aylanasi = models.DecimalField(verbose_name='Bel Aylanasi', max_digits=6, decimal_places=2)
    qon_bosimi_yuqori = models.DecimalField(verbose_name='Qon Bosimi Yuqori', blank=True, null=True, max_digits=6, decimal_places=2)
    qon_bosimi_quyi = models.DecimalField(verbose_name='Qon Bosimi Quyi', max_digits=6, decimal_places=2, blank=True, null=True)
    qushimcha_qabul_qiladigan_dorilari = models.TextField(max_length=1000,
                                                          verbose_name='Qushimcha qabul qiladigan dorilari', blank=True,
                                                          null=True)
    holati = models.BooleanField(default=True, verbose_name='Holati')
    tuman_id = models.ForeignKey(Tuman, verbose_name='Tuman ID', on_delete=models.PROTECT)
    endokrinologik_tashxis_mkb10 = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='mkb10_q',verbose_name='Endokrinologik tashxisi')  # bitta kasallik bilan 2 marta uchotga olib bo'lmaydi bunda fuq id va mkb10 id tekshiriladi
    endokrinologik_tashxis_mkb10_text = models.CharField(max_length=30, verbose_name='Endokrinologik tashxisi yozuv', blank=True, null=True)  # bitta kasallik bilan 2 marta uchotga olib bo'lmaydi bunda fuq id va mkb10 id tekshiriladi
    asoratlar_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+', verbose_name='Asoratlar', blank=True, null=True)
    asoratlar_mkb10_text = models.CharField(max_length=30, verbose_name='Asoratlar', blank=True, null=True)
    hamroh_kaslliklar = models.CharField(max_length=30, verbose_name='Hamroh kasalliklar', blank=True, null=True)

    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Kirituvchi', related_name='customusers')
    add_tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Kirituvchi Tashkilot')
    qushilgan_sana = models.DateTimeField(verbose_name='Qushilgan sana', auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fuqaro_id

    class Meta:
        verbose_name = 'Qandli Diabet Ruyxat'
        verbose_name_plural = 'Qandli Diabet Ruyxatlari'

'''o'tgan'''
class Qandli_diabet_ruyxat_shir_takror(models.Model):
    fuqarolik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    fuqaro_id = models.IntegerField()
    coviddan_keyin_kelib_chiqqan = models.BooleanField(default=False)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana')
    qandli_diabet_boshlangan_sana = models.DateField(verbose_name='Qandli diabet boshlangan sana', blank=True,
                                                     null=True)
    insulin_terapiya_boshlangan_sana = models.DateField(verbose_name='Insulin terapiya boshlangan sana', blank=True,
                                                        null=True)
    insulin_miqdori_h = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=20, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_r = models.DecimalField(verbose_name='Insulin miqdori r', max_digits=20, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_30_70 = models.DecimalField(verbose_name='Insulin miqdori 30_70', max_digits=20, decimal_places=2,
                                                blank=True, null=True)
    analog_insulin_h = models.DecimalField(verbose_name='Analog Insulin h', max_digits=20, decimal_places=2, blank=True,
                                           null=True)
    analog_insulin_r = models.DecimalField(verbose_name='Analog Insulin r', max_digits=20, decimal_places=2, blank=True,
                                           null=True)
    tabletka_biguanid = models.DecimalField(verbose_name='Tabletka biguanid',max_digits=20, decimal_places=2,
                                            blank=True, null=True)
    tabletka_glibenklamid = models.DecimalField(verbose_name='Tabletka glibenklamid', max_digits=20, decimal_places=2,
                                                blank=True, null=True)
    tabletka_glimepirid = models.DecimalField(verbose_name='Tabletka glimepirid', max_digits=20, decimal_places=2,
                                              blank=True, null=True)
    tabletka_gliklazid = models.DecimalField(verbose_name='Tabletka gliklazid', max_digits=20, decimal_places=2,
                                             blank=True, null=True)
    tabletka_tiozolidindion = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=20, decimal_places=2,
                                                  blank=True, null=True)
    tabletka_boshqa_nomi_dozasi = models.CharField(max_length=200, verbose_name='Boshqa Tabletka nomi', blank=True, null=True)
    ijtimoiy_holati = models.ForeignKey(IjtimoiyHolat, on_delete=models.PROTECT, verbose_name='Ijtimoiy Holat')
    nogironligi = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironligi')
    buyi = models.DecimalField(verbose_name='Bo`yi', max_digits=20, decimal_places=2)
    vazni = models.DecimalField(verbose_name='Vazni', max_digits=20, decimal_places=2)
    bel_aylanasi = models.DecimalField(verbose_name='Bel Aylanasi', max_digits=20, decimal_places=2)
    qon_bosimi_yuqori = models.DecimalField(verbose_name='Qon Bosimi Yuqori', blank=True, null=True, max_digits=20, decimal_places=2)
    qon_bosimi_quyi = models.DecimalField(verbose_name='Qon Bosimi Quyi', blank=True, null=True, max_digits=20, decimal_places=2)
    qushimcha_qabul_qiladigan_dorilar = models.TextField(max_length=1000,
                                                          verbose_name='Qushimcha qabul qiladigan dorilari', blank=True,
                                                          null=True)
    holati = models.BooleanField(default=True, verbose_name='Holati')
    tuman = models.ForeignKey(Tuman, verbose_name='Tuman ID', on_delete=models.PROTECT)
    endokrinologik_tashxis_mkb10 = models.CharField(max_length=30, verbose_name='Endokrinologik tashxisi yozuv', blank=True, null=True)  # bitta kasallik bilan 2 marta uchotga olib bo'lmaydi bunda fuq id va mkb10 id tekshiriladi
    asoratlar = models.CharField(max_length=30, verbose_name='Asoratlar', blank=True, null=True)
    hamroh_kasalliklar = models.CharField(max_length=30, verbose_name='Hamroh kasalliklar', blank=True, null=True)

    qushgan_user = models.IntegerField(verbose_name='Kirituvchi Tashkilot')
    qushilgan_sana = models.DateTimeField(verbose_name='Qushilgan sana', auto_now_add=True)

    # def __str__(self):
    #     return self.fuqaro_id

    class Meta:
        verbose_name = 'Qandli Diabet Ruyxat'
        verbose_name_plural = 'Qandli Diabet Ruyxatlari'


class QandliDiabetRuyxat_chiqarish(models.Model):
    fuqaro_lik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro ID', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='Fuqaro ID', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='Chet el fuqarosi ID', blank=True, null=True)
    coviddan_keyin_kelib_chiqishi = models.BooleanField(default=False)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana', blank=True, null=True )
    qandli_diabet_boshlangan_sana = models.DateField(verbose_name='Qandli diabet boshlangan sana', blank=True,
                                                     null=True)
    insulin_terapiya_boshlangan_sana = models.DateField(verbose_name='Insulin terapiya boshlangan sana', blank=True,
                                                        null=True)
    insulin_miqdori_h = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_r = models.DecimalField(verbose_name='Insulin miqdori r', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    insulin_miqdori_30_70 = models.DecimalField(verbose_name='Insulin miqdori 30_70', max_digits=15, decimal_places=2,
                                                blank=True, null=True)
    analog_insulin_h = models.DecimalField(verbose_name='Analog Insulin h', max_digits=15, decimal_places=2, blank=True,
                                           null=True)
    analog_insulin_r = models.DecimalField(verbose_name='Analog Insulin r', max_digits=15, decimal_places=2, blank=True,
                                           null=True)
    tabletka_biguanid = models.DecimalField(verbose_name='Tabletka biguanid', max_digits=15, decimal_places=2,
                                            blank=True, null=True)
    tabletka_glibenklamid = models.DecimalField(verbose_name='Tabletka glibenklamid', max_digits=15, decimal_places=2,
                                                blank=True, null=True)
    tabletka_glimepirid = models.DecimalField(verbose_name='Tabletka glimepirid', max_digits=15, decimal_places=2,
                                              blank=True, null=True)
    tabletka_gliklazid = models.DecimalField(verbose_name='Tabletka gliklazid', max_digits=15, decimal_places=2,
                                             blank=True, null=True)
    tabletka_tiozolidindion = models.DecimalField(verbose_name='Insulin miqdori h', max_digits=15, decimal_places=2,
                                                  blank=True, null=True)
    tabletka_boshqa_nomi = models.CharField(max_length=200, verbose_name='Boshqa Tabletka nomi', blank=True, null=True)
    ijtimoiy_holat = models.ForeignKey(IjtimoiyHolat, on_delete=models.PROTECT, verbose_name='Ijtimoiy Holat')
    nogironligi = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironligi')
    buyi = models.DecimalField(verbose_name='Bo`yi', max_digits=6, decimal_places=2)
    vazni = models.DecimalField(verbose_name='Vazni', max_digits=6, decimal_places=2)
    bel_aylanasi = models.DecimalField(verbose_name='Bel Aylanasi', max_digits=6, decimal_places=2)
    qon_bosimi_yuqori = models.DecimalField(verbose_name='Qon Bosimi Yuqori', blank=True, null=True, max_digits=6, decimal_places=2)
    qon_bosimi_quyi = models.DecimalField(verbose_name='Qon Bosimi Quyi', max_digits=6, decimal_places=2, blank=True, null=True)
    qushimcha_qabul_qiladigan_dorilari = models.TextField(max_length=1000,
                                                          verbose_name='Qushimcha qabul qiladigan dorilari', blank=True,
                                                          null=True)
    holati = models.BooleanField(default=True, verbose_name='Holati')
    tuman_id = models.ForeignKey(Tuman, verbose_name='Tuman ID', on_delete=models.PROTECT)
    endokrinologik_tashxis_mkb10 = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+',verbose_name='Endokrinologik tashxisi')  # bitta kasallik bilan 2 marta uchotga olib bo'lmaydi bunda fuq id va mkb10 id tekshiriladi
    endokrinologik_tashxis_mkb10_text = models.CharField(max_length=30, verbose_name='Endokrinologik tashxisi yozuv', blank=True, null=True)  # bitta kasallik bilan 2 marta uchotga olib bo'lmaydi bunda fuq id va mkb10 id tekshiriladi
    asoratlar_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+', verbose_name='Asoratlar', blank=True, null=True)
    asoratlar_mkb10_text = models.CharField(max_length=30, verbose_name='Asoratlar', blank=True, null=True)
    hamroh_kaslliklar = models.CharField(max_length=30, verbose_name='Hamroh kasalliklar', blank=True, null=True)

    add_user_id = models.IntegerField(verbose_name='Oldin Kirituvchi', default=1)
    add_tashkilot_id = models.IntegerField(verbose_name='Kirituvchi Tashkilot')
    qushilgan_sana = models.DateTimeField(blank=True, null=True)
    yangilangan_sana = models.DateTimeField(blank=True, null=True)

    ''' yuqorisi to'liq ko'chadi '''

    uchotdan_chiqqan_sana = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    uchotdan_chiqargan_user = models.ForeignKey(CustomUser, verbose_name="Kirituvchi", on_delete=models.PROTECT, related_name='+')
    uchotdan_chiqarish_sababi = models.ForeignKey(UchotChiqarishSababi, on_delete=models.PROTECT,
                                                  verbose_name='Uchotdan chiqarish sababi', related_query_name='UchotChiqarishSababi')
    uchotdan_chiqarish_sababi_text = models.CharField(max_length=200, blank=True, null=True)
    uchotdan_chiqarish_sababimkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+',
                                                     verbose_name='Hisobdan chiqarilgan sababi mkb10')

    def __str__(self):
        return self.fuqaro_id

    class Meta:
        verbose_name = 'Qandli Diabet Ruyxatdan chiqarish'
        verbose_name_plural = 'Qandli Diabet Ruyxatdan chiqarish'



