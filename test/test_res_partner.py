# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.tests.common import new_test_user
from odoo.tests import tagged

#Testing the creation of social media url
@tagged('standard', 'at_install')
class TestResPartner(TransactionCase):
    
    def test_social_media_create(self):
        #new test user
        test_user = new_test_user(self.env, login='test_user', groups='sales_team.group_sale_salesman')
        #new partner
        Partner = self.env['res.partner'].with_user(test_user)
        
        #testing the creation of 4 partners 3 with only 1 social media and 1 with the 3
        #test_partner_1, test_partner_2, test_partner_3 only 1 social media
        #test_partner_4 all social media
        test_partner_1 = Partner.create({'name': 'test_partner_1', 'twitter': 'twitter'})
        test_partner_2 = Partner.create({'name': 'test_partner_2', 'facebook': 'facebook'})
        test_partner_3 = Partner.create({'name': 'test_partner_3', 'linkedin': 'linkedin'})
        test_partner_4 = Partner.create({'name': 'test_partner_4', 'twitter': 'twitter', 'facebook': 'facebook', 'linkedin': 'linkedin'})
        
        #Checking is social media is created and the profile is not complete
        #Only the test_partner_4 has to be complete
        self.assertEqual(test_partner_1.twitter, "twitter")
        self.assertEqual(test_partner_1.complete_profile, False)
        self.assertEqual(test_partner_2.facebook, "facebook")
        self.assertEqual(test_partner_2.complete_profile, False)
        self.assertEqual(test_partner_3.linkedin, "linkedin")
        self.assertEqual(test_partner_3.complete_profile, False)
        self.assertEqual(test_partner_4.complete_profile, True)


