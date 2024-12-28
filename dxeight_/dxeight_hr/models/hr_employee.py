# -*- coding: utf-8 -*-
# A product of DX-8, module restricted as per the license.
from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    pan_card = fields.Char(string='PAN Card',help='Capital letters are the upper-case')
    aadhaar_card = fields.Char(string='Aadhaar Card',help='12 Digit aadhaar card number.')
    address_home_id = fields.Many2one('res.partner', string='Address')

    @api.constrains('aadhaar_card')
    def _check_aadhaar_card(self):
        for record in self:
            if record.aadhaar_card and not re.match(r'^\d{12}$', record.aadhaar_card):
                raise ValidationError("Aadhaar Card number must be exactly 12 digits.")

    @api.constrains('pan_card')
    def _check_pan_card(self):
        for record in self:
            if record.pan_card and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', record.pan_card):
                raise ValidationError("PAN Card number must follow the format: 5 letters, 4 digits, and 1 letter.")

    @api.model_create_multi
    def create(self, vals):
        employees = super(HrEmployee, self).create(vals)
        for val in employees:
            if val.address_home_id:
                val.address_home_id.write({
                    'aadhaar_card': val.aadhaar_card,
                    'pan_card': val.pan_card,
                })
        return employees

    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        if 'aadhaar_card' in vals or 'pan_card' in vals:
            for employee in self:
                if employee.address_home_id:
                    employee.address_home_id.write({
                        'aadhaar_card': employee.aadhaar_card,
                        'pan_card': employee.pan_card,
                    })
        return res
