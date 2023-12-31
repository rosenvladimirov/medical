# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    mdgr_observe_code = fields.Char(
        related="product_tmpl_id.product_prop_static_id.mdgr_observe_code"
    )
    mdgr_observe_price = fields.Monetary(
        related="product_tmpl_id.product_prop_static_id.mdgr_observe_price",
        currency_field="currency_id",
    )
    vmdgr_observe_code = fields.Char(
        related="product_id.product_prop_static_id.mdgr_observe_code"
    )
    vmdgr_observe_price = fields.Monetary(
        related="product_id.product_prop_static_id.mdgr_observe_price",
        currency_field="currency_id",
    )
