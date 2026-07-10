{
    'name': "estate module",
    'version': '0.1.0',
    'depends': ['base'],
    'author': "topiqnurrm",
    'category': 'Tutorials',
    'description': """
    ini adalah modul estate untuk tutorial odoo 19
    """,
    # data files always loaded at installation
    'data': [
        "security/ir.model.access.csv",
        'views/estate_property_action.xml',
        'views/estate_property_menu.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],

    "application": True,
    "auto_install": False,
}