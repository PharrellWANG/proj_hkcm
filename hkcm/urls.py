from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views, list_json

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^hkcm/$', views.map_page, name='map'),
    url(r'^charts/$', views.charts, name='charts'),
    # url(r'^filters$', views.filters, name='filters'),

    # urls for json data list
    url(r'^hkcm/FilterCrimeListJson/$', list_json.FilterCrimeListJson.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
