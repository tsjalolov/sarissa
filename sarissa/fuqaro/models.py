from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

'''o'tgan'''
class Davlat(models.Model):
    """Davlat"""
    name = models.CharField(verbose_name="Davlat", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        # order_with_respect_to = 'name'
        ordering = ['name']
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"

'''o'tgan'''
class Viloyat(models.Model):
    """Viloyat"""
    name = models.CharField("Viloyat", max_length=60)
    davlat = models.ForeignKey(Davlat, verbose_name="davlat", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"

'''o'tgan'''
class Tuman(models.Model):
    """Tuman"""
    name = models.CharField("Tuman", max_length=60)
    viloyat_id = models.ForeignKey(Viloyat, verbose_name="viloyat", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"

'''o'tgan'''
class Mahalla(models.Model):
    """Mahalla"""
    ordering = ['name']
    name = models.CharField("Mahalla", max_length=60)
    tuman_id = models.ForeignKey(Tuman, verbose_name="tuman", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahallalar"

'''o'tgan'''
class Kucha(models.Model):
    """ Kucha """
    ordering = ['name']
    name = models.CharField("Kucha", max_length=60)
    mahalla_id = models.ForeignKey(Mahalla, verbose_name="mahalla", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kucha"
        verbose_name_plural = "Kuchalar"

'''o'tgan'''
class Millat(models.Model):
    """ Millat """
    name = models.CharField(verbose_name="Millati", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Millat"
        verbose_name_plural = "Millatlar"

'''o'tgan'''
class Jins(models.Model):
    """ Jins """
    name = models.CharField(verbose_name="Jinsi", max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Jins"
        verbose_name_plural = "Jinslar"


class Holat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Holati')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Holat'
        verbose_name_plural = 'Holatlar'

'''o'tgan'''
class Fuqarolik_turi(models.Model):
    name = models.CharField(verbose_name="Fuqarolik turi", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Fuqarolik turi'
        verbose_name_plural = 'Fuqarolik turlari'


'''o'tgan'''
class Fuqaro(models.Model):
    """ Fuqaro """
    jshir = models.BigIntegerField(verbose_name="JSHIR", validators=[MaxValueValidator(99999999999999),
                                                                     MinValueValidator(10000000000000)], unique=True)
    familiya = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    sharif = models.CharField(max_length=30)
    tug_sana = models.DateField()
    tug_joy_davlat_id = models.ForeignKey(Davlat, verbose_name="Tug'ulgan davlati", on_delete=models.PROTECT)
    tug_joy_tuman_id = models.ForeignKey(Tuman, verbose_name="Tug'ulgan tumani", related_name='+',
                                         on_delete=models.PROTECT)
    millat_id = models.ForeignKey(Millat, verbose_name="Millat", on_delete=models.PROTECT)
    pass_kim_bergan_tuman_id = models.ForeignKey(Tuman, verbose_name="Passport bergan tuman", related_name='+',
                                                 on_delete=models.PROTECT)
    jins = models.ForeignKey(Jins, verbose_name="Jinsi", on_delete=models.PROTECT)
    pass_seriya = models.CharField(max_length=2, verbose_name="Passport seriyasi")
    pass_raqam = models.IntegerField(verbose_name="Passport seriyasi",
                                     validators=[MaxValueValidator(9999999), MinValueValidator(1000000)])
    pass_berilgan_sana = models.DateField()
    doimiy_viloyat = models.ForeignKey(Viloyat, verbose_name="Doimiy yashash viloyati", on_delete=models.PROTECT)
    doimiy_tuman = models.ForeignKey(Tuman, verbose_name="Doimiy yashash tumani", related_name='+',
                                     on_delete=models.PROTECT)
    doimiy_mahalla = models.ForeignKey(Mahalla, verbose_name="Doimiy yashash mahallasi", on_delete=models.PROTECT)
    doimiy_kucha = models.ForeignKey(Kucha, verbose_name="Doimiy yashash ko'chasi", on_delete=models.PROTECT)
    doimiy_manzil = models.TextField( verbose_name="Doimiy yashash manzili", blank=True, null=True)
    doimiy_hozirgi_manzil = models.BooleanField(default=True, blank=True)  # ko'rish kerak
    status = models.BooleanField(default=True)  # o'lim holati
    migrant = models.BooleanField(default=False, blank=True, null=True)  # bu olib tashlangan
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    add_user = models.ForeignKey('CustomUser', verbose_name="Kirituvchi", on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.familiya

    class Meta:
        ordering = ['-qushulgan_sana']
        verbose_name = "Fuqaro"
        verbose_name_plural = "Fuqarolar"



'''o'tgan'''
class Fuqaro_Jshir_Takror(models.Model):
    """ Fuqaro JSHIR takrorlanganlar aloxida olib qo'yilgan """
    jshir = models.BigIntegerField(verbose_name="JSHIR", validators=[MaxValueValidator(99999999999999),
                                                                     MinValueValidator(10000000000000)])
    familiya = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    sharif = models.CharField(max_length=30)
    tug_sana = models.DateField()
    tug_joy_davlat_id = models.ForeignKey(Davlat, verbose_name="Tug'ulgan davlati", on_delete=models.PROTECT)
    tug_joy_tuman_id = models.ForeignKey(Tuman, verbose_name="Tug'ulgan tumani", related_name='+',
                                         on_delete=models.PROTECT)
    millat_id = models.ForeignKey(Millat, verbose_name="Millat", on_delete=models.PROTECT)
    pass_kim_bergan_tuman_id = models.ForeignKey(Tuman, verbose_name="Passport bergan tuman", related_name='+',
                                                 on_delete=models.PROTECT)
    jins = models.ForeignKey(Jins, verbose_name="Jinsi", on_delete=models.PROTECT)
    pass_seriya = models.CharField(max_length=2, verbose_name="Passport seriyasi")
    pass_raqam = models.IntegerField(verbose_name="Passport seriyasi",
                                     validators=[MaxValueValidator(9999999), MinValueValidator(1000000)])
    pass_berilgan_sana = models.DateField()
    doimiy_viloyat = models.ForeignKey(Viloyat, verbose_name="Doimiy yashash viloyati", on_delete=models.PROTECT)
    doimiy_tuman = models.ForeignKey(Tuman, verbose_name="Doimiy yashash tumani", related_name='+',
                                     on_delete=models.PROTECT)
    doimiy_mahalla = models.ForeignKey(Mahalla, verbose_name="Doimiy yashash mahallasi", on_delete=models.PROTECT)
    doimiy_kucha = models.ForeignKey(Kucha, verbose_name="Doimiy yashash ko'chasi", on_delete=models.PROTECT)
    doimiy_manzil = models.CharField(max_length=250, verbose_name="Doimiy yashash manzili", blank=True, null=True)
    doimiy_hozirgi_manzil = models.BooleanField(default=True, blank=True)  # ko'rish kerak
    status = models.BooleanField(default=True)  # o'lim holati
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    add_user = models.ForeignKey('CustomUser', verbose_name="Kirituvchi", on_delete=models.PROTECT)

    def __str__(self):
        return self.familiya

    class Meta:
        ordering = ['-qushulgan_sana']
        verbose_name = "Takror kiritilgan fuqaro"
        verbose_name_plural = "Takror kiritilgan fuqarolar"


class Fuqaro_tashqi_kiritilgan(models.Model):
    """ fuqaro_tashqi_kiritilgan pisx uchotga olganda kiritgan """
    fuqarolik_turi = models.ForeignKey(Fuqarolik_turi, on_delete=models.PROTECT)
    fuqaro_id =  models.ForeignKey(Fuqaro, on_delete=models.PROTECT)


    class Meta:
        ordering = ['fuqaro_id']
        verbose_name = "Tashqi kiritilgan fuqaro"
        verbose_name_plural = "Tashqi kiritilgan fuqarolar"

'''o'tgan'''
class Boshqa_manzili(models.Model):
    fuqaro_id = models.ForeignKey(Fuqaro, on_delete=models.PROTECT, verbose_name="fuqaro id si")
    yashash_viloyat = models.ForeignKey(Viloyat, on_delete=models.PROTECT, verbose_name="fuqaro  yashash viloyati")
    yashash_tuman = models.ForeignKey(Tuman, on_delete=models.PROTECT, verbose_name="fuqaro  yashash Tuman")
    yashash_mahalla = models.ForeignKey(Mahalla, on_delete=models.PROTECT, verbose_name="fuqaro  yashash Mahalla")
    yashash_kucha = models.ForeignKey(Kucha, on_delete=models.PROTECT, verbose_name="fuqaro  yashash ko'chasi")
    yashash_manzili = models.CharField(max_length=200, verbose_name="yashash manzili", blank=True, null=True)

'''o'tgan'''
class Usmir(models.Model):
    """ Usmir """

    familiya = models.CharField(max_length=100)
    ism = models.CharField(max_length=100)
    sharif = models.CharField(max_length=100)
    tug_sana = models.DateField()
    tug_joy_davlat_id = models.ForeignKey(Davlat, verbose_name="Tug'ulgan davlati", on_delete=models.PROTECT)
    tug_joy_tuman_id = models.ForeignKey(Tuman, verbose_name="Tug'ulgan tumani", on_delete=models.PROTECT)
    millat_id = models.ForeignKey(Millat, verbose_name="Millat", on_delete=models.PROTECT)
    guvohnoma_kim_bergan_tuman_id = models.ForeignKey(Tuman, verbose_name="tuman", related_name='+',
                                                      on_delete=models.PROTECT)
    guvohnoma_seriya = models.CharField(max_length=10, verbose_name="guvohnoma seriyasi")
    guvohnoma_raqam = models.BigIntegerField(verbose_name="guvohnoma seriyasi")
    jins = models.ForeignKey(Jins, verbose_name="tuman", on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    migrant = models.BooleanField(default=False)  # bu olib tashlangan
    qushulgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)

    add_user = models.ForeignKey('CustomUser', verbose_name="Kirituvchi", on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.familiya, self.ism

    class Meta:
        ordering = ['-qushulgan_sana']
        verbose_name = "O`smir"
        verbose_name_plural = "O`smirlar"

'''o'tgan'''
class ChetElFuqarosi(models.Model):
    hujjatning_seriyasi_raqami = models.CharField(max_length=30)
    familiya = models.CharField(max_length=50, verbose_name='Familiyasi')
    ism = models.CharField(max_length=50, verbose_name='Ismi')
    sharif = models.CharField(max_length=50, verbose_name='Sharifi')
    tug_sana = models.DateField(verbose_name='Tug`ilgan sanasi')
    jins = models.ForeignKey(Jins, on_delete=models.PROTECT, verbose_name='Jins')
    fuqaroligi = models.ForeignKey(Davlat, on_delete=models.PROTECT, verbose_name='Fuqaroligi')
    vaqtinchalik_viloyat = models.ForeignKey(Viloyat, on_delete=models.PROTECT)
    vaqtinchalik_tuman = models.ForeignKey(Tuman, on_delete=models.PROTECT)
    vaqtinchalik_mahalla = models.ForeignKey(Mahalla, on_delete=models.PROTECT, blank=True, null= True)
    vaqtinchalik_kucha = models.ForeignKey(Kucha, on_delete=models.PROTECT, blank=True, null= True)
    vaqtinchalik_manzil = models.TextField()
    qushilgan_sana = models.DateTimeField(auto_now_add=True)
    yangilgan_sana = models.DateTimeField(auto_now=True)

    add_user = models.ForeignKey('CustomUser', verbose_name="Kirituvchi", on_delete=models.PROTECT)

    def __str__(self):
        return self.hujjatning_seriyasi_raqami

    class Meta:
        ordering = ['-qushilgan_sana']
        verbose_name = 'Chet El Fuqarosi'
        verbose_name_plural = 'Chet El Fuqarosi'


'''o'tgan'''
class Baza_Fuqaro(models.Model):
    """ BazaFuqaro """

    jshir = models.BigIntegerField(verbose_name="JSHIR", unique=True, primary_key=True) # primary_key= True
    berilgan_joy = models.CharField(max_length=200)
    pass_seriya = models.CharField(max_length=8, verbose_name="Passport seriyasi")
    pass_raqam = models.IntegerField(verbose_name="Passport seriyasi")
    pass_berilgan_sana = models.DateField()
    pass_amal_muddati = models.DateField()
    ism = models.CharField(max_length=80)
    familiya = models.CharField(max_length=80)
    sharif = models.CharField(max_length=80)
    tug_sana = models.DateField()
    guvohnoma_seriya = models.CharField(max_length=30, verbose_name="guvohnoma seriyasi")
    guvohnoma_raqam = models.IntegerField(verbose_name="guvohnoma seriyasi")
    guvohnoma_sana = models.DateField()
    guvohnoma_berilgan_joy = models.CharField(max_length=200)
    hujjat_turi = models.SmallIntegerField(verbose_name='Hujjat turi')
    jins = models.SmallIntegerField(verbose_name="tuman")
    holati = models.SmallIntegerField(verbose_name="Holati")


    def __str__(self):
        return self.ism

    class Meta:
        ordering = ['jshir']
        verbose_name = "BazaFuqaro"
        verbose_name_plural = "BazaFuqarolar"

'''o'tgan'''
class BazaUsmir(models.Model):
    """ BazaUsmir """
    branch = models.IntegerField(verbose_name='branch')
    jshir = models.BigIntegerField(verbose_name="JSHIR", blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    qfy_code = models.IntegerField(verbose_name='QFY code', blank=True, null=True)
    familiya = models.CharField(max_length=60, blank=True, null=True)
    ism = models.CharField(max_length=60, blank=True, null=True)
    sharif = models.CharField(max_length=60, blank=True, null=True)
    jins_code = models.IntegerField(verbose_name="Jins kodi", blank=True, null=True)
    jins_nomi = models.CharField(verbose_name="Jins Nomi", max_length=10, blank=True, null=True)
    tugilgan_kun = models.DateField(blank=True, null=True)
    vazni = models.IntegerField(blank=True, null=True)
    buyi = models.IntegerField(blank=True, null=True)
    cert_num = models.CharField(max_length=60, verbose_name='Cert_num', blank=True, null=True)
    cert_date = models.DateField(blank=True, null=True)
    cert_place = models.IntegerField(verbose_name='Cert Place', blank=True, null=True)
    ota_familiya = models.CharField(max_length=100, verbose_name='Otasining Familiyasi', blank=True, null=True)
    ota_ism = models.CharField(max_length=100, verbose_name='Otasining ismi', blank=True, null=True)
    ota_sharif = models.CharField(max_length=100, verbose_name='Otasining Sharifi', blank=True, null=True)
    ota_tug_sana = models.DateField(verbose_name='Otasining tug`ilgan sanasi', blank=True, null=True)
    ona_familiya = models.CharField(max_length=100, verbose_name='Onasining Familiyasi', blank=True, null=True)
    ona_ism = models.CharField(max_length=100, verbose_name='Onasining ismi', blank=True, null=True)  # ForeignKey
    ona_sharif = models.CharField(max_length=60, verbose_name='Onasining Sharifi', blank=True, null=True)
    ona_tug_sana = models.DateField(verbose_name='Onasining tug`ilgan sanasi', blank=True, null=True)
    ona_passport_raqami = models.IntegerField(verbose_name='Onasining Pasport raqami', blank=True, null=True)
    guvohnoma_seriyasi = models.CharField(max_length=10, verbose_name='Guvohnoma seriyasi', blank=True, null=True)
    guvohnoma_raqami = models.BigIntegerField(verbose_name='Guvohnoma raqami', blank=True, null=True)
    guvohnoma_berilgan_sana = models.DateField(verbose_name='Guvohnoma berilgan sanasi', blank=True, null=True)
    doc_num = models.CharField(max_length=200, verbose_name='Doc_num', blank=True, null=True)



    ota_shir = models.BigIntegerField(verbose_name='Ota JSHIR', blank=True, null=True)
    ona_shir = models.BigIntegerField(verbose_name='Ona JSHIR', blank=True, null=True)
    ota_pasport_seriya = models.CharField(max_length=10, verbose_name='Otasining Pasport seriyasi', blank=True,
                                          null=True)
    ona_pasport_seriya = models.CharField(max_length=2, verbose_name='Onasining Pasport seriyasi', blank=True,
                                          null=True)
    ota_pasport_raqami = models.SmallIntegerField(verbose_name='Otasining Pasport raqami', blank=True, null=True)


    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "BazaUsmir"
        verbose_name_plural = "BazaUsmirlar"

'''o'tgan'''
class mkb10(models.Model):
    r = models.CharField(max_length=15)
    r_parent = models.CharField(max_length=15, blank=True, null=True)
    r_level = models.SmallIntegerField()
    row_num = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    include = models.TextField(blank=True, null=True)
    exclude = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    s_group = models.BooleanField(default=False)
    F_Print = models.BooleanField(default=False)
    R3 = models.CharField(max_length=3)
    ER3 = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['r']
        verbose_name = "mkb10"
        verbose_name_plural = "mkb10"


'''tashkilotlarga tegishli'''

'''o'tgan'''
class Tashkilot_tur(models.Model):
    '''barcha tashkilotlar turlari'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Tashkilot turi"
        verbose_name_plural = "Tashkilot turlari"

'''o'tgan'''
class Tashkilot(models.Model):
    parent = models.ForeignKey('Tashkilot', blank=True, null=True, on_delete=models.PROTECT, related_name='child')
    nomi = models.CharField(max_length=50)
    tashkilot_turi = models.ForeignKey(Tashkilot_tur, verbose_name="Tashkilot turi", on_delete=models.PROTECT)
    tuman_tashkilotimi = models.BooleanField(default=True, verbose_name='Tuman tashkilotimi yoki viliya?')
    tuman_id = models.ForeignKey(Tuman, verbose_name="Tuman nomi", on_delete=models.PROTECT)
    login = models.CharField(max_length=50, default='', blank=True, null=True)  # bu faqat malumot uchun qo'yilgan
    parol = models.CharField(max_length=50, default='', blank=True, null=True)  # bu faqat malumot uchun qo'yilgan
    oldingi_id = models.IntegerField(blank=True, null=True)

    # fuqarolari_soni = models.IntegerField(blank=True, null=True)        bu     Tashkilot_qushimcha_malumot     ga o'tdi
    # oila_soni = models.IntegerField(blank=True, null=True)                bu     Tashkilot_qushimcha_malumot     ga o'tdi

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['nomi']
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlari"

'''o'tgan'''
class Tashkilot_qushimcha_malumot(models.Model):
    tashkilot_id = models.ForeignKey(Tashkilot, verbose_name="Tashkilot nomi", on_delete=models.PROTECT)
    fuqarolari_soni = models.IntegerField(blank=True, null=True)
    oila_soni = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['tashkilot_id']
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlari"


class Tashkilot_Tel(models.Model):
    tashkilot = models.ForeignKey(Tashkilot, verbose_name="Tashkilot nomi", on_delete=models.PROTECT)
    tel = models.CharField(max_length=20, verbose_name='Tashkilot telefon raqami')

    class Meta:
        ordering = ['tashkilot_id']
        verbose_name = "Tashkilot telefon raqami"
        verbose_name_plural = "Tashkilotlar telefon raqamilari"



'''o'tgan'''
class Mahalla_op(models.Model):
    tashkilot = models.ForeignKey(Tashkilot, verbose_name="Tashkiloti", on_delete=models.PROTECT)
    mahalla = models.ForeignKey(Mahalla, verbose_name="Biriktirilgan maxallalar",  on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.tashkilot

    class Meta:
        ordering = ['tashkilot']
        verbose_name = "Biriktirilgan maxallalar "
        verbose_name_plural = "Biriktirilgan maxallalar"


""" Users """


class CustomUser(AbstractUser):
    tashkilot = models.ForeignKey(Tashkilot, on_delete=models.PROTECT, verbose_name='Qaysi Tashkilotda ishlaydi ',blank=True, null=True)


class CustomGroup(Group):
    tashkilot_turi = models.ForeignKey(Tashkilot_tur, verbose_name="Tashkilot Turi", on_delete=models.SET_NULL,
                                       null=True)

    class Meta:
        verbose_name = "Lavozim Group"
        verbose_name_plural = "Lavozim Groups"



