# This Python file uses the following encoding: utf-8
import json
import logging
from collections import OrderedDict

from django.shortcuts import render

from .models import Cmdata

log = logging.getLogger(__name__)
log.debug("")


def map_page(request):
    outer_dic = OrderedDict()
    all_records = Cmdata.objects.all()
    auto_id = 0
    for entry in all_records:
        # log.debug("====")
        # log.debug(auto_id)
        # log.debug(entry)

        inner_dic = OrderedDict()

        it = entry.issuetime
        it.strftime('%Y-%m-%d %H:%M')
        it = str(it)[0:16]
        inner_dic["id"] = auto_id
        inner_dic["issue_time"] = it
        inner_dic["location"] = entry.location
        inner_dic["crime"] = entry.crime
        inner_dic["crimecat"] = entry.crimecat
        inner_dic["latitude"] = entry.latitude
        inner_dic["longitude"] = entry.longitude
        inner_dic["title"] = entry.title
        inner_dic["URL"] = entry.URL
        outer_dic[auto_id] = inner_dic
        auto_id += 1
    length_of_records = auto_id
    log.debug(auto_id)
    outer_dic = json.dumps(outer_dic)

    crimecat_selector = [{'name': "總體罪案(All)", 'value': 0},
                         {'name': "劫案(Robbery)", 'value': 1},
                         {'name': "暴力罪案(Violent Crime)", 'value': 2},
                         {'name': "爆竊案(Burglary)", 'value': 3},
                         {'name': "傷人及嚴重毆打(Wounding and Serious Assault)", 'value': 4},
                         {'name': "刑事恐嚇(Criminal Intimidation)", 'value': 5},
                         {'name': "強姦及非禮(Rape)", 'value': 6},
                         {'name': "嚴重毒品罪行(Serious Drug Offenses)", 'value': 7}]

    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})

    content = {
        'outer_dic': outer_dic,
        'le': length_of_records,
        'crimecat_selector': crimecat_selector,
    }

    return render(request, 'index.html', content)


def charts(request):
    list_of_crimes = Cmdata.objects.all()
    total_crimes = list_of_crimes.count()
    caw = 0
    eastern = 0
    kowloon_city = 0
    kwai_tsing = 0
    kt = 0
    north = 0
    sk = 0
    st = 0
    ssp = 0
    southern = 0
    tp = 0
    tw = 0
    tm = 0
    wc = 0
    wts = 0
    ytm = 0
    yl = 0
    island = 0

    for x in list_of_crimes:
        if str(x.district) == 'Central & Western':
            caw += 1
        elif str(x.district) == 'Eastern':
            eastern += 1
        elif str(x.district) == 'Kowloon City':
            kowloon_city += 1
        elif str(x.district) == 'Kwai Tsing':
            kwai_tsing += 1
        elif str(x.district) == 'Kwun Tong':
            kt += 1
        elif str(x.district) == 'North':
            north += 1
        elif str(x.district) == 'Sai Kung':
            sk += 1
        elif str(x.district) == 'Sha Tin':
            st += 1
        elif str(x.district) == 'Sham Shui Po':
            ssp += 1
        elif str(x.district) == 'Southern':
            southern += 1
        elif str(x.district) == 'Tai Po':
            tp += 1
        elif str(x.district) == 'Tsuen Wan':
            tw += 1
        elif str(x.district) == 'Tuen Mun':
            tm += 1
        elif str(x.district) == 'Wan Chai':
            wc += 1
        elif str(x.district) == 'Wong Tai Sin':
            wts += 1
        elif str(x.district) == 'Yau Tsim Mong':
            ytm += 1
        elif str(x.district) == 'Yuen Long':
            yl += 1
        elif str(x.district) == 'Island':
            island += 1

    caw_crime_rate = round(caw / (246600.0 / 100000), 2)
    eastern_crime_rate = round(eastern / (574500.0 / 100000), 2)
    kowloon_city_crime_rate = round(kowloon_city / (405400.0 / 100000), 2)
    kwai_tsing_crime_rate = round(kwai_tsing / (507100.0 / 100000), 2)
    kt_crime_rate = round(kt / (641100.0 / 100000), 2)
    north_crime_rate = round(north / (310800.0 / 10000), 2)
    sk_crime_rate = round(sk / (457400.0 / 100000), 2)
    st_crime_rate = round(st / (660200.0 / 100000), 2)
    ssp_crime_rate = round(ssp / (390600.0 / 100000), 2)
    southern_crime_rate = round(southern / (269200 / 100000), 2)
    tp_crime_rate = round(tp / (307100.0 / 100000), 2)
    tw_crime_rate = round(tw / (303600.0 / 100000), 2)
    tm_crime_rate = round(tm / (495900.0 / 100000), 2)
    wc_crime_rate = round(wc / (150900.0 / 100000), 2)
    wts_crime_rate = round(wts / (426200.0 / 100000), 2)
    ytm_crime_rate = round(ytm / (318100.0 / 100000), 2)
    yl_crime_rate = round(yl / (607200.0 / 100000), 2)
    island_crime_rate = round(island / (146900.0 / 100000), 2)

    list_for_finding_maximum_crime_region = [caw, eastern, kwai_tsing, kowloon_city,
                                             kt, sk, north, ssp, tp, tw, tm, wc,
                                             wts, ytm, yl, island, st, southern]
    list_for_finding_maximum_crime_rate = [caw_crime_rate,
                                           eastern_crime_rate,
                                           kwai_tsing_crime_rate,
                                           kowloon_city_crime_rate,
                                           kt_crime_rate, sk_crime_rate,
                                           north_crime_rate,
                                           ssp_crime_rate,
                                           tp_crime_rate,
                                           tw_crime_rate,
                                           tm_crime_rate,
                                           wc_crime_rate,
                                           wts_crime_rate,
                                           ytm_crime_rate,
                                           yl_crime_rate,
                                           island_crime_rate,
                                           st_crime_rate,
                                           southern_crime_rate]

    maximum_crime_number = max(list_for_finding_maximum_crime_region)
    maximum_crime_rate____x = max(list_for_finding_maximum_crime_rate)

    location_name_of_maximum_crime = "Yau Tsim Mong"
    if maximum_crime_number == ytm:
        location_name_of_maximum_crime = "Yau Tsim Mong"
    elif maximum_crime_number == caw:
        location_name_of_maximum_crime = "Central & Western"
    elif maximum_crime_number == eastern:
        location_name_of_maximum_crime = "Eastern"
    elif maximum_crime_number == kwai_tsing:
        location_name_of_maximum_crime = "Kwai Tsing"
    elif maximum_crime_number == kowloon_city:
        location_name_of_maximum_crime = "Kowloon City"
    elif maximum_crime_number == kt:
        location_name_of_maximum_crime = "Kwun Tong"
    elif maximum_crime_number == sk:
        location_name_of_maximum_crime = "Sai Kung"
    elif maximum_crime_number == north:
        location_name_of_maximum_crime = "North"
    elif maximum_crime_number == ssp:
        location_name_of_maximum_crime = "Sham Shui Po"
    elif maximum_crime_number == tp:
        location_name_of_maximum_crime = "Tai Po"
    elif maximum_crime_number == tw:
        location_name_of_maximum_crime = "Tsuen Wan"
    elif maximum_crime_number == tm:
        location_name_of_maximum_crime = "Tuen Mun"
    elif maximum_crime_number == wc:
        location_name_of_maximum_crime = "Wan Chai"
    elif maximum_crime_number == wts:
        location_name_of_maximum_crime = "Wong Tai Sin"
    elif maximum_crime_number == island:
        location_name_of_maximum_crime = "Island"
    elif maximum_crime_number == yl:
        location_name_of_maximum_crime = "Yuen Long"
    elif maximum_crime_number == st:
        location_name_of_maximum_crime = "Sha Tin"
    elif maximum_crime_number == southern:
        location_name_of_maximum_crime = "Southern"

    loc = location_name_of_maximum_crime

    # maximum_crime_number

    log.debug(maximum_crime_number)
    log.debug(total_crimes)
    max_rate = round(float(maximum_crime_number) / total_crimes, 3) * 100
    log.debug(max_rate)
    log.debug(type(max_rate))
    content = {
        'max_rate': max_rate,
        'loc': loc,
        'maximum_crime_number': maximum_crime_number,
        'total_crimes': total_crimes,
        'caw': caw,
        'eastern': eastern,
        'kowloon_city': kowloon_city,
        'kwai_tsing': kwai_tsing,
        'kt': kt,
        'north': north,
        'sk': sk,
        'st': st,
        'ssp': ssp,
        'southern': southern,
        'tp': tp,
        'tw': tw,
        'tm': tm,
        'wc': wc,
        'wts': wts,
        'ytm': ytm,
        'yl': yl,
        'island': island,
        'caw_crime_rate': caw_crime_rate,
        'eastern_crime_rate': eastern_crime_rate,
        'kowloon_city_crime_rate': kowloon_city_crime_rate,
        'kwai_tsing_crime_rate': kwai_tsing_crime_rate,
        'kt_crime_rate': kt_crime_rate,
        'north_crime_rate': north_crime_rate,
        'sk_crime_rate': sk_crime_rate,
        'st_crime_rate': st_crime_rate,
        'ssp_crime_rate': ssp_crime_rate,
        'southern_crime_rate': southern_crime_rate,
        'tp_crime_rate': tp_crime_rate,
        'tw_crime_rate': tw_crime_rate,
        'tm_crime_rate': tm_crime_rate,
        'wc_crime_rate': wc_crime_rate,
        'wts_crime_rate': wts_crime_rate,
        'ytm_crime_rate': ytm_crime_rate,
        'yl_crime_rate': yl_crime_rate,
        'island_crime_rate': island_crime_rate,
        'maximum_crime_rate____x': maximum_crime_rate____x,
    }
    log.debug("=========")
    log.debug("=========")
    log.debug("=====??????????====")
    log.debug(maximum_crime_number)
    log.debug("maximum_crime_rate is: " + str(maximum_crime_rate____x))
    log.debug("=========")
    log.debug("")

    return render(request, 'charts.html', content)
