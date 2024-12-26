from odoo import fields, models


class OrdersLogs(models.Model):
    _name = 'orders.logs'
    _description = 'Logs of updated and created orders'

    order_id = fields.Many2one('sale.order', string='Order')
    updated = fields.Datetime(string='Updated')