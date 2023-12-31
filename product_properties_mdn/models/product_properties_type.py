#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProductPropertiesType(models.Model):
    _inherit = "product.properties.type"

    def _get_default_currency_id(self, properties, field_name):
        # _logger.info(f"PRODUCT PROPERTIES {properties}:{field_name}")
        if isinstance(field_name, self.env["product.properties.type"].__class__):
            return properties.currency_id

        if field_name in properties._fields:
            return super()._get_default_currency_id(properties, field_name)

        if field_name[:4] == "mdbg" or field_name[:5] == "vmdbg":
            return properties.bg_currency_id
        elif field_name[:4] == "mdgr" or field_name[:5] == "vmdgr":
            return properties.gr_currency_id
        elif field_name[:4] == "mdcy" or field_name[:5] == "vmdcy":
            return properties.cy_currency_id

        return super()._get_default_currency_id(properties, field_name)
