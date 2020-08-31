from django.db import models


# Create your models here.
class RegionData(models.Model):
    region = models.CharField(max_length=100)
    country_code = models.IntegerField()
    year = models.IntegerField()
    population = models.FloatField()

    class Meta:
        db_table = 'region_data'

    def __repr__(self):
        return f'Region : {self.region}'


class AseanCountry(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'asean_countries'

    def __repr__(self):
        return f'Country : {self.name}'


class BricsCountry(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brics_countries'

    def __repr__(self):
        return f'Country : {self.name}'


class G4Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'g4_countries'

    def __repr__(self):
        return f'Country : {self.name}'


class G7Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'g7_countries'

    def __repr__(self):
        return f'Country : {self.name}'


class SaarcCountry(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'saarc_countries'

    def __repr__(self):
        return f'Country : {self.name}'
