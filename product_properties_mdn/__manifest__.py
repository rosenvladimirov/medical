# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Medical device nomenclature",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "category": "Sales",
    "summary": """
    Added support for medical device nomenclature base on product properties module
    """,
    "website": "https://github.com/rosenvladimirov/medical",
    "author": "Rosen Vladimirov,Odoo Community Association (OCA)",
    "depends": [
        "product",
        "product_properties",
        "queue_job",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/mdn_codes_data.xml",
        "views/medical_properties.xml",
        "views/product_properties_views.xml",
        "views/product_views.xml",
        "views/product_template_views.xml",
        "views/account_move_view.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
    ],
    "demo": [],
    "installable": True,
}
