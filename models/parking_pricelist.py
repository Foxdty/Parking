from odoo import fields,models
class parking_pricelist(models.Model):
    _name='parking.pricelist'
    _description='pricelist'

    name=fields.Char(string='Name')
    item_ids = fields.One2many(string='Item',comodel_name='parking.pricelist.item',inverse_name='pricelist_id')
    _sql_constraints=[('unique_name','unique(name)','The name is unique')]