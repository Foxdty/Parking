
from odoo import models,fields

class User(models.Model):
    _inherit ='res.users'
    _description='res'

    ticket_ids = fields.One2many(comodel_name='parking.ticket',inverse_name='user_id')
    

   
