# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        vals = super()._get_new_picking_values()
        vals[
            "patient_data_file_id"
        ] = self.sale_line_id.order_id.patient_data_file_id.id
        if self.sale_line_id.order_id.partner_doctor_id:
            vals["partner_doctor_id"] = (
                self.sale_line_id.order_id.partner_doctor_id.id,
            )
        return vals
