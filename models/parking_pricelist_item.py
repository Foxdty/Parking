from odoo import fields,models
class parking_pricelist_item(models.Model):
    _name='parking.pricelist.item'
    _description='pricelist.item'

    vehicle_id = fields.Many2one(string='Vehicle',comodel_name='parking.vehicle')
    price = fields.Integer(string='Price',default=0)
    pricelist_id = fields.Many2one(comodel_name='parking.pricelist')
