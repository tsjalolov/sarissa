from django.contrib import admin
from .models import *
from fuqaro.forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin, Group


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Role',
            {
                'fields': (
                    'tashkilot',
                )
            }
        )
    )


admin.site.register(Tashkilot)

admin.site.register(Baza_Fuqaro)
admin.site.register(Usmir)
admin.site.register(BazaUsmir)
admin.site.register(Tashkilot_tur)

admin.site.register(Kucha)
admin.site.register(Mahalla)
admin.site.register(Tuman)
admin.site.register(Viloyat)
admin.site.register(Davlat)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)


admin.site.register(Fuqaro)
admin.site.register(Fuqarolik_turi)
admin.site.register(Millat)
admin.site.register(Jins)
