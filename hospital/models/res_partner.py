#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import re

from odoo import _, api, fields, models
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    medical_type = fields.Selection(
        selection=[
            ("standard", _("No Medical Type")),
            ("hospital", _("Hospital")),
            ("patient", _("Patient")),
            ("doctor", _("Doctor")),
        ],
        default="standard",
    )
    patient_data_file_id = fields.One2many(
        "patient.data", "patient_partner_id", "Patient"
    )
    patient_name = fields.Char("Patient Alias")
    doctor_rank = fields.Integer(default=0, copy=False)

    @property
    def _order(self):
        res = super()._order
        partner_search_mode = self.env.context.get("res_partner_search_mode")
        if partner_search_mode != "doctor":
            return res
        order_by_field = f"{partner_search_mode}_rank DESC"
        return f"{order_by_field}, {res}" if res else order_by_field

    @api.onchange("name")
    def _change_partner_patient_id(self):
        delimiters = ",", ".", " "
        regex_pattern = "|".join(map(re.escape, delimiters))
        if not self.patient_name and self.name:
            self.patient_name = (
                ". ".join(
                    [x[0].upper() for x in re.split(regex_pattern, self.name) if x]
                )
                + "."
            )

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        domain = []
        if name:
            partner_patient = self.env["res.partner"].search(
                [("name", "=ilike", name + "%")]
            )
            if partner_patient:
                domain = [
                    "|",
                    "|",
                    ("patient_name", "=ilike", name + "%"),
                    ("partner_patient_id", "in", partner_patient.ids),
                    ("name", operator, name),
                ]
            else:
                domain = [
                    "|",
                    ("patient_name", "=ilike", name + "%"),
                    ("name", operator, name),
                ]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ["&", "!"] + domain[1:]
        return self.search(domain + args, limit=limit).name_get()

    @api.model_create_multi
    def create(self, vals_list):
        search_partner_mode = self.env.context.get("res_partner_search_mode")
        medical_type = search_partner_mode == "doctor" and "doctor" or "standard"
        is_doctor = search_partner_mode == "doctor"

        if search_partner_mode:
            for vals in vals_list:
                if vals.get("medical_type") != medical_type:
                    vals["medical_type"] = medical_type
                if is_doctor and "doctor_rank" not in vals:
                    vals["doctor_rank"] = 1
        return super().create(vals_list)
