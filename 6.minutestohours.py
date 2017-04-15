# -*- coding: utf-8 -*-
def mTOh(minutes):
    hours = int(minutes/60)
    return hours

def sTOh(seconds):
    hours1 = int(seconds/3600)
    return hours1


minutes = int(input ("Enter Minutes: "))
seconds = int(input ("Enter Seconds: "))
print (("Conversion of %d to hours : "  %minutes) mTOh())
print ("Conversion of %d to hours : " %seconds)
