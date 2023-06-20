from rest_framework import viewsets
from .serializer import TblColegioSerializer, TblZonaSerializer
from .models import TblColegio, TblZona

class TblColegioView(viewsets.ModelViewSet):
    serializer_class = TblColegioSerializer
    queryset = TblColegio.objects.all()


class TblZonaView(viewsets.ModelViewSet):
    serializer_class = TblZonaSerializer
    queryset = TblZona.objects.all()
