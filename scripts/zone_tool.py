import time
import gpiozero
import gpiozero.pins.rpigpio
import click
import warnings
from loguru import logger
from rich.console import Console
from rich.table import Table

# zone   = bcm   pin
zones = dict()
zones[1] = 17  # 11  gpio0
zones[2] = 18  # 12  gpio1
zones[3] = 27  # 13  gpio2
zones[4] = 22  # 15  gpio3
zones[5] = 23  # 16  gpio4
zones[6] = 24  # 18  gpio5
zones[7] = 25  # 22  gpio6
zones[8] = 4  # 7   gpio7


@click.command()
@click.option("--zone", help="Zone to turn on.")
def zone_on(zone):
    """Turn on a given zone"""
    if zone:
        bcm = zones[int(zone)]
        # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
        relay = gpiozero.OutputDevice(
            pin=bcm,
            initial_value=None,
            pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
            active_high=False
        )
        logger.debug(f"bcm value = {relay.value}")
        logger.debug(f"pin/bcm = {bcm} to OUTPUT/OFF")

        relay.on()
        logger.debug(f"bcm value = {relay.value}")


@click.command()
@click.option("--zone", help="Zone to turn off.")
def zone_off(zone):
    """Turn off a given zone"""
    if zone:
        bcm = zones[int(zone)]
        # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
        relay = gpiozero.OutputDevice(
            pin=bcm,
            initial_value=None,
            pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
            active_high=False
        )
        logger.debug(f"bcm value = {relay.value}")
        logger.debug(f"pin/bcm = {bcm} to OUTPUT/OFF")

        relay.off()
        logger.debug(f"bcm value = {relay.value}")


@click.command()
@click.option("--zone", default=2, help="Zone to test.")
def test_zone(zone):
    """Test by running a given zone for 40 seconds"""
    bcm = zones[int(zone)]
    # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
    relay = gpiozero.OutputDevice(
        pin=bcm,
        initial_value=None,
        pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
        active_high=False
    )
    logger.debug(f"bcm value = {relay.value}")
    logger.debug(f"pin/bcm = {bcm} to OUTPUT/OFF")

    relay.on()
    logger.debug(f"bcm value = {relay.value}")
    time.sleep(40)
    relay.off()
    logger.debug(f"bcm value = {relay.value}")


@click.command()
def read_zones():
    """Read the current state of the zones and display"""
    table = Table(title="Zone status")
    table.add_column("Zone", justify="right", style="cyan", no_wrap=True)
    table.add_column("BCM", style="magenta")
    table.add_column("On[1]/Off[0]", justify="right", style="green")
    for zone in zones:
        bcm = zones[zone]
        relay = gpiozero.OutputDevice(
            pin=bcm,
            initial_value=None,
            pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
            active_high=False
        )
        table.add_row(str(zone), str(bcm), str(relay.value))

    console = Console()
    console.print(table)


def close(self):
    """This function is a workaround for gpiozero's cleanup on close resetting pins state"""
    # https://github.com/gpiozero/gpiozero/issues/707
    pass


@click.group(help="Zone tools")
def cli():
    pass


gpiozero.pins.rpigpio.RPiGPIOPin.close = close
cli.add_command(read_zones)
cli.add_command(test_zone)
cli.add_command(zone_on)
cli.add_command(zone_off)

if __name__ == '__main__':
    cli()
