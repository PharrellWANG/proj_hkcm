# This Python file uses the following encoding: utf-8# !/usr/bin/env pythonimport osimport djangoimport geocoderos.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj_hkcm.settings")django.setup()from hkcm.models import DistrictsForAllLocationsinLocaListfrom proj_hkcm.settings import BASE_DIRif __name__ == "__main__":    """this file is for importing the list of locations    together with generated lati&longi    to the database table named 'hongkongdistricts'    Author  : Pharrell.zx    Date    : 2017 Feb 6 """    with open(str(BASE_DIR) + '/txt_csv_files/Lib2_ListOfLocation.txt', 'r+') as fl:        localines = [line[:-1] for line in fl]  # for escaping the newline next to the location string    counter = 0    for ori_location in localines:        if counter < 36058:            counter += 1            print(counter)        elif 36058 <= counter < 37058 and counter < 38058:  # line for modify: next day is 2400<=counter<4800            location = "香港" + ori_location            # print(type(location))            print(location)            counter += 1            print(counter)            g = geocoder.google(location)            # print(g)            try:                # print("enter try....")                lat = g.latlng[0]                lng = g.latlng[1]                print(lat)                print(lng)                location_name = ori_location                record = DistrictsForAllLocationsinLocaList(location=location_name,                                                            latitude=lat,                                                            longitude=lng,                                                            Districts="null")                record.save()            except:                pass        else:            pass## if __name__ == "__main__":#     """this file is for importing the list of locations#     together with generated lati&longi#     to the database table named 'hongkongdistricts'##     Author  : Pharrell.zx#     Date    : 2017 Feb 6 """##     with open('/home/ubuntu/proj_hkcm/txt_csv_files/Lib2_ListOfLocation.txt', 'r+') as fl:#         localines = [line[:-1] for line in fl]  # for escaping the newline next to the location string#     counter = 0#     # for location in localines:#     ##     #     if 0 <= counter < 2400 and counter < 38058:  # line for modify: next day is 2400<=counter<4800##     location = localines[0]#     print(type(location))#     print(location)#     # u_location = location#     # u_location = location.decode('utf-8', 'ignore')#     # print(type(u_location))#     # print(u_location)##     print(counter)#     counter += 1#     print(counter)#     g = geocoder.google(location)#     print(g)#     # try:#     #     lat = g.latlng[0]#     #     lng = g.latlng[1]#     #     print(lat)#     #     print(lng)#     #     location_name = location#     ##     #     record = DistrictsForAllLocationsinLocaList(location=location_name,#     #                                                    latitude=lat,#     #                                                    longitude=lng,#     #                                                    Districts="null")#     #     record.save()#     # except:#     #     pass##         # else:#         #     pass