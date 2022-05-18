from django.db import models
from fuqaro.models import *
from helper_app.models import *

from django.utils import timezone


# Create your models here.
'''o'tgan'''
class Asosiy(models.Model):
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro id', blank=True, null=True)
    oilaviy_sharoiti = models.ForeignKey(OilaviySharoiti, on_delete=models.PROTECT, verbose_name='Oilaviy Sharoiti')
    farzandlari_soni = models.SmallIntegerField(blank=True, null=True)
    tirikchilik_manbasi = models.ForeignKey(TirikchilikManbasi, on_delete=models.PROTECT,
                                            verbose_name='Tirikchilik Manbasi')
    ish_joyi = models.CharField(max_length=200, verbose_name='Ish Joyi', blank=True, null=True)
    malumoti_id = models.ForeignKey(Malumoti, on_delete=models.PROTECT, verbose_name='Ma`lumoti', blank=True, null=True)
    tashxis_sana = models.DateField(verbose_name='Tashxis Sana', blank=True, null=True)
    nogironlik_id = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironlik ID')
    dispanser_holati = models.BooleanField(default=False, verbose_name='Dispanser Holati')
    kasallik_bosh_sana = models.DateField(verbose_name='Kasallik Boshlangan Sana', blank=True, null=True)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana')
    jamoatga_xavf = models.BooleanField(default=False, verbose_name='Jamoatga xavf')
    jamoatga_xavf_text = models.TextField(max_length=5000, verbose_name='Jamoatga xavf Text', blank=True, null=True)
    shifoxonaga_yotish_soni = models.SmallIntegerField(verbose_name='Shifoxonaga yotish soni', blank=True, null=True)
    majburiy_davo_shifoxonasi = models.SmallIntegerField(verbose_name='Majburiy davo shifoxonasi', blank=True,
                                                         null=True)
    hisobga_olish_kim_yuborgan = models.CharField(max_length=200, verbose_name='Hisobga olish kim yuborgan', blank=True,
                                                  null=True)
    tashxis_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, verbose_name='Tashxis mkb10 ID')
    tashxis_mkb10_text = models.CharField(max_length=30, verbose_name='Tashxis mkb10 ID')
    holati = models.BooleanField(default=True, verbose_name='Holati')
    # hisobdan_chiqarish_sana = models.DateField(verbose_name='Hisobdan chiqarilgan sana', blank=True, null=True)
    # hisobdan_chiqarish_sababi_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+',
    #                                                  verbose_name='Hisobdan chiqarilgan sababi mkb10', blank=True,
    #                                                  null=True)
    # hisobdan_chiqarishgan_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT,related_name='customuser',
    #                                                verbose_name='Hisobdan chiqarilgan user ID', blank=True, null=True)
    nechanchi_sinf_uqigan = models.SmallIntegerField(verbose_name='Nechanchi sinf o`qigan', blank=True, null=True)
    uqiydi_id = models.BooleanField(default=False)
    fuqarolik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    tuman_id = models.ForeignKey(Tuman, on_delete=models.PROTECT, verbose_name='Tuman ID')
    dinamik_kuzatuv_guruhi = models.ForeignKey(DinamikKuzatuvchiGuruh, on_delete=models.PROTECT,
                                               verbose_name='Dinamik Kuzatuvchi guruh', blank=True, null=True)
    add_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Kirituvchi', related_name='+')
    add_tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Kirituvchi Tashkilot')
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.fuqari_id

    class Meta:
        verbose_name = 'Asosiy'
        verbose_name_plural = 'Asosiy'


class Shir_takror_psix(models.Model):
    #  takror kiritilgan fuqarolar
    fuqaro_id = models.IntegerField(verbose_name='Fuqaro id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro id', blank=True, null=True)
    oilaviy_sharoiti = models.ForeignKey(OilaviySharoiti, on_delete=models.PROTECT, verbose_name='Oilaviy Sharoiti')
    farzandlari_soni = models.SmallIntegerField(blank=True, null=True)
    tirikchilik_manbasi = models.ForeignKey(TirikchilikManbasi, on_delete=models.PROTECT,
                                            verbose_name='Tirikchilik Manbasi')
    ish_joyi = models.CharField(max_length=200, verbose_name='Ish Joyi', blank=True, null=True)
    malumoti = models.ForeignKey(Malumoti, on_delete=models.PROTECT, verbose_name='Ma`lumoti', blank=True, null=True)
    tashxis_sana = models.DateField(verbose_name='Tashxis Sana', blank=True, null=True)
    nogironlik = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironlik ID')
    dispanser_holati = models.BooleanField(default=False, verbose_name='Dispanser Holati')
    kasallik_bosh_sana = models.DateField(verbose_name='Kasallik Boshlangan Sana', blank=True, null=True)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana')
    jamoatga_xavf = models.BooleanField(default=False, verbose_name='Jamoatga xavf')
    jamoatga_xavf_text = models.TextField(max_length=5000, verbose_name='Jamoatga xavf Text', blank=True, null=True)
    shifoxonaga_yotish_soni = models.SmallIntegerField(verbose_name='Shifoxonaga yotish soni', blank=True, null=True)
    majburiy_davo_shifoxonasi = models.SmallIntegerField(verbose_name='Majburiy davo shifoxonasi', blank=True,
                                                         null=True)
    hisobga_olish_kim_yuborgan = models.CharField(max_length=200, verbose_name='Hisobga olish kim yuborgan', blank=True,
                                                  null=True)
    tashxis_mkb10 = models.ForeignKey(mkb10, on_delete=models.PROTECT, verbose_name='Tashxis mkb10 ID', blank=True, null=True)
    tashxis_mkb10_text = models.CharField(max_length=30, verbose_name='Tashxis mkb10 ID')
    holati = models.BooleanField(default=True, verbose_name='Holati')
    hisobdan_chiqarish_sana = models.DateField(verbose_name='Hisobdan chiqarilgan sana', blank=True, null=True)
    hisobdan_chiqarish_sababi = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+',
                                                     verbose_name='Hisobdan chiqarilgan sababi mkb10', blank=True,
                                                     null=True)
    hisobdan_chiqarishgan_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT,related_name='+',
                                                   verbose_name='Hisobdan chiqarilgan user ID', blank=True, null=True)
    nechanchi_sinf_uqigan = models.SmallIntegerField(verbose_name='Nechanchi sinf o`qigan', blank=True, null=True)
    uqiydi = models.BooleanField(default=False)
    fuqarolik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    tuman = models.ForeignKey(Tuman, on_delete=models.PROTECT, verbose_name='Tuman ID')
    dinamik_kuzatuv_guruhi = models.ForeignKey(DinamikKuzatuvchiGuruh, on_delete=models.PROTECT,
                                               verbose_name='Dinamik Kuzatuvchi guruh', blank=True, null=True)
    add_tashkilot_id = models.IntegerField(verbose_name='Kirituvchi Tashkilot')
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.fuqari_id

    class Meta:
        verbose_name = 'Asosiy'
        verbose_name_plural = 'Asosiy'

'''bunda ma'lumot yo'q'''
class ShifoxonagaYotkazish(models.Model):
    fuqari_id = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro id')
    qayd_raqami = models.IntegerField(verbose_name='Qayd raqami')
    kelgan_sana = models.DateField(verbose_name='Kelgan Sanasi')
    ketgan_sana = models.DateField(verbose_name='Ketgan Sanasi')
    tashxis_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, verbose_name='Tashxis mkb10 ID')
    qushilgan_sana = models.DateField(auto_now_add=True, verbose_name='Qushilgan Sana')
    qushgan_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Kirituvchi', related_name='+')

    def __str__(self):
        return self.fuqari_id

    class Meta:
        verbose_name = 'Shifoxonaga Yotkazish'
        verbose_name_plural = 'Shifoxonaga Yotkazishlar'

'''o'tgan'''
class TashkilotPisxEndoQushimcha(models.Model):
    fuqarolari_soni = models.PositiveSmallIntegerField(verbose_name='Fuqarolari soni')
    tashkilot_p_endo_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Tashkilot nomi')
    qandli_diabet_1_tur = models.PositiveSmallIntegerField(verbose_name='qandli diabet 1-tur')
    qandli_diabet_2_tur = models.PositiveSmallIntegerField(verbose_name='qandli diabet 2-tur')
    qandsiz_diabet = models.PositiveSmallIntegerField(verbose_name='qandsiz diabet')
    gipotireoz = models.PositiveSmallIntegerField(verbose_name='gipotireoz')
    diffuz_toksik_buqoq = models.PositiveSmallIntegerField(verbose_name='diffuz toksik buqoq')
    tugunli_buqoq = models.PositiveSmallIntegerField(verbose_name='tugunli buqoq')
    somatotrop_yetishmovchilik = models.PositiveSmallIntegerField(verbose_name='somatotrop yetishmovchilik')
    jinsiy_balogatga_kechikish = models.PositiveSmallIntegerField(verbose_name='jinsiy balogatga kechikish')
    akromegaliya = models.PositiveSmallIntegerField(verbose_name='akromegaliya')
    semizlik = models.PositiveSmallIntegerField(verbose_name='semizlik')
    boshqa = models.PositiveSmallIntegerField(verbose_name='boshqa')

    def __str__(self):
        return self.fuqarolari_soni

    class Meta:
        verbose_name = "Tashkilotning qo'shimcha ma'lumotlari"
        verbose_name_plural = "Tashkilotlarning qo'shimcha ma'lumotlari"


class Asosiy_psix_uchot_chiqarish(models.Model):
    fuqaro = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name='Fuqaro id', blank=True, null=True)
    usmir = models.ForeignKey(Usmir, on_delete=models.PROTECT, verbose_name='usmir id', blank=True, null=True)
    chetel_fuqaro = models.ForeignKey(ChetElFuqarosi, on_delete=models.PROTECT, verbose_name='chetel fuqaro id',
                                      blank=True, null=True)
    oilaviy_sharoiti = models.ForeignKey(OilaviySharoiti, on_delete=models.PROTECT, verbose_name='Oilaviy Sharoiti')
    farzandlari_soni = models.SmallIntegerField(blank=True, null=True)
    tirikchilik_manbasi = models.ForeignKey(TirikchilikManbasi, on_delete=models.PROTECT,
                                            verbose_name='Tirikchilik Manbasi')
    ish_joyi = models.CharField(max_length=200, verbose_name='Ish Joyi', blank=True, null=True)
    malumoti_id = models.ForeignKey(Malumoti, on_delete=models.PROTECT, verbose_name='Ma`lumoti', blank=True, null=True)
    tashxis_sana = models.DateField(verbose_name='Tashxis Sana', blank=True, null=True)
    nogironlik_id = models.ForeignKey(Nogironlik, on_delete=models.PROTECT, verbose_name='Nogironlik ID')
    dispanser_holati = models.BooleanField(default=False, verbose_name='Dispanser Holati')
    kasallik_bosh_sana = models.DateField(verbose_name='Kasallik Boshlangan Sana', blank=True, null=True)
    d_nazoratga_olingan_sana = models.DateField(verbose_name='Dinamik nazoratga olingan sana')
    jamoatga_xavf = models.BooleanField(default=False, verbose_name='Jamoatga xavf')
    jamoatga_xavf_text = models.TextField(max_length=5000, verbose_name='Jamoatga xavf Text', blank=True, null=True)
    shifoxonaga_yotish_soni = models.SmallIntegerField(verbose_name='Shifoxonaga yotish soni', blank=True, null=True)
    majburiy_davo_shifoxonasi = models.SmallIntegerField(verbose_name='Majburiy davo shifoxonasi', blank=True,
                                                         null=True)
    hisobga_olish_kim_yuborgan = models.CharField(max_length=200, verbose_name='Hisobga olish kim yuborgan', blank=True,
                                                  null=True)
    tashxis_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, verbose_name='Tashxis mkb10 ID')
    tashxis_mkb10_text = models.CharField(max_length=30, verbose_name='Tashxis mkb10 ID')
    holati = models.BooleanField(default=True, verbose_name='Holati')
    # hisobdan_chiqarish_sana = models.DateField(verbose_name='Hisobdan chiqarilgan sana', blank=True, null=True)
    # hisobdan_chiqarishgan_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='+',
    #                                                verbose_name='Hisobdan chiqarilgan user ID', blank=True, null=True)
    nechanchi_sinf_uqigan = models.SmallIntegerField(verbose_name='Nechanchi sinf o`qigan', blank=True, null=True)
    uqiydi_id = models.BooleanField(default=False)
    fuqarolik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT, verbose_name='Fuqarolik Turi')
    tuman_id = models.ForeignKey(Tuman, on_delete=models.PROTECT, verbose_name='Tuman ID')
    dinamik_kuzatuv_guruhi = models.ForeignKey(DinamikKuzatuvchiGuruh, on_delete=models.PROTECT,
                                               verbose_name='Dinamik Kuzatuvchi guruh', blank=True, null=True)
    add_user_id = models.IntegerField(verbose_name='Kirituvchi', default=1)
    add_tashkilot_id = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Kirituvchi Tashkilot')
    qushulgan_sana = models.DateTimeField(blank=True, null=True)
    yangilangan_sana = models.DateTimeField(blank=True, null=True)
    ''' yuqorisi to'liq ko'chadi '''


    uchotdan_chiqqan_sana = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    uchotdan_chiqargan_user = models.ForeignKey(CustomUser, verbose_name="Kirituvchi", on_delete=models.PROTECT, related_name='+')
    uchotdan_chiqarish_sababi = models.ForeignKey(UchotChiqarishSababi, on_delete=models.PROTECT,
                                                  verbose_name='Uchotdan chiqarish sababi')
    uchotdan_chiqarish_sababi_text = models.CharField(max_length=200, blank=True, null=True)
    uchotdan_chiqarish_sababi_mkb10_id = models.ForeignKey(mkb10, on_delete=models.PROTECT, related_name='+',
                                                     verbose_name='Hisobdan chiqarilgan sababi mkb10')

    # def __str__(self):
    #     return self.fuqari_id

    class Meta:
        verbose_name = 'Asosiy_psix_uchot_chiqarish'
        verbose_name_plural = 'Asosiy_psix_uchot_chiqarishlar'

