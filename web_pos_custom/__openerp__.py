{
    'name': 'Web Point of Sale',
    'category': 'Hidden',
    'description': """
OpenERP Point of sale Custimize.
==========================

        """,
    'version': '2.0',
    'depends':['point_of_sale'],
    'data' : [
        'views/web_pos_custom.xml',
        'views/pos_extend.xml',
    ],
    'qweb': ['static/src/xml/web_pos_custom.xml'],
    'auto_install': False,
}
