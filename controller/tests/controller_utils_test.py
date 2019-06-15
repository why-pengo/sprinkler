from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import controller.utils as utils
from crontab import CronTab


class ControllerUtilsTests(StaticLiveServerTestCase):

    def test_ZoneMapInit_returnsTrue(self):
        self.assertTrue(utils.init_zone_map(), "Returns True on completion")

    def test_ReadCrontab_returnsCronTab(self):
        cron = utils.read_crontab()

        self.assertIsInstance(cron, CronTab)
