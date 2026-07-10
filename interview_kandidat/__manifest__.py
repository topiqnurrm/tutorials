{
    'name': 'Interview Kandidat',
    'version': '0.1.0',
    'depends': ['base'],
    'author': 'topiqnurrm',
    'category': 'project penilaian kandidat interview',
    'description': """
        module untuk menilai kandidat interview
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/interview_kandidat_action.xml',
        'views/interview_kandidat_menu.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    "application": True,
    "auto_install": False,
}