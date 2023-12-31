# Copyright 2023 Rosen Vladimirov, BioPrint Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Product Set Mdn",
    "summary": """
        Add mdn data in product set""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "website": "https://github.com/rosenvladimirov/medical",
    "author": "Rosen Vladimirov, BioPrint Ltd.,Odoo Community Association (OCA)",
    "depends": [
        "product_set",
        "product_properties",
        "product_properties_mdn",
        "product_properties_product_set",
    ],
    "data": [
        "views/product_set.xml",
    ],
    "demo": [],
}
