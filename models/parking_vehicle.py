from calendar import c
from odoo import fields,models
class parking_vehicle(models.Model):
    _name="parking.vehicle"
    _description="vehicle"

    name=fields.Char(string='Name')
    lot_ids = fields.One2many(string='parking lot',comodel_name='parking.lot',inverse_name='vehicle_id')
    park_veh_ref = fields.One2many('parking.limit','vehicle_id',string = 'Parking Vehicle')
    _sql_constraints=[('unique_name','unique(name)','The name is unique')]
    