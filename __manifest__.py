# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Parking',
    'version': '1.2',
    'category': 'Sales/Parking',
    'sequence': 1,
    'summary': ' opportunities',
    'description': "",
    'license': 'OEEL-1',
    'website': '',
    'depends': [
        'base',
        'report_xlsx',
        'hr',
        
        
        
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/parking_menu.xml',
        'views/parking_lot_view.xml',
        'views/parking_vehicle_view.xml',
        'views/parking_ticket_view.xml',
        'views/parking_pricelist_view.xml',
        'views/res_user_view.xml',
        'views/parking_lot_working_hours.xml',
        'report/condition_report.xml',
        'report/condition_template.xml',
        'report/report_view.xml',
        'report/xlsx_report_view.xml',
        
        
       
        
        
    ],
    "demo": [
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}