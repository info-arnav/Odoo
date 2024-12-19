from odoo import fields, models, api

class Products(models.Model):

    _name = 'store.product'
    _description = 'Products'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Product', required=True)
    reference = fields.Char(string='Reference', default="New")
    description = fields.Text('Description')
    price = fields.Float('Price', digits=(16, 2))
    tag_ids = fields.Many2many('store.tag', "customer_tag_rel", "customer_id", "tag_id", string='Tags')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("reference") or vals["reference"] == "New":
                vals["reference"] = self.env["ir.sequence"].next_by_code("store.product")
        return super().create(vals_list)

class ProductsList(models.Model):

    _name = 'store.product.list'
    _description = 'Products List'

    name = fields.Many2one("store.product", string="Product")
    quantity = fields.Float("Quantity", digits=(16, 2))
    customer_id = fields.Many2one("store.customer", string="Customer")
