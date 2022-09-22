import unittest
from odoo.tests import tagged

from odoo_social.models import Partner

@tagged('post_install', '-at_install')
class TestResPartner(unittest.TestCase):
    def test_complete_profile(self):
        self.assertFalse(Partner._compute_complete_profile("", "", ""))
        self.assertTrue(Partner._compute_complete_profile("a", "a", "a"))


if __name__ == '__main__':
    unittest.main()
