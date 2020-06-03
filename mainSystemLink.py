#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import ubinascii, ujson, urequests, utime
import password

#Key from another python script
Key = 'G375AkeRsKSzMop1HOvumDGIU96LIhNHwzk7w_Qp_g'

#SystemLink functions
def SL_setup():
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    return urlBase, headers
     
def Put_SL(Tag, Type, Value):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = urequests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply

def Get_SL(Tag):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current"
    try:
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        #print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result
     
def Create_SL(Tag, Type):
    urlBase, headers = SL_setup()
    urlTag = urlBase + Tag
    propName={"type":Type,"path":Tag}
    try:
        urequests.put(urlTag,headers=headers,json=propName).text
    except Exception as e:
        print(e)

Create_SL('Testing','BOOLEAN')
Put_SL('Testing', 'BOOLEAN', 'true')
test = Get_SL('Testing')

print(test)