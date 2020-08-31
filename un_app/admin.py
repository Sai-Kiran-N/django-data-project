from django.contrib import admin
from un_app.models import (
                    RegionData,
                    AseanCountry,
                    BricsCountry,
                    G4Country,
                    G7Country,
                    SaarcCountry,
                )


class RegionDataAdmin(admin.ModelAdmin):
    list_display = [
                    'region', 'country_code',
                    'year', 'population'
                    ]


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(RegionData, RegionDataAdmin)
admin.site.register(AseanCountry, CountryAdmin)
admin.site.register(BricsCountry, CountryAdmin)
admin.site.register(G4Country, CountryAdmin)
admin.site.register(G7Country, CountryAdmin)
admin.site.register(SaarcCountry, CountryAdmin)
