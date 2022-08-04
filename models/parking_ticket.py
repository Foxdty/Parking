
from datetime import date,datetime
from re import S
import pytz
from decimal import ROUND_UP
from email.policy import default
import math

from xml import dom


from odoo import fields,models,api
from odoo.tools import image
from odoo.exceptions import ValidationError
class parking_ticket(models.Model):
    _name='parking.ticket'
    _description='ticket'

    name= fields.Char(default='New',readonly=True)
    image = fields.Binary()
    vehicle_id = fields.Many2one(comodel_name="parking.vehicle",default=None,required=True)
    time_in = fields.Datetime(string='Time In',default= lambda self: fields.Datetime.now(),readonly=True)
    time_out = fields.Datetime(string='Time Out',readonly=True)
    total_time = fields.Char(string='Total Time', readonly=True)
    remaining_parking_spaces = fields.Integer(readonly=True)
    lot_id = fields.Many2one(comodel_name='parking.lot',required=True)
    state = fields.Char(default='in')
    
    

    user_id = fields.Many2one(comodel_name='res.users',string='Employee',default= lambda self: self.env.user,readonly=True)
    

    
    price = fields.Integer(string='Price',default=0,readonly=True)



    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
           'self.service') + str(fields.Date.today().day) + str(fields.Date.today().month) + str(fields.Date.today().year) or 'New'

        limit = self.env['parking.lot'].browse(vals['lot_id'])
        show_limit = self.env['parking.limit'].search([('lot_id','=',vals['lot_id']),('vehicle_id','=',vals['vehicle_id'])])
        
        if show_limit.limit == 0:
            raise ValidationError('The parking lot is full')
        show_limit.limit -=1

        
        hcm = pytz.timezone('Asia/Ho_Chi_Minh')
        time_now = datetime.now(hcm).hour 
        minute = (datetime.now().minute) / 60
        time = time_now + minute
        
       
        date1 = str(date.weekday(date.today()))

        working_time = self.env['resource.calendar.attendance'].search([('dayofweek','=',date1),('calendar_id','=',limit.working_hours.id)])
        
        if not working_time:
            raise ValidationError('Parking %s outside working hours'%(limit.name))
        for x in working_time:
   
            if (time < x.hour_from) and (time > x.hour_to):
                raise ValidationError('Parking %s outside working hours'%(limit.name))
        
        test = self.env['parking.lot']
        
        result = super().create(vals)
        return result
    
    def Timeline(self):

        self.state = 'out'
        time_now = fields.Datetime.now()
        self.time_out = time_now
        time = time_now - self.time_in
        duration_second = time.total_seconds()  
        minutes = divmod(duration_second, 60)[0] 
        hours = divmod(duration_second, 3600)[0]+round((minutes%60)/60,2)
        
        round_hours =round(hours)

        price_ticket = self.env['parking.pricelist.item'].search([('pricelist_id','=',self.lot_id.pricelist_id.id),('vehicle_id','=',self.vehicle_id.id)])

        if self.price != 0:
            raise ValidationError('Ride has been out')
        if round_hours > 0:
            if round_hours>hours:
                self.total_time = str(round_hours)+'h'
                self.price = price_ticket.price * round_hours

            elif round_hours < hours:
                self.total_time = str(hours)+ "h"
                self.price = price_ticket.price * hours

        else:
            self.total_time = str(minutes)+'m'
            self.price = price_ticket.price * (round(minutes/60,2))
        
        show_limit = self.env['parking.limit'].search([('lot_id','=',self.lot_id.id),('vehicle_id','=',self.vehicle_id.id)])
        show_limit.limit +=1
        

    @api.onchange('vehicle_id')
    def _parking_vehicle(self):
        show_limit = self.env['parking.limit'].search([('lot_id','=',self.lot_id.id),('vehicle_id','=',self.vehicle_id.id)])
     
        self.remaining_parking_spaces = show_limit.limit 

    @api.onchange('lot_id')
    def _parking_lot(self):
        domain=[]
        if self.lot_id:
            lot = self.env['parking.lot'].search([('id','=',self.lot_id.id)])
        
            for x in lot.vehicle_id:
                domain.append(x.id)
            return {'domain': {'vehicle_id': [('id','in',domain)]}}




