"""Basic smoke tests for device discovery helpers."""

import unittest
from src.protocols.ssdp import SSDP_SEARCH, SSDP_ADDR, SSDP_PORT


class TestSSDPConstants(unittest.TestCase):
    def test_multicast_address(self):
        self.assertEqual(SSDP_ADDR, "239.255.255.250")

    def test_port(self):
        self.assertEqual(SSDP_PORT, 1900)

    def test_search_target(self):
        self.assertIn("urn:dial-multiscreen-org", SSDP_SEARCH)

    def test_search_method(self):
        self.assertTrue(SSDP_SEARCH.startswith("M-SEARCH"))


if __name__ == "__main__":
    unittest.main()
