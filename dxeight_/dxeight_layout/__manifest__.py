# -*- coding: utf-8 -*-
# A prdouct of DX-8, module resricted as per the license.

{
    "name": "DX8 Sale",
    "version": "17.0.1.0.0",
    "category": "web",
    "sequence": "101",
    "summary": """Dx8 layout""",
    "description": """Dx8 layout""",
    'website': 'https://www.dxeight.com/odoo',
    "license": "LGPL-3",
    "depends": ["product_matrix","sale_management","account_accountant", "dxeight_account"],
    "data": [
        "views/dxeight_layout.xml",
        "data/layout_options.xml",
        "views/report_template.xml",
        "views/ir_action_report.xml",
    ],
    'assets': {
        'web.report_assets_common': [
            'dxeight_layout/static/src/**/*',
        ],
    },
    "installable": True,
}
