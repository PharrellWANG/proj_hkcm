Structure of Program
====================

Core 1: crawler
---------------
The file ``./crawler_for_crime_map.py`` is the crawler that regularly
scraps data from https://wwww.hk01.com, which is a news website. It
first collects data then saves collected data into database when certain
conditions are met. Check the codes for details. The file ``./fill_cmdata_with_dist.py``
is for assigning one of the eighteen districts in HK to each newly added
crime record.

Core 2: website
---------------
There are two web pages in this project, the html template files
are located in ``./templates``.
Inside folder ``./hkcm``: ``views.py`` contains python codes for getting data
from database and rendering two views, one is the main page of the website,
the other is the charts page; ``models.py`` defines the database table structures;
``list_json.py`` is making use of **django rest framework** to provide api support
for crime information filtering function.

Others
------
Libs
^^^^
The ``./hkcm/static`` folder contains
all the third party libraries. Do not delete from ``./hkcm/static``
folder. In contrary, you may add libraries to ``./hkcm/static``
folder when needs arise.
``./txt_csv_files`` contains three libraries built by myself,
there is no need to modify them.

Relics
^^^^^^
``./archived`` contains some python scripts that have
been used, which are now kept for future reference.

Logs
^^^^
``./logs`` contains project logs.

Git ignore
^^^^^^^^^^
Inside folder ``./proj_hkcm``, ``dev_db.py`` is
ignored by git since it might be different in each development site.
Check codes for details.
