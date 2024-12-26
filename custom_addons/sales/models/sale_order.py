from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    poem = fields.Char(string="Poem")
    # _description = 'Sales Order Custom'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            print(vals)
        return super().create(vals_list)

