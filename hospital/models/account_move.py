#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "patient.data.mixin"]

    partner_doctor_id = fields.Many2one(
        "res.partner",
        "Treating doctor",
        required=True,
        change_default=True,
        domain="[('is_company', '=', False)]",
    )

    @api.onchange("partner_doctor_id")
    def _onchange_partner_doctor_id(self):
        for record in self:
            if record.partner_doctor_id:
                if record.patient_data_file_id:
                    patient_data_file_id = record.patient_data_file_id
                    patient_data_file_id.partner_doctor_id = record.partner_doctor_id.id
                for line in record.invoice_line_ids:
                    sales = line.sale_line_ids
                    for sale in sales.mapped("order_id"):
                        sale.partner_doctor_id = record.partner_doctor_id.id
                        for picking_id in sale.picking_ids:
                            picking_id.doctor_id = record.partner_doctor_id.id

    def write(self, vals):
        self.ensure_one()
        if self.patient_data_file_id:
            values = self._write_update(vals)
            if values:
                self.patient_data_file_id.write(values)
        return super().write(vals)
