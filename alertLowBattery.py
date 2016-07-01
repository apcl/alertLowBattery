#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import time
import sl4a

droid = sl4a.Android()
time.sleep(1)
#setea el nivel de batería en que se alertará
alerta = 20
while True:
      droid.batteryStartMonitoring()
      status = droid.batteryGetLevel()
      level = int (status [1])
      if (level <= alerta):
          droid.ttsSpeak ('bateria baja')
      droid.batteryStopMonitoring()
      time.sleep (5)



