{
    'name': 'Sales Custom',
    'version': '1.1',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': [
        "sale"
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/menu_views.xml",
        "views/sale_order_views.xml",
        "views/sale_portal_template.xml"],
    'license': 'LGPL-3',
}
