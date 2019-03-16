from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import controller.utils as utils


class ControllerUtilsTests(StaticLiveServerTestCase):

    def test_ZoneMapInit_returnsTrue(self):
        self.assertTrue(utils.init_zone_map(), "Returns True on completion")
