from tkinter.font import BOLD
from odoo import models
class condition_report_xlsx(models.AbstractModel):
    _name = 'report.parking.template_id_xlsx'
    _inherit = 'report.report_xlsx.abstract'  



    def generate_xlsx_report(self, workbook, data, partners):
        print('1...................',data)
        print('2...................',partners)
        sheet = workbook.add_worksheet('Report')
        bold = workbook.add_format({'bold': True})
        sheet.write(0,0,'From date',bold)
        sheet.write(0,1,str(partners.from_date),bold)
        sheet.write(1,0,'To date',bold)
        sheet.write(1,1,str(partners.to_date),bold)
        print('4...................',partners.from_date)
        print('5...................',partners.to_date)
        sheet.write(3,0,'Code',bold)
        sheet.write(3,1,'Vehicle Type',bold)
        sheet.write(3,2,'Parking Lot',bold)
        sheet.write(3,3,'Price',bold)
        col = 0
        row = 3
        for obj in data['tickets']:
            row+=1
            sheet.write(row,col,obj['name'])
            sheet.write(row,col+1,obj['vehicle_id'][1])
            sheet.write(row,col+2,obj['lot_id'][1])
            sheet.write(row,col+3,obj['price'])
        
        sheet.write(row+2,col,'total ride:',bold)
        sheet.write(row+2,col+2,data['total_ticket'],bold)
        sheet.write(row+3,col,'total price:',bold)
        sheet.write(row+3,col+2,data['total_price'],bold)
            

