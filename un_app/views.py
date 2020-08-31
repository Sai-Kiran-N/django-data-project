from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum

from un_app.models import (
                            RegionData,
                            AseanCountry,
                            BricsCountry,
                            G4Country,
                            G7Country,
                            SaarcCountry,
                        )


def home(request):
    return render(request, 'home.html')


def plot_1(request):
    start_year = int(request.GET['start'])
    if(start_year > 2015):
        start_year = 2015 - int(request.GET['end'])
    elif(start_year < 1950):
        start_year = 1950
    end_year = start_year + int(request.GET['end'])
    if(end_year > 2015):
        end_year = 2015
    region = request.GET['region']
    year_list = list(range(start_year, end_year+1))
    population, data = list(), dict()

    query_data = RegionData.objects.\
        filter(region=region, year__in=year_list).\
        order_by('year').values('year', 'population')

    for row in query_data:
        population.append(row['population'])
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = f'{region} population over years ({start_year}-{end_year})'
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    data['y_axis_title'] = 'Population'
    data['start'] = start_year
    data['end'] = end_year - start_year
    data['region'] = region
    return JsonResponse(data)


def region_group(region):
    if(region == 'ASEAN'):
        country_list = AseanCountry.objects.values('name')
    elif(region == 'BRICS'):
        country_list = BricsCountry.objects.values('name')
    elif(region == 'G4'):
        country_list = G4Country.objects.values('name')
    elif(region == 'G7'):
        country_list = G7Country.objects.values('name')
    elif(region == 'SAARC'):
        country_list = SaarcCountry.objects.values('name')
    return country_list


def plot_2(request):
    data = {}
    start_year = int(request.GET['start'])
    if(start_year > 2015):
        start_year = 2015
    elif(start_year < 1950):
        start_year = 1950
    region = request.GET['region_group']
    country_list = region_group(region)

    query_data = RegionData.objects.\
        filter(region__in=country_list, year=start_year).\
        order_by('region').values('population', 'region')

    population = [[row['region'], row['population']] for row in query_data]
    country_list = [row['region'] for row in query_data]
    data['title'] = f'Population of {region} Countries ({start_year})'
    data['x_axis_title'] = f'{region} countries'
    data['y_axis_title'] = 'Population'
    data['x_axis_points'] = country_list
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    data['start'] = start_year
    data['region_group'] = region
    return JsonResponse(data)


def plot_3(request):
    start_year = int(request.GET['start'])
    if(start_year > 2015):
        start_year = 2015 - int(request.GET['end'])
    elif(start_year < 1950):
        start_year = 1950
    end_year = start_year + int(request.GET['end'])
    if(end_year > 2015):
        end_year = 2015
    region = request.GET['region_group']
    country_list = region_group(region)
    year_list = list(range(start_year, end_year+1))
    data, population = dict(), list()

    query_data = RegionData.objects.\
        filter(region__in=country_list, year__in=year_list).\
        values('year').order_by('year').annotate(population=Sum('population'))

    for row in query_data:
        population.append(row['population'])
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = f'Population of {region} Countries \
        ({start_year}-{end_year})'
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    data['y_axis_title'] = 'Population'
    data['start'] = start_year
    data['end'] = end_year - start_year
    data['region_group'] = region
    return JsonResponse(data)


def plot_4(request):
    start_year = int(request.GET['start'])
    if(start_year > 2010):
        start_year = 2010
        end_year = 2015
    elif(start_year < 1950):
        start_year = 1950
        end_year = 1955
    else:
        end_year = start_year + 5
    region = request.GET['region_group']
    country_list = region_group(region)
    country, index, population, data = '', -1, list(), dict()
    year_list = list(range(start_year, end_year+1))

    query_data = RegionData.objects.\
        filter(region__in=country_list, year__in=year_list).\
        order_by('region', 'year').values('population', 'region', 'year')

    for row in query_data:
        if(row['region'] != country):
            country = row['region']
            population.append({'name': country, 'data': []})
            index += 1
        population[index]['data'].append(['population', row['population']])
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = f'Grouped Bar chart of {region}\
         Population vs Years ({start_year}-{end_year})'
    data['plot_data'] = population
    data['y_axis_title'] = 'Population'
    data['start'] = start_year
    data['region_group'] = region
    return JsonResponse(data)
