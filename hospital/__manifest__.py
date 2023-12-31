# Copyright 2023 Rosen Vladimirov, BioPrint Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Hospital",
    "summary": """
        Patient data and used medical devices.""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "website": "https://github.com/rosenvladimirov/medical",
    "author": "Rosen Vladimirov, BioPrint Ltd.,Odoo Community Association (OCA)",
    "depends": [
        "base",
        "sale",
        "stock",
        "hr",
        "partner_identification",
        "product_properties",
        "partner_contact_birthdate",
        "product_properties_mdn",
        "stock_location_consignment_owner",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "views/patient_data_views.xml",
        "views/res_partner_view.xml",
        "views/stock_picking_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_view.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
}
