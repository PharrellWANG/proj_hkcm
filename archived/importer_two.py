# This Python file uses the following encoding: utf-8# !/usr/bin/env pythonimport csvimport osimport djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj_hkcm.settings")django.setup()from hkcm.models import latlngMappingDistrictsfrom proj_hkcm.settings import BASE_DIRif __name__ == "__main__":    """this file is for importing the classification of existing    data in table cmdata    together with generated districts    to the database table named 'districtsclassification'    Author  : Pharrell.zx    Date    : 2017 Feb 6 """    with open(str(BASE_DIR) + '/txt_csv_files/pointInPolygon_output_20170228.csv', 'rb') as ifile:        reader = csv.reader(ifile)        header = "undefined"        rownum = 0        for row in reader:            if rownum == 0:                header = row            else:                colnum = 0                id_in_d = 0                location = 0                latitude = 0                longitude = 0                Districts = 0                Districts_chn = 0                for col in row:                    if header[colnum] == 'id':                        id_in_d = col                    # elif header[colnum] == 'name':                    #     location = col                    elif header[colnum] == 'lat':                        latitude = col                    elif header[colnum] == 'lon':                        longitude = col                    elif header[colnum] == 'DISTRICT_E':                        Districts = col                    # elif header[colnum] == 'DISTRICT_C':                    #     Districts_chn = col                    else:                        pass                    colnum += 1                record = latlngMappingDistricts(id_in_d=id_in_d,                                                 # location=location,                                                 latitude=latitude,                                                 longitude=longitude,                                                 Districts=Districts,                                                 )                record.save()            rownum += 1    ifile.close()