# -*- coding: utf-8 -*-
{
    'name': "vit_dynamic_sequence",

    'summary': """
        Add %(company)s %(unit)s %(location)s on sequence for 
        Company code, Department code, Account analytic code""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'hr',
                'sale',
                'purchase',
                'account',
                'vit_employee_analytic',
                'project',
                'vit_project_rab_inherit',
                'vit_bakn',
                'vit_budget_cut',
                'vit_budget_relokasi',
                'vit_uudp',
                'purchase_requisition',
                'hr_payroll',
                'vit_product_request',
                'stock',
            ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/company.xml',
        'views/department.xml',
        'views/analytic_tag.xml',
        'views/templates.xml',
        'data/ir_sequence_so.xml',
        'data/ir_sequence_po.xml',
        'data/ir_sequence_project.xml',
        'data/ir_sequence_budget_cut.xml',
        'data/ir_sequence_budget_relokasi.xml',
        'data/ir_sequence_uudp_pengajuan.xml',
        'data/ir_sequence_uudp_pertanggungjawaban.xml',
        'data/ir_sequence_purchase_requisition.xml',
        'data/ir_sequence_ap.xml',
        'data/ir_sequence_ar.xml',
        'data/ir_sequence_misc_journal.xml',
        'data/ir_sequence_payroll.xml',
        'data/ir_sequence_bakn.xml',
        'data/ir_sequence_pr.xml',
        'data/ir_sequence_receive.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}