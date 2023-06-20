from colegio import views
from django.urls import path, include
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'colegio', views.TblColegioView, 'colegio')
route.register(r'zona', views.TblZonaView, 'zona')


urlpatterns = [
    path('api/', include(route.urls))
]