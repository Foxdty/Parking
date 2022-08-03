from email.policy import default
from odoo import models, fields,api
from odoo.exceptions import ValidationError

class Park_Vehicle(models.Model):
    _name = 'parking.limit'
    _description = 'limit'

    lot_id = fields.Many2one('parking.lot',string = 'Parking Lot')
    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle',default='')
    limit = fields.Integer(string = 'Limit Vehicle')

    # ---------------------
    @api.onchange('lot_id')
    def _parking_lot(self):
        domain=[]
        if self.lot_id:
            lot = self.env['parking.lot'].search([('id','=',self.lot_id.id)])
            print('lot.............',lot.vehicle_id)
            for x in lot.vehicle_id:
                domain.append(x.id)
            return {'domain': {'vehicle_id': [('id','in',domain)]}}
 
        

