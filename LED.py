import time
from pynq.overlays.base import BaseOverlay

base = BaseOverlay("base.bit")
led0 = base.leds[0]

for i in range(5):
    led0.on()
    time.sleep(0.5)
    led0.off()
    time.sleep(0.5)