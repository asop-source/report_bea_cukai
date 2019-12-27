# -*- coding: utf-8 -*-
{
    'name': "Report Bea Cukai",

    'summary': """
        Addons Bea Cukai

        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "asopkarawang@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Report',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/doc_mutasi_bahan_baku.xml',
        'views/doc_mutasi_barang_jadi.xml',
        'views/doc_mutasi_mesin_peralatan.xml',
        'views/doc_mutasi_reject_scrap.xml',
        'views/doc_pemasukan_barang.xml',
        'views/doc_pengeluaran_barang.xml',
        'views/doc_posisi_wip.xml',
        'views/master_data_doc.xml',
        'report/report_mutasi_bahan_baku.xml',
        'report/report_mutasi_barang_jadi.xml',
        'report/report_mutasi_mesin_peralatan.xml',
        'report/report_mutasi_reject_scrap.xml',
        'report/report_pemasukan_barang.xml',
        'report/report_pengeluaran_barang.xml',
        'report/report_posisi_wip.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}