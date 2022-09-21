# -*- coding: utf-8 -*-

from odoo import api, models, fields

#Class to add the new attributes such as twitter profile, facebook profile and linkedin profile
class Partner(models.Model):
    _inherit = 'res.partner'

    #Social media Profiles url
    twitter = fields.Char('Twitter')
    facebook = fields.Char('Facebook')
    linkedin = fields.Char('Linkedin')
