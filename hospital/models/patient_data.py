# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PatientData(models.Model):
    _name = "patient.data"
    _description = "Patient data file"

    name = fields.Char(
        string="File Reference",
        required=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )
    patient_partner_id = fields.Many2one(
        "res.partner", "Patient Contact", required=True, index=True, ondelete="cascade"
    )
    partner_doctor_id = fields.Many2one(
        "res.partner", "Treating doctor", required=True, change_default=True
    )
    hospital_partner_id = fields.Many2one("res.partner", "Hospital")

    patient_name = fields.Char("File Patient Alias")
    birthdate_date = fields.Date("File Patient Birthdate")

    icd11_id = fields.Many2one("medical.data.icd11", "ICD11")
    issue_user_id = fields.Many2one("hr.employee", "Issue User")

    company_id = fields.Many2one(
        "res.company",
        "Company",
        default=lambda self: self.env["res.company"]._company_default_get(
            "patient.data"
        ),
    )

    order_ids = fields.Many2many("sale.order", string="Sale orders")
    stock_picking_ids = fields.Many2many("stock.picking", string="Picking orders")
    account_invoice_ids = fields.Many2many("account.move", string="Invoices")

    patient_clinical_path_ref = fields.Char("Patient Clinical Path")
    patient_incident_nr = fields.Char("Incident Number")
    patient_visit_nr = fields.Char("Visit Number")
    patient_clinical_case_number = fields.Char("Patient Case number")
    patient_material_acquisition = fields.Char("Material Acquisition Nr.")
    patient_fund_confirmation = fields.Char("Fund Confirmation")
    patient_ada = fields.Char("ADA")
    patient_tender = fields.Char("Tender")
    patient_surgery_date = fields.Date("Surgery date")

    isupply_contract = fields.Char("E-tender Contract")
    isupply_contract_date = fields.Date("E-tender Contract Date")
    isupply_order_number = fields.Char("E-tender Order Number")
    isupply_order_date = fields.Date("E-tender Order Date")
    fund_verification = fields.Char("Fund Verification Code")
    patient_case_pics = fields.Char("Patient Case Pictures")
    patient_note = fields.Text("Description")
    ct_mri_url = fields.Char("CT/MRI", help="URL")

    @api.depends("patient_partner_id")
    def name_get(self):
        result = []
        for data in self:
            patient_partner_id = data.patient_partner_id
            patient_name = data.patient_partner_id.name
            name = f"[{data.name}] {patient_partner_id and patient_name or ''}"
            result.append((data.id, name))
        return result

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New"):
                if "company_id" in vals:
                    vals["name"] = self.env["ir.sequence"].with_context(
                        force_company=vals["company_id"]
                    ).next_by_code("patient.data") or _("New")
                else:
                    vals["name"] = self.env["ir.sequence"].next_by_code(
                        "patient.data"
                    ) or _("New")
        return super().create(vals_list)
