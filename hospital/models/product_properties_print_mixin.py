#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductPropertiesPrintMixin(models.AbstractModel):
    _inherit = "product.properties.print.mixin"

    use_patient_visit_nr = fields.Boolean(
        string="Print Visit number",
        compute="_compute_use_patient_visit_nr",
        inverse="_inverse_use_patient_visit_nr",
    )

    @api.depends("print_properties")
    def _compute_use_patient_visit_nr(self):
        for record in self:
            record.use_patient_visit_nr = record.get_static_field("patient_visit_nr")

    def _inverse_use_patient_visit_nr(self):
        for record in self:
            record.set_static_field("patient_visit_nr", record.use_patient_visit_nr)

    use_clinical_case_number = fields.Boolean(
        string="Print Clinical case number",
        compute="_compute_use_clinical_case_number",
        inverse="_inverse_use_clinical_case_number",
    )

    @api.depends("print_properties")
    def _compute_use_clinical_case_number(self):
        for record in self:
            record.use_clinical_case_number = record.get_static_field(
                "patient_clinical_case_number"
            )

    def _inverse_use_clinical_case_number(self):
        for record in self:
            record.set_static_field(
                "patient_clinical_case_number", record.use_clinical_case_number
            )

    use_patient_name = fields.Boolean(
        string="Print Patient name",
        compute="_compute_use_patient_name",
        inverse="_inverse_use_patient_name",
    )

    @api.depends("print_properties")
    def _compute_use_patient_name(self):
        for record in self:
            record.use_patient_name = record.get_static_field("patient_name")

    def _inverse_use_patient_name(self):
        for record in self:
            record.set_static_field("patient_name", record.use_patient_name)

    use_clinical_path_ref = fields.Boolean(
        string="Print Clinical path reference",
        compute="_compute_use_clinical_path_ref",
        inverse="_inverse_use_clinical_path_ref",
    )

    @api.depends("print_properties")
    def _compute_use_clinical_path_ref(self):
        for record in self:
            record.use_clinical_path_ref = record.get_static_field(
                "patient_clinical_path_ref"
            )

    def _inverse_use_clinical_path_ref(self):
        for record in self:
            record.set_static_field(
                "patient_clinical_path_ref", record.use_clinical_path_ref
            )

    use_incident_nr = fields.Boolean(
        string="Print Incident number",
        compute="_compute_use_incident_nr",
        inverse="_inverse_use_incident_nr",
    )

    @api.depends("print_properties")
    def _compute_use_incident_nr(self):
        for record in self:
            record.use_incident_nr = record.get_static_field("patient_incident_nr")

    def _inverse_use_incident_nr(self):
        for record in self:
            record.set_static_field("patient_incident_nr", record.use_incident_nr)

    use_material_acquisition = fields.Boolean(
        string="Print Material acquisition",
        compute="_compute_use_material_acquisition",
        inverse="_inverse_use_material_acquisition",
    )

    @api.depends("print_properties")
    def _compute_use_material_acquisition(self):
        for record in self:
            record.use_material_acquisition = record.get_static_field(
                "patient_material_acquisition"
            )

    def _inverse_use_material_acquisition(self):
        for record in self:
            record.set_static_field(
                "patient_material_acquisition", record.use_material_acquisition
            )

    use_patient_fund_confirmation = fields.Boolean(
        string="Print Patient confirmation",
        compute="_compute_use_patient_fund_confirmation",
        inverse="_inverse_use_patient_fund_confirmation",
    )

    @api.depends("print_properties")
    def _compute_use_patient_fund_confirmation(self):
        for record in self:
            record.use_patient_fund_confirmation = record.get_static_field(
                "patient_fund_confirmation"
            )

    def _inverse_use_patient_fund_confirmation(self):
        for record in self:
            record.set_static_field(
                "patient_fund_confirmation", record.use_patient_fund_confirmation
            )

    use_patient_ada = fields.Boolean(
        string="Print Patient ada",
        compute="_compute_use_patient_ada",
        inverse="_inverse_use_patient_ada",
    )

    @api.depends("print_properties")
    def _compute_use_patient_ada(self):
        for record in self:
            record.use_patient_ada = record.get_static_field("patient_ada")

    def _inverse_use_patient_ada(self):
        for record in self:
            record.set_static_field("patient_ada", record.use_patient_ada)

    use_patient_tender = fields.Boolean(
        string="Print Patient tender",
        compute="_compute_use_patient_tender",
        inverse="_inverse_use_patient_tender",
    )

    @api.depends("print_properties")
    def _compute_use_patient_tender(self):
        for record in self:
            record.use_patient_tender = record.get_static_field("patient_tender")

    def _inverse_use_patient_tender(self):
        for record in self:
            record.set_static_field("patient_tender", record.use_patient_tender)

    use_patient_surgery_date = fields.Boolean(
        string="Print Patient surgery date",
        compute="_compute_use_patient_surgery_date",
        inverse="_inverse_use_patient_surgery_date",
    )

    @api.depends("print_properties")
    def _compute_use_patient_surgery_date(self):
        for record in self:
            record.use_patient_surgery_date = record.get_static_field(
                "patient_surgery_date"
            )

    def _inverse_use_patient_surgery_date(self):
        for record in self:
            record.set_static_field(
                "patient_surgery_date", record.use_patient_surgery_date
            )

    use_patient_note = fields.Boolean(
        string="Print Patient note",
        compute="_compute_use_patient_note",
        inverse="_inverse_use_patient_note",
    )

    @api.depends("print_properties")
    def _compute_use_patient_note(self):
        for record in self:
            record.use_patient_note = record.get_static_field("patient_note")

    def _inverse_use_patient_note(self):
        for record in self:
            record.set_static_field("patient_note", record.use_patient_note)

    use_isupply_contract = fields.Boolean(
        string="Print Supply contract",
        compute="_compute_use_isupply_contract",
        inverse="_inverse_use_isupply_contract",
    )

    @api.depends("print_properties")
    def _compute_use_isupply_contract(self):
        for record in self:
            record.use_isupply_contract = record.get_static_field("isupply_contract")

    def _inverse_use_isupply_contract(self):
        for record in self:
            record.set_static_field("isupply_contract", record.use_isupply_contract)

    use_isupply_contract_date = fields.Boolean(
        string="Print Supply contract date",
        compute="_compute_use_isupply_contract_date",
        inverse="_inverse_use_isupply_contract_date",
    )

    @api.depends("print_properties")
    def _compute_use_isupply_contract_date(self):
        for record in self:
            record.use_isupply_contract_date = record.get_static_field(
                "isupply_contract_date"
            )

    def _inverse_use_isupply_contract_date(self):
        for record in self:
            record.set_static_field(
                "isupply_contract_date", record.use_isupply_contract_date
            )

    use_isupply_order_number = fields.Boolean(
        string="Print Supply order number",
        compute="_compute_use_isupply_order_number",
        inverse="_inverse_use_isupply_order_number",
    )

    @api.depends("print_properties")
    def _compute_use_isupply_order_number(self):
        for record in self:
            record.use_isupply_order_number = record.get_static_field(
                "isupply_order_number"
            )

    def _inverse_use_isupply_order_number(self):
        for record in self:
            record.set_static_field(
                "isupply_order_number", record.use_isupply_order_number
            )

    use_isupply_order_date = fields.Boolean(
        string="Print Supply order date",
        compute="_compute_use_isupply_order_date",
        inverse="_inverse_use_isupply_order_date",
    )

    @api.depends("print_properties")
    def _compute_use_isupply_order_date(self):
        for record in self:
            record.use_isupply_order_date = record.get_static_field(
                "isupply_order_date"
            )

    def _inverse_use_isupply_order_date(self):
        for record in self:
            record.set_static_field("isupply_order_date", record.use_isupply_order_date)

    use_fund_verification = fields.Boolean(
        string="Print Fund verification",
        compute="_compute_use_fund_verification",
        inverse="_inverse_use_fund_verification",
    )

    @api.depends("print_properties")
    def _compute_use_fund_verification(self):
        for record in self:
            record.use_fund_verification = record.get_static_field("fund_verification")

    def _inverse_use_fund_verification(self):
        for record in self:
            record.set_static_field("fund_verification", record.use_fund_verification)

    use_patient_case_pics = fields.Boolean(
        string="Print Patient case pics",
        compute="_compute_use_patient_case_pics",
        inverse="_inverse_use_patient_case_pics",
    )

    @api.depends("print_properties")
    def _compute_use_patient_case_pics(self):
        for record in self:
            record.use_patient_case_pics = record.get_static_field("patient_case_pics")

    def _inverse_use_patient_case_pics(self):
        for record in self:
            record.set_static_field("patient_case_pics", record.use_patient_case_pics)

    def _get_target_field(self, target_field_name=False):
        if self._name == "patient.data":
            target_field_name = "medical_data_id"
        return super()._get_target_field(target_field_name=target_field_name)
