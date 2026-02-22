import unittest

from src.network import check_existing_network_interface


class TestCheckExistingNetworkInterfaces(unittest.TestCase):

    def test_loopback_if(self):

        self.assertTrue(check_existing_network_interface("lo"))

    def test_invalid_if(self):

        try:
            check_existing_network_interface("this_if_does_not_3xist")
            self.fail("Invalid interface did not raise an exception.")
        except ValueError:
            pass

        except:
            self.fail("Invalid interface raise an exception but not a ValueError")
