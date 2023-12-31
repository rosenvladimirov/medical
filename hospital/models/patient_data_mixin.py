#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import re

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PatientDataMixin(models.AbstractModel):
    _name = "patient.data.mixin"
    _description = "Patient Data mixin"

    patient_data_file_id = fields.Many2one("patient.data", "Patient data file")
    patient_partner_id = fields.Many2one(
        "res.partner",
        "Patient partner",
        related="patient_data_file_id.patient_partner_id",
    )
    patient_name = fields.Char(
        "Patient alias",
        compute="_compute_patient_name",
        inverse="_inverse_patient_name",
    )

    icd11_id = fields.Many2one(
        "medical.data.icd11", "ICD11", related="patient_data_file_id.icd11_id"
    )

    ct_mri_url = fields.Char(
        "CT/MRI", related="patient_data_file_id.ct_mri_url", help="URL"
    )

    issue_user_id = fields.Many2one(
        "hr.employee", related="patient_data_file_id.issue_user_id"
    )
    patient_clinical_path_ref = fields.Char(
        related="patient_data_file_id.patient_clinical_path_ref"
    )
    patient_incident_nr = fields.Char(
        related="patient_data_file_id.patient_incident_nr"
    )
    patient_visit_nr = fields.Char(related="patient_data_file_id.patient_visit_nr")
    patient_clinical_case_number = fields.Char(
        related="patient_data_file_id.patient_clinical_case_number"
    )
    patient_material_acquisition = fields.Char(
        related="patient_data_file_id.patient_material_acquisition"
    )
    patient_fund_confirmation = fields.Char(
        related="patient_data_file_id.patient_fund_confirmation"
    )
    patient_ada = fields.Char(related="patient_data_file_id.patient_ada")
    patient_tender = fields.Char(related="patient_data_file_id.patient_tender")
    patient_surgery_date = fields.Date(
        related="patient_data_file_id.patient_surgery_date"
    )
    patient_birthdate_date = fields.Date(
        "Birthdate Date",
        compute="_compute_patient_birthdate_date",
        inverse="_inverse_patient_birthdate_date",
    )
    isupply_contract = fields.Char(related="patient_data_file_id.isupply_contract")
    isupply_contract_date = fields.Date(
        related="patient_data_file_id.isupply_contract_date"
    )
    isupply_order_number = fields.Char(
        related="patient_data_file_id.isupply_order_number"
    )
    isupply_order_date = fields.Date(related="patient_data_file_id.isupply_order_date")
    fund_verification = fields.Char(related="patient_data_file_id.fund_verification")
    patient_case_pics = fields.Char(related="patient_data_file_id.patient_case_pics")
    patient_note = fields.Text(related="patient_data_file_id.patient_note")

    @api.depends("patient_partner_id", "patient_data_file_id")
    def _compute_patient_name(self):
        patient_partner_id = self.env.ref(
            "hospital.random_patient", raise_if_not_found=False
        )
        for record in self:
            if (
                record.patient_partner_id
                and record.patient_partner_id.id == patient_partner_id.id
            ):
                record.patient_name = record.patient_data_file_id.patient_name
            elif (
                record.patient_partner_id
                and record.patient_partner_id.id != patient_partner_id.id
            ):
                record.patient_name = record.patient_partner_id.name

    def _inverse_patient_name(self):
        patient_partner_id = self.env.ref(
            "hospital.random_patient", raise_if_not_found=False
        )
        for record in self:
            if (
                record.patient_partner_id
                and record.patient_partner_id.id == patient_partner_id.id
            ):
                record.patient_data_file_id.patient_name = record.patient_name
            elif (
                record.patient_partner_id
                and record.patient_partner_id.id != patient_partner_id.id
            ):
                record.patient_partner_id.name = record.patient_name

    @api.depends("patient_partner_id", "patient_data_file_id")
    def _compute_patient_birthdate_date(self):
        patient_partner_id = self.env.ref(
            "hospital.random_patient", raise_if_not_found=False
        )
        for record in self:
            if (
                record.patient_partner_id
                and record.patient_partner_id.id == patient_partner_id.id
            ):
                record.patient_birthdate_date = (
                    record.patient_data_file_id.birthdate_date
                )
            elif (
                record.patient_partner_id
                and record.patient_partner_id.id != patient_partner_id.id
            ):
                record.patient_birthdate_date = record.patient_partner_id.birthdate_date

    def _inverse_patient_birthdate_date(self):
        patient_partner_id = self.env.ref(
            "hospital.random_patient", raise_if_not_found=False
        )
        for record in self:
            if (
                record.patient_partner_id
                and record.patient_partner_id.id == patient_partner_id.id
            ):
                record.patient_data_file_id.birthdate_date = (
                    record.patient_birthdate_date
                )
            elif (
                record.patient_partner_id
                and record.patient_partner_id.id != patient_partner_id.id
            ):
                record.patient_partner_id.birthdate_date = record.patient_birthdate_date

    def _set_partner_doctor_id(self, partner_doctor_id):
        if self.patient_data_file_id:
            self.patient_data_file_id.partner_doctor_id = partner_doctor_id

    @api.model
    def ignore_fields(self):
        return [
            "__last_update",
            "write_date",
            "write_uid",
            "create_date",
            "create_uid",
            "id",
            "display_name",
            "company_id",
            "name",
            "order_ids",
            "stock_picking_ids",
            "account_invoice_ids",
            "partner_id",
            "patient_data_file_id",
        ]

    def _get_res_partner_patient_data(self, res, vals):
        partner_id = False
        partner_doctor_id = False

        if vals.get("partner_id"):
            partner_id = vals["partner_id"]

        if not partner_id:
            partner_id = res.partner_id.id or partner_id
        if res._name == "sale.order":
            partner_doctor_id = (
                res.partner_doctor_id and res.partner_doctor_id.id or partner_id
            )
        elif res._name == "sale.order" and res.partner_id != res.partner_shipping_id:
            partner_id = (
                res.partner_shipping_id and res.partner_shipping_id.id or partner_id
            )
        elif res._name == "sale.order" and vals.get("partner_shipping_id"):
            partner_id = vals["partner_shipping_id"]
        elif res._name == "stock.picking" and res.location_dest_id.out_partner_id:
            partner_id = (
                res.location_dest_id.out_partner_id
                and res.location_dest_id.out_partner_id.id
                or partner_id
            )
        elif self._name == "stock.picking" and vals.get("location_dest_id"):
            out_partner_id = res.env["stock.location"].browse(vals["location_dest_id"])
            if out_partner_id:
                partner_id = out_partner_id.out_partner_id.id
        return {
            "hospital_partner_id": partner_id,
            "partner_doctor_id": partner_doctor_id,
        }

    @api.model
    def patient_data_update(self, res, vals, updates=None, patient_data_ids=False):
        patient_data_obj = self.env["patient.data"]
        patient_data = {}
        if not patient_data_ids:
            patient_data_ids = list(
                filter(
                    lambda r: r not in self.ignore_fields(), patient_data_obj._fields
                )
            )

        if any([x in vals for x in patient_data_ids]):
            for field in patient_data_ids:
                if res and field in res._fields:
                    field_value = vals.get(field) and vals[field] or getattr(res, field)
                    field_name = patient_data_obj.fields_get(field)[field]
                    if not vals.get(field, False) and field_name["type"] == "many2one":
                        field_value = field_value.id
                    patient_data.update({field: field_value})

        for field in patient_data_ids:
            if field == "partner_doctor_id":
                continue
            if vals.get(field):
                del vals[field]
        if updates is not None:
            patient_data.update(updates)
        _logger.info("PATIENT DATA UPDATE %s" % patient_data)
        return patient_data

    @api.model
    def patient_data(self, res, vals, updates=None):
        patient_data = {}
        patient_partner_id = False
        regex_pattern = "|".join(map(re.escape, [",", ".", " "]))
        patient_data_obj = self.env["patient.data"]
        patient_data_ids = list(
            filter(lambda r: r not in self.ignore_fields(), patient_data_obj._fields)
        )
        # patient_data = patient_data_obj.default_get(patient_data_ids)

        if vals.get("patient_partner_id"):
            patient_partner_id = self.env["res.partner"].browse(
                vals["patient_partner_id"]
            )
            if vals.get("patient_birthdate_date"):
                patient_partner_id.birthdate_date = vals["patient_birthdate_date"]
                del vals["patient_birthdate_date"]

        if patient_partner_id and not vals.get("patient_name"):
            patient_data["patient_name"] = (
                ". ".join(
                    [
                        x[0].upper()
                        for x in re.split(regex_pattern, patient_partner_id.name)
                        if x
                    ]
                )
                + "."
            )

        if not patient_partner_id:
            patient_partner_id = self.env.ref(
                "hospital.random_patient", raise_if_not_found=False
            )

        # _logger.info("PATIENT %s" % patient_partner_id)
        patient_data.update(
            self.patient_data_update(
                res, vals, updates=updates, patient_data_ids=patient_data_ids
            )
        )
        patient_data.update(self._get_res_partner_patient_data(res, vals))
        # _logger.info("PATIENT DATA %s" % patient_data)
        patient_data.update(
            {
                "patient_partner_id": patient_partner_id.id,
            }
        )
        # _logger.info("PATIENT DATA VALS %s" % vals)
        # _logger.info("PATIENT DATA %s" % patient_data)
        return patient_data

    def _write_update(self, vals):
        values = {}
        patient_data_ids = list(
            filter(
                lambda r: r not in self.ignore_fields(),
                self.env["patient.data"]._fields,
            )
        )
        if any([x in vals for x in patient_data_ids]):
            values = self.patient_data_update(self, vals)
        return values
