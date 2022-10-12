from email.policy import default
from enum import unique
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models




class Farm(models.Model):
    farmid = models.CharField(max_length=150)
    domeid = models.CharField(max_length=50)
    deviceid = models.CharField(max_length=50)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.farmid

class Config(models.Model):
    type = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type        

class ChangeStatus(models.Model):
    status = models.CharField(max_length=50, unique=True)
    changefrom = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Device(models.Model):
    pcbid = models.CharField(max_length=50)
    pcbboardversion = models.CharField(max_length=50)
    atmega = models.CharField(max_length=50)
    esp32 = models.CharField(max_length=50)
    deviceid = models.CharField(max_length=50)
    farmid = models.ForeignKey(Farm, on_delete = models.CASCADE)
    type = models.ForeignKey(Config, on_delete=models.CASCADE)
    status = models.ForeignKey(ChangeStatus, to_field='status', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pcbid


class BasicTest(models.Model):
    pcbid = models.ForeignKey(Device, on_delete=models.CASCADE)
    pcbboardversion = models.CharField(max_length=50)
    visualcheck = models.CharField(max_length=50)
    continuity = models.CharField(max_length=50)
    powersupply = models.CharField(max_length=50)
    atmega = models.CharField(max_length=50)
    esp32 = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pcbboardversion

class FunctionalTest(models.Model):
    pcbid = models.ForeignKey(Device, on_delete=models.CASCADE)
    pcbboardversion = models.CharField(max_length=50)
    espchipid = models.CharField(max_length=50)
    atmegachipid = models.CharField(max_length=50)
    rgbsingleled = models.CharField(max_length=50)
    ssrtrigger = models.CharField(max_length=50)
    waterlevel = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    rtctimecheck = models.CharField(max_length=50)
    rtctimecheckafterreset = models.CharField(max_length=50)
    rybvoltege = models.CharField(max_length=50)
    solenoidfeedback = models.CharField(max_length=50)
    triggerbutton = models.CharField(max_length=50)
    startingcurrent = models.CharField(max_length=50)
    loadoncurrent = models.CharField(max_length=50)
    loadoffcurrent = models.CharField(max_length=50)
    currentteststatus = models.CharField(max_length=50)
    espatmegacom = models.CharField(max_length=50)
    espled = models.CharField(max_length=50)
    espreset = models.CharField(max_length=50)
    atmegareset = models.CharField(max_length=50)
    atmegaresetbutton = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pcbboardversion

class AssemblyTest(models.Model):
    pcbid = models.ForeignKey(Device, on_delete=models.CASCADE)
    pcbboardversion = models.CharField(max_length=50)
    deviceid = models.CharField(max_length=50)
    wiring = models.CharField(max_length=50)
    continuity = models.CharField(max_length=50)
    esp32programming = models.CharField(max_length=50)
    atmegaprog = models.CharField(max_length=50)
    startertype = models.CharField(max_length=50)
    setconfig = models.CharField(max_length=50)
    selenoidtestfeedback = models.CharField(max_length=50)
    loadtest = models.CharField(max_length=50)
    rybcurrent = models.CharField(max_length=50)
    button = models.CharField(max_length=50)
    rtc = models.CharField(max_length=50)
    loadtesttimermin = models.CharField(max_length=50)
    loadtesttimeronoff = models.CharField(max_length=50)
    statusparam = models.CharField(max_length=50)
    errorcode = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pcbboardversion

class Shipping(models.Model):
    pcbid = models.ForeignKey(Device, on_delete=models.CASCADE)
    pcbboardversion = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    transport = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pcbboardversion

class Deployment(models.Model):
    pcbid = models.ForeignKey(Device, on_delete=models.CASCADE)
    farmid = models.ForeignKey(Farm, on_delete=models.CASCADE)
    application = models.CharField(max_length=50)
    hprange = models.CharField(max_length=50)
    dome = models.CharField(max_length=50)
    deviceid = models.CharField(max_length=50)
    operationtest = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.deviceid



