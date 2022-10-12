from django.contrib import admin
from django.urls import path
from . import views
from .views import FarmDetails, PCBList, PCBDetails, BasicTestList, BasicTestDetails, FunctionalTestList, FunctionalTestDetails,AssemblyTestList, AssemblyTestDetails, ShippingList, ShippingDetails, DeploymentList, DeploymentDetails,FarmList
# from .views import devicedetail
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path("farmlist/", cache_page(60*60)(FarmViewSet.as_view())),
    path("farm/", cache_page(60*60)(FarmList.as_view())),
    path("farm/<int:pk>/", cache_page(60*60)(FarmDetails.as_view())),
    path("pcb/", cache_page(60*60)(PCBList.as_view())),
    path("pcb/<int:pk>", cache_page(60*60)(PCBDetails.as_view())),
    path("basic/", cache_page(60*60)(BasicTestList.as_view())),
    path("basic/<int:pk>", cache_page(60*60)(BasicTestDetails.as_view())),
    path("functional/", cache_page(60*60)(FunctionalTestList.as_view())),
    path("functional/<int:pk>", cache_page(60*60)(FunctionalTestDetails.as_view())),
    path("assembly/", cache_page(60*60)(AssemblyTestList.as_view())),
    path("assembly/<int:pk>", cache_page(60*60)(AssemblyTestDetails.as_view())),
    path("shipping/", cache_page(60*60)(ShippingList.as_view())),
    path("shipping/<int:pk>", cache_page(60*60)(ShippingDetails.as_view())),
    path("deployment/", cache_page(60*60)(DeploymentList.as_view())),
    path("deployment/<int:pk>", cache_page(60*60)(DeploymentDetails.as_view())),
]