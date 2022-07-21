from datetime import date
from email.policy import default
from pyparsing import Char
from odoo import fields,models,api

class parking_lot(models.Model):
    _name='parking.lot'
    _description='lot'
   
    

    
    name = fields.Char(string='Name')
    vehicle_id = fields.Many2one(comodel_name="parking.vehicle")
    limit_vehicle=fields.Integer(string='Limit Vehicle')
    pricelist_id = fields.Many2one(string='Pricelist',comodel_name='parking.pricelist') 
    time_begin = fields.Datetime(string='Start time')
    time_end = fields.Datetime(string='End time')
    ticket_id = fields.Many2one(comodel_name='parking.ticket')
    working_hours = fields.Many2one(comodel_name='resource.calendar',string='Working hours',required=True)


    _sql_constraints=[('unique_name','unique(name)','The name is unique')]


    def active(self):
        return{
            'name': ('Ticket'),
            'res_model': 'parking.ticket',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'domain': [('lot_id','=',self.id)],
            'context': {'search_default_sate_filter_unpaid':1}
        }
    

        

