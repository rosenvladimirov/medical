#  Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _prepare_procurement_values(self, group_id=False):
        values = super()._prepare_procurement_values(group_id=group_id)
        values.update(
            {
                "patient_data_file_id": self.order_id.patient_data_file_id.id,
                "patient_partner_id": self.order_id.patient_partner_id.id,
            }
        )
        return values
