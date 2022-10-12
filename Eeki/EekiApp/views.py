from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics

from .serializers import DeploymentSerializer, FarmSerializer, ShippingSerializer
from .serializers import PCBSerializer
from .serializers import BasicTestSerializer
from .serializers import FunctionalTestSerializer
from .serializers import AssemblyTestSerializer
from .serializers import ConfigSerializer

from .models import Deployment, Farm, Shipping
from .models import Device
from .models import BasicTest
from .models import FunctionalTest
from .models import AssemblyTest
from django.core.cache import cache
from .models import Config

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


# def device(request):
#     payload = []
#     db = None
#     if cache.get('device'):
#         payload = cache.get('device')
#         db = 'redis'
#     else:
#         dev = Config.objects.all()
#         for i in dev:
#             payload.append(i.pcbid, i.deviceid)
#         db = 'postgres'
#         cache.set('device',payload) 
#     return JsonResponse({'status': 200, 'db' : db, 'data' : payload})      

# def devicedetail(request, id):
#     context = {}
#     context['data'] = Config.objects.get(id = id)
#     return render(request, "device.html", context)




class FarmList(generics.ListCreateAPIView):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()
    def get_queryset(self):
        queryset = Farm.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class FarmViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Config.objects.all()
        serializer = ConfigSerializer(queryset, many=True)
        return Response(serializer.data)

class FarmDetails(generics.RetrieveDestroyAPIView):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()


class PCBList(generics.ListCreateAPIView):
    serializer_class = PCBSerializer
    queryset = Device.objects.all()
    def get_queryset(self):
        queryset = Device.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
       

class PCBDetails(generics.RetrieveDestroyAPIView):
    serializer_class = PCBSerializer
    queryset = Device.objects.all()


class BasicTestList(generics.ListCreateAPIView):
    serializer_class = BasicTestSerializer
    queryset = BasicTest.objects.all()
    def get_queryset(self):
        queryset = BasicTest.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset           


class BasicTestDetails(generics.RetrieveDestroyAPIView):
    serializer_class = BasicTestSerializer
    queryset = BasicTest.objects.all()


class FunctionalTestList(generics.ListCreateAPIView):
    serializer_class = FunctionalTestSerializer
    queryset = FunctionalTest.objects.all()
    def get_queryset(self):
        queryset = FunctionalTest.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset    


class FunctionalTestDetails(generics.RetrieveDestroyAPIView):
    serializer_class = FunctionalTestSerializer
    queryset = FunctionalTest.objects.all()


class AssemblyTestList(generics.ListCreateAPIView):
    serializer_class = AssemblyTestSerializer
    queryset = AssemblyTest.objects.all()
    def get_queryset(self):
        queryset = AssemblyTest.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset     


class AssemblyTestDetails(generics.RetrieveDestroyAPIView):
    serializer_class = AssemblyTestSerializer
    queryset = AssemblyTest.objects.all()        


class ShippingList(generics.ListCreateAPIView):
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()
    def get_queryset(self):
        queryset = Shipping.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset     


class ShippingDetails(generics.RetrieveDestroyAPIView):
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()


class DeploymentList(generics.ListCreateAPIView):
    serializer_class = DeploymentSerializer
    queryset = Deployment.objects.all()
    def get_queryset(self):
        queryset = Deployment.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset     


class DeploymentDetails(generics.RetrieveDestroyAPIView):
    serializer_class = DeploymentSerializer
    queryset = Deployment.objects.all()    
