# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#Class to manage the Contacts
class Customers(http.Controller):

    #Route list to show all the contacts must be authenticated to see this
    @http.route('/list', type='http', auth="user", website=True, csrf=False)
    def list_customers(self):
        #Find all the partners who
        #
        #(partner_share) must be true
        #(active) the user must be active
        #
        customers = request.env["res.partner"].sudo().search([("partner_share", "=", True), ("active", "=", True)])

        #Return all contacts to the view
        #(customers) all the contacts
        return request.render(
            'odoo_social.website_list_customers',
            {'customers': customers})