# -*- coding: utf-8 -*-

from odoo import api, models, fields

#Class to add the new attributes such as twitter profile, facebook profile and linkedin profile
class Partner(models.Model):
    _inherit = 'res.partner'

    #Social media Profiles url
    twitter = fields.Char('Twitter')
    facebook = fields.Char('Facebook')
    linkedin = fields.Char('Linkedin')
    complete_profile = fields.Boolean(compute='_compute_complete_profile', string="Complete profile", store=True)
    
    @api.depends('twitter','facebook','linkedin')
    def _compute_complete_profile(self):
        if twitter == "" and facebook == "" and linkedin == "":
            self.complete_profile = True
        else:
            self.complete_profile = False
