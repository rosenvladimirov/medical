#  Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProductPropertiesStatic(models.Model):
    _inherit = "product.properties.static"

    medical_data_id = fields.Many2one("patient.data", "Medical data")

    patient_clinical_path_ref = fields.Char(
        related="medical_data_id.patient_clinical_path_ref"
    )
    patient_name = fields.Char(related="medical_data_id.patient_name")
    patient_incident_nr = fields.Char(related="medical_data_id.patient_incident_nr")
    patient_visit_nr = fields.Char(related="medical_data_id.patient_visit_nr")
    patient_clinical_case_number = fields.Char(
        related="medical_data_id.patient_clinical_case_number"
    )
    patient_material_acquisition = fields.Char(
        related="medical_data_id.patient_material_acquisition"
    )
    patient_fund_confirmation = fields.Char(
        related="medical_data_id.patient_fund_confirmation"
    )
    patient_ada = fields.Char(related="medical_data_id.patient_ada")
    patient_tender = fields.Char(related="medical_data_id.patient_tender")
    patient_surgery_date = fields.Date(related="medical_data_id.patient_surgery_date")
    patient_birthdate_date = fields.Date(related="medical_data_id.birthdate_date")
    isupply_contract = fields.Char(related="medical_data_id.isupply_contract")
    isupply_contract_date = fields.Date(related="medical_data_id.isupply_contract_date")
    isupply_order_number = fields.Char(related="medical_data_id.isupply_order_number")
    isupply_order_date = fields.Date(related="medical_data_id.isupply_order_date")
    fund_verification = fields.Char(related="medical_data_id.fund_verification")
    patient_case_pics = fields.Char(related="medical_data_id.patient_case_pics")
    patient_note = fields.Text(related="medical_data_id.patient_note")
