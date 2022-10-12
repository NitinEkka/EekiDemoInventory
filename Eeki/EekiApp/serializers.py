from rest_framework import serializers
from .models import Config, Farm, Device , BasicTest, FunctionalTest, AssemblyTest, Shipping, Deployment

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('__all__')

class PCBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__')

class BasicTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicTest
        fields = ('__all__') 

class FunctionalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionalTest
        fields = ('__all__')  

class AssemblyTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssemblyTest
        fields = ('__all__')  

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('__all__')

class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = ('__all__')

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('__all__')                                                           