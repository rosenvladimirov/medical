# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import Command, api, fields, models

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "patient.data.mixin"]

    partner_doctor_id = fields.Many2one(
        "res.partner",
        "Treating doctor",
        required=True,
        change_default=True,
        domain="[('is_company', '=', False)]",
    )

    @api.model_create_multi
    def create(self, vals_list):
        patient_data_ids = list(
            filter(
                lambda r: r not in self.ignore_fields(),
                self.env["patient.data"]._fields,
            )
        )
        for vals in vals_list:
            if "partner_doctor_id" not in vals:
                partner = self.env["res.partner"].browse(vals.get("partner_id"))
                if partner:
                    vals["partner_doctor_id"] = (
                        partner.child_ids
                        and partner.mapped("child_ids")[0].id
                        or partner.id
                    )

            if (
                any([x in vals for x in patient_data_ids])
                and "patient_data_file_id" not in vals
            ):
                patient_data_file_id = self.env["patient.data"].create(
                    self.patient_data(self, vals)
                )
                vals["patient_data_file_id"] = patient_data_file_id.id
        return super().create(vals_list)

    def write(self, vals):
        self.ensure_one()
        if not self.patient_data_file_id:
            patient_data_file_id = self.env["patient.data"].create(
                self.patient_data(self, vals)
            )
            vals["patient_data_file_id"] = patient_data_file_id.id
            for picking_id in self.picking_ids:
                picking_id.patient_data_file_id = patient_data_file_id
            for invoice_id in self.invoice_ids:
                invoice_id.patient_data_file_id = patient_data_file_id
        else:
            values = self._write_update(vals)
            if values:
                self.patient_data_file_id.write(values)
        return super().write(vals)

    def view_static_properties(self):
        action = self.env.ref(
            "product_properties.product_properties_static_action"
        ).read()[0]
        action.update(
            {"domain": [("object_id", "in", ["sale.order,%s" % x.id for x in self])]}
        )
        return action

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        self.ensure_one()
        invoice_vals.update(
            {
                "patient_data_file_id": self.patient_data_file_id.id,
                "partner_doctor_id": self.partner_doctor_id.id,
                # 'payment_deal_id': self.payment_deal_id.id,
                "icd11_id": self.icd11_id.id,
            }
        )
        return invoice_vals

    def action_confirm(self):
        res = super().action_confirm()
        for record in self:
            record.patient_data_file_id.write({"order_ids": [Command.set(record.ids)]})
        return res
