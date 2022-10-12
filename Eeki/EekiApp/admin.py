from django.contrib import admin
from .models import Config
from .models import Farm
from .models import Device
from .models import BasicTest
from .models import FunctionalTest
from .models import AssemblyTest
from .models import Shipping
from .models import Deployment
from .models import ChangeStatus

from django.shortcuts import render
from django.contrib import messages
from .form import *


# class StatusAdmin(admin.ModelAdmin):
#     model = Config
#     actions = ['basictestdone', 'functionaltestdone', 'assemblytestdone', 'shippingdone', 'deploymentdone', 'Alldone']
#     fields = ['pcbid', 'deviceid','basicteststatus','functionalteststatus', 'assemblyteststatus', 'shippingstatus', 'deploymentstatus', 'status',]

#     def basictestdone(self, request, queryset):
#         queryset.update(basicteststatus = True)

#     def functionaltestdone(self, request, queryset):
#         queryset.update(functionalteststatus = True)

#     def assemblytestdone(self, request, queryset):
#         queryset.update(assemblyteststatus = True)

#     def shippingdone(self, request, queryset):
#         queryset.update(shippingstatus = True)

#     def deploymentdone(self, request, queryset):
#         queryset.update(deploymentstatus = True)

#     def Alldone(self, request, queryset):
#         queryset.update(status = True)    




class DeviceAdmin(admin.ModelAdmin):
    list_display = ('pcbid', 'pcbboardversion', 'atmega', 'esp32', 'deviceid')
    actions = ['change status with remarks']

    def set_genre_action(self, request, queryset):
        if 'do_action' in request.POST:
            form = Form(request.POST)
            if form.is_valid():
                status = request.POST.get('status')
                changefrom = request.POST.get('changefrom')
                remarks = request.POST.get('remarks')
                dt = Form(status=status, changefrom=changefrom, remarks=remarks)
                dt.save()
                print("Inserted")
                # status = form.cleaned_data['status']
                # updated = queryset.update(status=status)
                # messages.success(request, '{0} status were updated'.format(updated))
                return
        else:
            form = Form()

        return render(request, 'index.html',
            {'title': u'Choose status',
             'objects': queryset,
             'form': form})
    set_genre_action.short_description = u'Update status of selected device'
admin.site.register(Device, DeviceAdmin)




admin.site.register(Config)
admin.site.register(Farm)
# admin.site.register(Device)
admin.site.register(ChangeStatus)
admin.site.register(BasicTest)
admin.site.register(FunctionalTest)
admin.site.register(AssemblyTest)
admin.site.register(Shipping)
admin.site.register(Deployment)
