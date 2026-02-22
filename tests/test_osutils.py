import os
import unittest

from src.osutils import TempPcapHandler


class TestTempPcapHandler(unittest.TestCase):

    def setUp(self) -> None:

        self.temp_pcap_dir = "/tmp/pcaptest"
        return super().setUp()

    def test_constructor(self):
        temp_pcap_handler = TempPcapHandler(self.temp_pcap_dir, rotate_every_t_seconds=10)
        self.assertTrue(os.path.exists(self.temp_pcap_dir))

    def test_cleanup(self):

        temp_pcap_handler = TempPcapHandler(self.temp_pcap_dir, rotate_every_t_seconds=10)
        with open(os.path.join(self.temp_pcap_dir, "test.pcap"), "wb") as f:
            ## NOTE: Writes an empty pcap file
            f.write(b'\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00')

        self.assertTrue("test.pcap" in os.listdir(self.temp_pcap_dir))
        temp_pcap_handler.clean_pcap_files()
        self.assertFalse("test.pcap" in os.listdir(self.temp_pcap_dir))

    def tearDown(self) -> None:
        return super().tearDown()
