{
    'name': 'Dxeight HR',
    'version': '1.0',
    'summary': 'Custom module for HR related customization',
    'description': 'Custom module for HR related customization',
    'author': 'DX8',
    'category': 'Human Resources',
    'depends': ['hr_recruitment'],
    'data': [
        'views/hr_applicant_views.xml',
        'views/res_partner_views.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'license' : 'LGPL-3',
}
