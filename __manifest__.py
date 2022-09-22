# -*- coding: utf-8 -*-
{
    # Module Name
    'name': 'Odoo Social',
    
    # Module summary
    'summary': 'Odoo Social',
    
    # Module Descriptions
    'description': """
    Odoo Social.
    """,
    
    # Module author, license, category and version
    'author': "Kronos",
    'website': '',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'version': '1.0',
    
    # Any module necessary for this one to work correctly
    'depends': ['crm', 'website'],
    
    # Always loaded
    'data': [
        'views/res_partner_view.xml',
        'views/template.xml',
        'views/profile.xml',
    ],
    
    'application': False,
    'installable': True,
    'auto_install': False,
}
