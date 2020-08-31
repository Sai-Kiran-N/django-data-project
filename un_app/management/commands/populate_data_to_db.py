from django.core.management.base import BaseCommand
from django.db import transaction
from csv import reader

from un_app.models import (
    RegionData,
    AseanCountry,
    BricsCountry,
    G4Country,
    G7Country,
    SaarcCountry,
)


def csv_to_region_table(file_name):
    with open(file_name, 'r') as csv_file:
        csv_data = list(reader(csv_file))
        data = RegionData.objects.all()
        if(not data):
            print('\nAdding csv file records to the database...\n')
            with transaction.atomic():
                for row in csv_data[1:]:
                    RegionData.objects.create(
                                            region=row[0],
                                            country_code=int(row[1]),
                                            year=int(row[2]),
                                            population=float(row[3]),
                                            )
        else:
            print('\nCsv file records already exists in the database\n')


def asean_table(asean_countries):
    data = AseanCountry.objects.all()
    if(not data):
        print('Adding ASEAN countries records to the database...\n')
        for country in asean_countries:
            AseanCountry.objects.create(name=country)
    else:
        print('ASEAN countries records already exists in the database\n')


def brics_table(brics_countries):
    data = BricsCountry.objects.all()
    if(not data):
        print('Adding BRICS countries records to the database...\n')
        for country in brics_countries:
            BricsCountry.objects.create(name=country)
    else:
        print('BRICS countries records already exists in the database\n')


def g4_table(g4_countries):
    data = G4Country.objects.all()
    if(not data):
        print('Adding G4 countries records to the database...\n')
        for country in g4_countries:
            G4Country.objects.create(name=country)
    else:
        print('G4 countries records already exists in the database\n')


def g7_table(g7_countries):
    data = G7Country.objects.all()
    if(not data):
        print('Adding G7 countries records to the database...\n')
        for country in g7_countries:
            G7Country.objects.create(name=country)
    else:
        print('G7 countries records already exists in the database\n')


def saarc_table(saarc_countries):
    data = SaarcCountry.objects.all()
    if(not data):
        print('Adding Saarc countries records to the database...\n')
        for country in saarc_countries:
            SaarcCountry.objects.create(name=country)
    else:
        print('Saarc countries records already exists in the database\n')


class Command(BaseCommand):

    def handle(self, *args, **options):
        asean_countries = [
            'Brunei Darussalam', 'Cambodia', 'Indonesia',
            "Lao People's Democratic Republic",
            'Malaysia', 'Myanmar', 'Philippines',
            'Singapore', 'Thailand', 'Viet Nam',
            ]

        brics_countries = [
            'Brazil', 'Russian Federation', 'India', 'China',
            'South Africa',
            ]

        g4_countries = [
            'Brazil', 'Germany', 'India', 'Japan',
            ]

        g7_countries = [
            'Canada', 'France', 'Germany', 'Italy', 'Japan',
            'United Kingdom', 'United States of America',
            ]

        saarc_countries = [
            'Afghanistan', 'Bangladesh', 'Bhutan', 'India',
            'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka',
            ]

        csv_file_name = 'population-estimates_csv.csv'

        # Reads data from csv file, stores it in database table "region_data"
        csv_to_region_table(csv_file_name)

        # Stores the asean_countries names in database table "asean_countries"
        asean_table(asean_countries)

        # Stores the brics_countries names in database table "brics_countries"
        brics_table(brics_countries)

        # Stores the g4_countries names in database table "g4_countries"
        g4_table(g4_countries)

        # Stores the g7_countries names in database table "g7_countries"
        g7_table(g7_countries)

        # Stores the saarc_countries names in database table "saarc_countries"
        saarc_table(saarc_countries)
