from odoo import fields, models

class Customers(models.Model):

    _name = 'store.customer'
    _description = 'Customers'

    name = fields.Char('Customer Name', required=True)
    address = fields.Char('Customer Address', required=True)
    age = fields.Integer('Customer Age', required=True)
    date = fields.Date('Date of Delivery', required=True, default=fields.Datetime.now)
    state = fields.Selection(
        [
            ["draft", "Draft"],
            ["scheduled", "Scheduled"],
            ["delivered", "Delivered"],
            ["cancelled", "Cancelled"],
        ],
        default="draft", string="Customer State"
    )
    product_ids = fields.One2many('store.product.list', "customer_id", string='Product')

    def action_schedule(self):
        for recs in self:
            recs.state = "scheduled"

    def action_deliver(self):
        for recs in self:
            recs.state = "delivered"

    def action_cancel(self):
        for recs in self:
            recs.state = "cancelled"