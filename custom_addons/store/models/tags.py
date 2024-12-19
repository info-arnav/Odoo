from odoo import fields, models

class Tag(models.Model):

    _name = 'store.tag'
    _description = 'Tags'

    name = fields.Char('Tag', required=True)