from ast import operator
from collections import Counter
from email.policy import default
from functools import reduce
from operator import add, itemgetter

from odoo import fields,models,api
class condition_report(models.TransientModel):
    _name='condition.report'
    _description='condition'
    

    from_date = fields.Date(string='From date',required=True)
    to_date = fields.Date(string='To date',required=True)
    vehicle_id = fields.Many2one(string='Vehicle Type',comodel_name='parking.vehicle')
    lot_id = fields.Many2one(string='Parking Lot',comodel_name='parking.lot')
   
    

    
    def get_report_values(self):
        print('test....',self.read()[0])
       
        domain=[]
        if self.from_date:
            domain+= [('time_in','>=',self.from_date)]
        if self.to_date:
            domain+=[('time_in','<=',self.to_date)]
        if self.vehicle_id:
            domain+=[('vehicle_id','=',self.vehicle_id.name)]
        if self.lot_id:
            domain+=[('lot_id','=',self.lot_id.name)]
            
        tickets = self.env['parking.ticket'].search_read(domain)
        print('ticket....',tickets)
        total_ticket = len(tickets)
        
        total_price = sum(map(itemgetter('price'),tickets))
        
        print('total...........',total_price)
        data={
            
            'form': self.read()[0],
            'tickets' : tickets,
            'total_price': total_price,
            'total_ticket': total_ticket
            

        }
        return  self.env.ref('parking.action_condition_report').sudo().report_action(self, data=data)

    def action_print_excel_report(self):
        domain=[]
        if self.from_date:
            domain+= [('time_in','>=',self.from_date)]
        if self.to_date:
            domain+=[('time_in','<=',self.to_date)]
        if self.vehicle_id:
            domain+=[('vehicle_id','=',self.vehicle_id.name)]
        if self.lot_id:
            domain+=[('lot_id','=',self.lot_id.name)]
            
        tickets = self.env['parking.ticket'].search_read(domain)
        total_ticket = len(tickets)
        total_price = sum(map(itemgetter('price'),tickets))
        data={
            
            'form': self.read()[0],
            'tickets' : tickets,
            
            'total_price': total_price,
            'total_ticket': total_ticket

            }

        return  self.env.ref('parking.action_condition_report_xlsx').sudo().report_action(self, data=data)

      



