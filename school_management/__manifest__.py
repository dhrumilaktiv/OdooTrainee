# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '14.0.1.0.0',
    'category': '',
    'summary': 'Student details',
    'description': """
This module contains all the common details of student.
    """,
    'depends': ['base',],
    'data': [
        'data/school_management_data.xml',
        'security/school_management_security.xml',
        'security/ir.model.access.csv',
        'views/student_info.xml',
        'views/teacher_info.xml',
        'views/res_partner_view.xml',
        'views/sports_info.xml',
        'views/event_participants.xml',
        
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True
}