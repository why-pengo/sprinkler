import time
import gpiozero
from loguru import logger

"""
    zone  BCM  pin gpio
zoneMap[1] = 17  # 11 gpio0
zoneMap[2] = 18  # 12 gpio1
zoneMap[3] = 27  # 13 gpio2
zoneMap[4] = 22  # 15 gpio3
zoneMap[5] = 23  # 16 gpio4
zoneMap[6] = 24  # 18 gpio5
zoneMap[7] = 25  # 22 gpio6
zoneMap[8] = 4   # 7 gpio7
"""

bcm = 18
gpio = 1
# (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
relay = gpiozero.OutputDevice(pin=bcm, active_high=False)
logger.debug(f"bcm value = {relay.value}")
logger.debug(f"pin/bcm = {bcm} to OUTPUT/OFF")

relay.on()
logger.debug(f"bcm value = {relay.value}")
time.sleep(40)
relay.off()
logger.debug(f"bcm value = {relay.value}")
