from odoo import fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Students in the school'
    _inherit = ['mail.thread']
    name = fields.Char('Name', required=True, tracking=True)
    date_of_birth = fields.Date('Date of Birth')