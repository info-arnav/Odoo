import odoo

import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.fields import Command
from odoo.http import request


from odoo.addons.sale.controllers.portal import CustomerPortal


class CustomerPortalCustom(CustomerPortal):
    @http.route(['/my/orders/<int:order_id>'], type='http', auth="public", website=True)
    def portal_order_page(
            self,
            order_id,
            report_type=None,
            access_token=None,
            message=False,
            download=False,
            downpayment=None,
            **kw
    ):
        print("running")
        return super().portal_order_page(order_id,
            report_type,
            access_token,
            message,
            download,
            downpayment)
