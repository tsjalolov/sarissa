from django.db import models

'''o'tgan'''
class IjtimoiyHolat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ijtimoiy Holati'
        verbose_name_plural = 'Ijtimoiy Holatlar'

'''o'tgan'''
class Malumoti(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ma`lumot'
        verbose_name_plural = 'Ma`lumoti'

'''o'tgan'''
class Nogironlik(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nogironlik'
        verbose_name_plural = 'Nogironliklar'

'''o'tgan'''
class OilaviySharoiti(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Oilaviy Sharoit'
        verbose_name_plural = 'Oilaviy Sharoitlar'

'''o'tgan'''
class DinamikKuzatuvchiGuruh(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dinamik Kuzatuvchi Guruh'
        verbose_name_plural = 'Dinamik Kuzatuvchi Guruhlar'

'''o'tgan'''
class TirikchilikManbasi(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tirikchilik Manbasi'
        verbose_name_plural = 'Tirikchilik Manbalari'


class UchotChiqarishSababi(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Uchot chiqarish sababi'
        verbose_name_plural = 'Uchot chiqarish sabablari'
