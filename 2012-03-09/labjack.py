import time
import ue9

jack = ue9.UE9()
outp = 0xAA

while True:
    jack.feedback(FIOMask=0xFF, FIODir=0xFF, FIOState=outp)
    time.sleep(0.5)
    jack.feedback(FIOMask=0xFF, FIODir=0xFF, FIOState=~outp)
    time.sleep(0.5)

