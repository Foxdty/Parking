from datetime import date
from email.policy import default
from pyparsing import Char
from odoo import fields,models,api

class parking_lot(models.Model):
    _name='parking.lot'
    _description='lot'
   
    

    
    name = fields.Char(string='Name')
    vehicle_id = fields.Many2many(comodel_name="parking.vehicle")
    
    pricelist_id = fields.Many2one(string='Pricelist',comodel_name='parking.pricelist') 

    ticket_ids = fields.One2many(comodel_name='parking.ticket',inverse_name='lot_id')
    working_hours = fields.Many2one(comodel_name='resource.calendar',string='Working hours',required=True)
    ticket_count = fields.Integer(compute='_ticket_count')

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
    
    @api.depends('ticket_ids')
    def _ticket_count(self):
        for record in self:
            tickets = self.env['parking.ticket'].search_count([('lot_id','=',record.id)])
            record.ticket_count = tickets
    def button_ticket(self):
        if len(self.vehicle_id) == 1:
            return{
            'name': ('Ticket'),
            'res_model': 'parking.ticket',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'domain': [('lot_id','=',self.id)],
            'context': {'default_lot_id':self.id, 'default_vehicle_id' : self.vehicle_id.id}
            } 
        return{
            'name': ('Ticket'),
            'res_model': 'parking.ticket',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'domain': [('lot_id','=',self.id)],
            'context': {'default_lot_id':self.id}
        }

