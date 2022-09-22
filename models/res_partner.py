# -*- coding: utf-8 -*-

from odoo import api, models, fields, modules
import base64

#Class to add the new attributes such as twitter profile, facebook profile and linkedin profile
class Partner(models.Model):
    _inherit = 'res.partner'

    #Social media Profiles url
    twitter = fields.Char('Twitter')
    facebook = fields.Char('Facebook')
    linkedin = fields.Char('Linkedin')
    
    #Computed field depending of twitter facebook linkedin to change the state to True
    #Used to show the profile incomplete filter (Contact search)
    complete_profile = fields.Boolean(compute='_compute_complete_profile', string='Complete Profile', store=True)
    
    
    #Dependencies of twitter facebook linkedin to change the state to True
    @api.depends('twitter', 'facebook', 'linkedin')
    def _compute_complete_profile(self):
        
        #Must find the fiels twitter facebook linkedin in self
        for l in self:  
            #If the three twitter facebook linkedin are not empty the profile is complete and change the image
            if l.twitter and l.facebook and l.linkedin:
                #Change to true the profile (Is complete)
                l.complete_profile = True
                
                #Change the image of contact to complete
                image = modules.get_module_resource('odoo_social', 'static/src/img', 'complete.png')
                self.image_1920 = base64.b64encode(open(image, 'rb').read())
            #If some of the social media are empty or at least one is change    
            else:
                #Change to false the profile (Is incomplete)
                l.complete_profile = False
                
                #Change the image of contact to incomplete
                image = modules.get_module_resource('odoo_social', 'static/src/img', 'incomplete.png')
                self.image_1920 = base64.b64encode(open(image, 'rb').read())
                 
