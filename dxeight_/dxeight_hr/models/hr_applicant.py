# -*- coding: utf-8 -*-
# A product of DX-8, module restricted as per the license.

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class HRApplicant(models.Model):
    _inherit = 'hr.applicant'

    current_ctc = fields.Float(string="Current CTC")
    expected_ctc = fields.Float(string="Expected CTC")
    feedback = fields.Text(string="Feedback")
    previous_organization = fields.Char(string="Previous Organization")
    notice_period_days = fields.Integer(string="Notice Period (Days)")

    aadhaar_card = fields.Char(string='Aadhaar Card',help='12 Digit aadhaar card number.')
    pan_card = fields.Char(string='PAN Card',help='Capital letters are the upper-case')
    previous_employer = fields.Char(string='Previous Employer')

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

    def _get_employee_create_vals(self):
        vals = super(HrApplicant, self)._get_employee_create_vals()
        partner = self.partner_id
        if partner:
            partner.write({
                'aadhaar_card': self.aadhaar_card,
                'pan_card': self.pan_card,
            })
        vals.update({
            'aadhaar_card': self.aadhaar_card,
            'pan_card': self.pan_card,
        })
        return vals