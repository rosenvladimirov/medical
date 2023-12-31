#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProductPropertiesType(models.Model):
    _name = "product.properties.type"

    def _get_statistic_prop(self, record):
        if record._name == "patient.data":
            return record
        return super()._get_statistic_prop(record)
