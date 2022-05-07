import time
import gpiozero
import click
import warnings
from loguru import logger
from rich import Console
from rich.table import Table

warnings.simplefilter('ignore')

# zone   = bcm   pin
zones = dict()
zones[1] = 17  # 11  gpio0
zones[2] = 18  # 12  gpio1
zones[3] = 27  # 13  gpio2
zones[4] = 22  # 15  gpio3
zones[5] = 23  # 16  gpio4
zones[6] = 24  # 18  gpio5
zones[7] = 25  # 22  gpio6
zones[8] = 4   # 7   gpio7


@click.command()
@click.option("--zone", default=2, help="Zone to test.")
def test_zone(zone):
    """Test by running a given zone for 40 seconds"""
    bcm = zones[zone]
    # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
    relay = gpiozero.OutputDevice(pin=bcm, active_high=False)
    logger.debug(f"bcm value = {relay.value}")
    logger.debug(f"pin/bcm = {bcm} to OUTPUT/OFF")

    relay.on()
    logger.debug(f"bcm value = {relay.value}")
    time.sleep(40)
    relay.off()
    logger.debug(f"bcm value = {relay.value}")


def read_zones():
    """Read the current state of the zones and display"""
    table = Table(title="Zone status")
    table.add_column("Zone", justify="right", style="cyan", no_wrap=True)
    table.add_column("BCM", style="magenta")
    table.add_column("On/Off", justify="right", style="green")
    for zone in zones:
        bcm = zones[zone]
        relay = gpiozero.OutputDevice(pin=bcm, active_high=False)
        table.add_row(zone, bcm, relay.value)

    console = Console()
    console.print(table)


if __name__ == '__main__':
    read_zones()
