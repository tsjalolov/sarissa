# Generated by Django 4.0.4 on 2022-05-08 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fuqaro', '0001_initial'),
        ('helper_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QandliDiabetRuyxat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coviddan_keyin_kelib_chiqishi', models.BooleanField(default=False)),
                ('d_nazoratga_olingan_sana', models.DateField(verbose_name='Dinamik nazoratga olingan sana')),
                ('qandli_diabet_boshlangan_sana', models.DateField(blank=True, null=True, verbose_name='Qandli diabet boshlangan sana')),
                ('insulin_terapiya_boshlangan_sana', models.DateField(blank=True, null=True, verbose_name='Insulin terapiya boshlangan sana')),
                ('insulin_miqdori_h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori h')),
                ('insulin_miqdori_r', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori r')),
                ('insulin_miqdori_30_70', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori 30_70')),
                ('analog_insulin_h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Analog Insulin h')),
                ('analog_insulin_r', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Analog Insulin r')),
                ('tabletka_biguanid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka biguanid')),
                ('tabletka_glibenklamid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka glibenklamid')),
                ('tabletka_glimepirid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka glimepirid')),
                ('tabletka_gliklazid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka gliklazid')),
                ('tabletka_tiozolidindion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori h')),
                ('tabletka_boshqa_nomi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Boshqa Tabletka nomi')),
                ('buyi', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Bo`yi')),
                ('vazni', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Vazni')),
                ('bel_aylanasi', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Bel Aylanasi')),
                ('qon_bosimi_yuqori', models.SmallIntegerField(blank=True, null=True, verbose_name='Qon Bosimi Yuqori')),
                ('qon_bosimi_quyi', models.SmallIntegerField(blank=True, null=True, verbose_name='Qon Bosimi Quyi')),
                ('qushimcha_qabul_qiladigan_dorilari', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Qushimcha qabul qiladigan dorilari')),
                ('holati', models.BooleanField(default=True, verbose_name='Holati')),
                ('endokrinologik_tashxis_mkb10_text', models.CharField(blank=True, max_length=30, null=True, verbose_name='Endokrinologik tashxisi yozuv')),
                ('asoratlar_mkb10_text', models.CharField(blank=True, max_length=30, null=True, verbose_name='Asoratlar')),
                ('hamroh_kaslliklar', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hamroh kasalliklar')),
                ('qushilgan_sana', models.DateTimeField(auto_now_add=True, verbose_name='Qushilgan sana')),
                ('yangilangan_sana', models.DateTimeField(auto_now=True)),
                ('add_tashkilot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.tashkilot', verbose_name='Kirituvchi Tashkilot')),
                ('add_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kirituvchi')),
                ('asoratlar_mkb10_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='fuqaro.mkb10', verbose_name='Asoratlar')),
                ('chetel_fuqaro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fuqaro.chetelfuqarosi', verbose_name='Chet el fuqarosi ID')),
                ('endokrinologik_tashxis_mkb10', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='fuqaro.mkb10', verbose_name='Endokrinologik tashxisi')),
                ('fuqaro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fuqaro.fuqaro', verbose_name='Fuqaro ID')),
                ('fuqaro_lik_turi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.fuqarolik_turi', verbose_name='Fuqarolik Turi')),
                ('ijtimoiy_holat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helper_app.ijtimoiyholat', verbose_name='Ijtimoiy Holat')),
                ('nogironligi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helper_app.nogironlik', verbose_name='Nogironligi')),
                ('tuman_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.tuman', verbose_name='Tuman ID')),
                ('usmir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fuqaro.usmir', verbose_name='Fuqaro ID')),
            ],
            options={
                'verbose_name': 'Qandli Diabet Ruyxat',
                'verbose_name_plural': 'Qandli Diabet Ruyxatlari',
            },
        ),
        migrations.CreateModel(
            name='Qandli_diabet_ruyxat_shir_takror',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coviddan_keyin_kelib_chiqqan', models.BooleanField(default=False)),
                ('d_nazoratga_olingan_sana', models.DateField(verbose_name='Dinamik nazoratga olingan sana')),
                ('qandli_diabet_boshlangan_sana', models.DateField(blank=True, null=True, verbose_name='Qandli diabet boshlangan sana')),
                ('insulin_terapiya_boshlangan_sana', models.DateField(blank=True, null=True, verbose_name='Insulin terapiya boshlangan sana')),
                ('insulin_miqdori_h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori h')),
                ('insulin_miqdori_r', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori r')),
                ('insulin_miqdori_30_70', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori 30_70')),
                ('analog_insulin_h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Analog Insulin h')),
                ('analog_insulin_r', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Analog Insulin r')),
                ('tabletka_biguanid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka biguanid')),
                ('tabletka_glibenklamid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka glibenklamid')),
                ('tabletka_glimepirid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka glimepirid')),
                ('tabletka_gliklazid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tabletka gliklazid')),
                ('tabletka_tiozolidindion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Insulin miqdori h')),
                ('tabletka_boshqa_nomi_dozasi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Boshqa Tabletka nomi')),
                ('buyi', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Bo`yi')),
                ('vazni', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Vazni')),
                ('bel_aylanasi', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Bel Aylanasi')),
                ('qon_bosimi_yuqori', models.SmallIntegerField(blank=True, null=True, verbose_name='Qon Bosimi Yuqori')),
                ('qon_bosimi_quyi', models.SmallIntegerField(blank=True, null=True, verbose_name='Qon Bosimi Quyi')),
                ('qushimcha_qabul_qiladigan_dorilar', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Qushimcha qabul qiladigan dorilari')),
                ('holati', models.BooleanField(default=True, verbose_name='Holati')),
                ('endokrinologik_tashxis_mkb10', models.CharField(blank=True, max_length=30, null=True, verbose_name='Endokrinologik tashxisi yozuv')),
                ('asoratlar', models.CharField(blank=True, max_length=30, null=True, verbose_name='Asoratlar')),
                ('hamroh_kasalliklar', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hamroh kasalliklar')),
                ('qushgan_user', models.IntegerField(verbose_name='Kirituvchi Tashkilot')),
                ('qushilgan_sana', models.DateTimeField(auto_now_add=True, verbose_name='Qushilgan sana')),
                ('fuqaro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.fuqaro_jshir_takror', verbose_name='Fuqaro')),
                ('fuqarolik_turi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.fuqarolik_turi', verbose_name='Fuqarolik Turi')),
                ('ijtimoiy_holati', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helper_app.ijtimoiyholat', verbose_name='Ijtimoiy Holat')),
                ('nogironligi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helper_app.nogironlik', verbose_name='Nogironligi')),
                ('tuman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fuqaro.tuman', verbose_name='Tuman ID')),
            ],
            options={
                'verbose_name': 'Qandli Diabet Ruyxat',
                'verbose_name_plural': 'Qandli Diabet Ruyxatlari',
            },
        ),
    ]
