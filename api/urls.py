from django.urls import include, path
from django.conf.urls import url
from api import api

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('initialize/', api.initialize),
    path('getmap/', api.get_map),
    path('getitem/0', api.get_item_0),
    path('getitem/1', api.get_item_1),
    path('getitem/2', api.get_item_2),
    path('getitem/3', api.get_item_3),
    path('getitem/4', api.get_item_4),
    path('getitem/5', api.get_item_5),
    path('getitem/6', api.get_item_6),
    path('getitem/7', api.get_item_7),
    path('getitem/8', api.get_item_8),
    path('getitem/9', api.get_item_9),
    path('getitem/10', api.get_item_10),
    path('getitem/11', api.get_item_11),
    path('getitem/12', api.get_item_12),
    path('getitem/13', api.get_item_13),
    path('getitem/14', api.get_item_14),
]
