from rest_framework import serializers
from .models import TblColegio, TblZona

class TblColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblColegio
        fields = '__all__'

class TblZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblZona
        fields = '__all__'