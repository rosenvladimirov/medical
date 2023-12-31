# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import Command, api, fields, models

_logger = logging.getLogger(__name__)


class Picking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking", "patient.data.mixin"]

    partner_doctor_id = fields.Many2one(
        "res.partner",
        "Treating doctor",
        required=True,
        change_default=True,
        domain="[('is_company', '=', False)]",
    )

    def action_confirm(self):
        res = super().action_confirm()
        if res:
            self.patient_data_file_id.write(
                {"stock_picking_ids": [Command.set(self.ids)]}
            )
        return res

    def action_cancel(self):
        res = super().action_cancel()
        if res:
            old_ids = self.patient_data_file_id.stock_picking_ids - self
            self.patient_data_file_id.write(
                {"stock_picking_ids": [Command.set(old_ids.ids)]}
            )
        return res

    @api.onchange("partner_doctor_id")
    def _onchange_partner_doctor_id(self):
        for record in self:
            if record.partner_doctor_id:
                if record.sale_id:
                    sale_id = record.sale_id
                    sale_id.partner_doctor_id = record.partner_doctor_id.id
                if record.patient_data_file_id:
                    patient_data_file_id = record.patient_data_file_id
                    patient_data_file_id.partner_doctor_id = record.partner_doctor_id.id
                for line in record.move_ids:
                    invoices = line.sale_line_id.invoice_lines.move_id.filtered(
                        lambda r: r.move_type in ("out_invoice", "out_refund")
                    )
                    for invoice in invoices:
                        invoice.partner_doctor_id = record.partner_doctor_id.id

    def write(self, vals):
        self.ensure_one()
        if self.patient_data_file_id:
            values = self._write_update(vals)
            if values:
                self.patient_data_file_id.write(values)
        return super().write(vals)
