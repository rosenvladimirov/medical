#  Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ProductPropertiesPrintMixin(models.AbstractModel):
    _inherit = "product.properties.print.mixin"

    use_mdgp_class = fields.Boolean(
        string="Print MD Class",
        compute="_compute_use_mdgp_class",
        inverse="_inverse_use_mdgp_class",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_class(self):
        for record in self:
            record.use_mdgp_class = record.get_static_field("mdgp_class")

    def _inverse_use_mdgp_class(self):
        for record in self:
            record.set_static_field("mdgp_class", record.use_mdgp_class)

    use_mdgp_material = fields.Boolean(
        string="Print MD Material",
        compute="_compute_use_mdgp_material",
        inverse="_inverse_use_mdgp_material",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_material(self):
        for record in self:
            record.use_mdgp_material = record.get_static_field("mdgp_material")

    def _inverse_use_mdgp_material(self):
        for record in self:
            record.set_static_field("mdgp_material", record.use_mdgp_material)

    use_mdgp_category = fields.Boolean(
        string="Print MD Category",
        compute="_compute_use_mdgp_category",
        inverse="_inverse_use_mdgp_category",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_category(self):
        for record in self:
            record.use_mdgp_category = record.get_static_field("mdgp_category")

    def _inverse_use_mdgp_category(self):
        for record in self:
            record.set_static_field("mdgp_category", record.use_mdgp_category)

    use_mdgp_risk = fields.Boolean(
        string="Print MD Risk",
        compute="_compute_use_mdgp_risk",
        inverse="_inverse_use_mdgp_risk",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_risk(self):
        for record in self:
            record.use_mdgp_risk = record.get_static_field("mdgp_risk")

    def _inverse_use_mdgp_risk(self):
        for record in self:
            record.set_static_field("mdgp_risk", record.use_mdgp_risk)

    use_mdgp_mri_allow = fields.Boolean(
        string="Print MD MRI Allow",
        compute="_compute_use_mdgp_mri_allow",
        inverse="_inverse_use_mdgp_mri_allow",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_mri_allow(self):
        for record in self:
            record.use_mdgp_mri_allow = record.get_static_field("mdgp_mri_allow")

    def _inverse_use_mdgp_mri_allow(self):
        for record in self:
            record.set_static_field("mdgp_mri_allow", record.use_mdgp_mri_allow)

    use_mdgp_mri_type = fields.Boolean(
        string="Print MD MRI Condition",
        compute="_compute_use_mdgp_mri_type",
        inverse="_inverse_use_mdgp_mri_type",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_mri_type(self):
        for record in self:
            record.use_mdgp_mri_type = record.get_static_field("mdgp_mri_type")

    def _inverse_use_mdgp_mri_type(self):
        for record in self:
            record.set_static_field("mdgp_mri_type", record.use_mdgp_mri_type)

    use_mdgp_steril_hosp = fields.Boolean(
        string="Print MD Hospital Sterilisation",
        compute="_compute_use_mdgp_steril_hosp",
        inverse="_inverse_use_mdgp_steril_hosp",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_steril_hosp(self):
        for record in self:
            record.use_mdgp_steril_hosp = record.get_static_field("mdgp_steril_hosp")

    def _inverse_use_mdgp_steril_hosp(self):
        for record in self:
            record.set_static_field("mdgp_steril_hosp", record.use_mdgp_steril_hosp)

    use_mdgp_steril_man = fields.Boolean(
        string="Print MD Manufacturer Sterilisation",
        compute="_compute_use_mdgp_steril_man",
        inverse="_inverse_use_mdgp_steril_man",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_steril_man(self):
        for record in self:
            record.use_mdgp_steril_man = record.get_static_field("mdgp_steril_man")

    def _inverse_use_mdgp_steril_man(self):
        for record in self:
            record.set_static_field("mdgp_steril_man", record.use_mdgp_steril_man)

    use_mdgp_useage = fields.Boolean(
        string="Print MD Usage",
        compute="_compute_use_mdgp_useage",
        inverse="_inverse_use_mdgp_useage",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_useage(self):
        for record in self:
            record.use_mdgp_useage = record.get_static_field("mdgp_useage")

    def _inverse_use_mdgp_useage(self):
        for record in self:
            record.set_static_field("mdgp_useage", record.use_mdgp_useage)

    use_mdgp_service = fields.Boolean(
        string="Print MD Service",
        compute="_compute_use_mdgp_service",
        inverse="_inverse_use_mdgp_service",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_service(self):
        for record in self:
            record.use_mdgp_service = record.get_static_field("mdgp_service")

    def _inverse_use_mdgp_service(self):
        for record in self:
            record.set_static_field("mdgp_service", record.use_mdgp_service)

    use_mdgp_type = fields.Boolean(
        string="Print MD Type",
        compute="_compute_use_mdgp_type",
        inverse="_inverse_use_mdgp_type",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_type(self):
        for record in self:
            record.use_mdgp_type = record.get_static_field("mdgp_type")

    def _inverse_use_mdgp_type(self):
        for record in self:
            record.set_static_field("mdgp_type", record.use_mdgp_type)

    use_mdgp_anatomy = fields.Boolean(
        string="Print MD Anatomy",
        compute="_compute_use_mdgp_anatomy",
        inverse="_inverse_use_mdgp_anatomy",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_anatomy(self):
        for record in self:
            record.use_mdgp_anatomy = record.get_static_field("mdgp_anatomy")

    def _inverse_use_mdgp_anatomy(self):
        for record in self:
            record.set_static_field("mdgp_anatomy", record.use_mdgp_anatomy)

    use_mdgp_device = fields.Boolean(
        string="Print MD Device",
        compute="_compute_use_mdgp_device",
        inverse="_inverse_use_mdgp_device",
    )

    @api.depends("print_properties")
    def _compute_use_mdgp_device(self):
        for record in self:
            record.use_mdgp_device = record.get_static_field("mdgp_device")

    def _inverse_use_mdgp_device(self):
        for record in self:
            record.set_static_field("mdgp_device", record.use_mdgp_device)

    use_mdgr_mil_spec = fields.Boolean(
        string="Print Military Specifications",
        compute="_compute_use_mdgr_mil_spec",
        inverse="_inverse_use_mdgr_mil_spec",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_mil_spec(self):
        for record in self:
            record.use_mdgr_mil_spec = record.get_static_field("mdgr_mil_spec")

    def _inverse_use_mdgr_mil_spec(self):
        for record in self:
            record.set_static_field("mdgr_mil_spec", record.use_mdgr_mil_spec)

    use_mdgr_future_c2 = fields.Boolean(
        string="Print Future R Code 2",
        compute="_compute_use_mdgr_future_c2",
        inverse="_inverse_use_mdgr_future_c2",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_future_c2(self):
        for record in self:
            record.use_mdgr_future_c2 = record.get_static_field("mdgr_future_c2")

    def _inverse_use_mdgr_future_c2(self):
        for record in self:
            record.set_static_field("mdgr_future_c2", record.use_mdgr_future_c2)

    use_mdgr_future_c3 = fields.Boolean(
        string="Print Future R Code 3",
        compute="_compute_use_mdgr_future_c3",
        inverse="_inverse_use_mdgr_future_c3",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_future_c3(self):
        for record in self:
            record.use_mdgr_future_c3 = record.get_static_field("mdgr_future_c3")

    def _inverse_use_mdgr_future_c3(self):
        for record in self:
            record.set_static_field("mdgr_future_c3", record.use_mdgr_future_c3)

    use_mdgr_alt_obs_code = fields.Boolean(
        string="Print Alt Observe Code",
        compute="_compute_use_mdgr_alt_obs_code",
        inverse="_inverse_use_mdgr_alt_obs_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_alt_obs_code(self):
        for record in self:
            record.use_mdgr_alt_obs_code = record.get_static_field("mdgr_alt_obs_code")

    def _inverse_use_mdgr_alt_obs_code(self):
        for record in self:
            record.set_static_field("mdgr_alt_obs_code", record.use_mdgr_alt_obs_code)

    use_mdgr_alt_obs_desc = fields.Boolean(
        string="Print Alt Observe Desc",
        compute="_compute_use_mdgr_alt_obs_desc",
        inverse="_inverse_use_mdgr_alt_obs_desc",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_alt_obs_desc(self):
        for record in self:
            record.use_mdgr_alt_obs_desc = record.get_static_field("mdgr_alt_obs_desc")

    def _inverse_use_mdgr_alt_obs_desc(self):
        for record in self:
            record.set_static_field("mdgr_alt_obs_desc", record.use_mdgr_alt_obs_desc)

    use_mdgr_alt_obs_web = fields.Boolean(
        string="Print Alt Observe Web",
        compute="_compute_use_mdgr_alt_obs_web",
        inverse="_inverse_use_mdgr_alt_obs_web",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_alt_obs_web(self):
        for record in self:
            record.use_mdgr_alt_obs_web = record.get_static_field("mdgr_alt_obs_web")

    def _inverse_use_mdgr_alt_obs_web(self):
        for record in self:
            record.set_static_field("mdgr_alt_obs_web", record.use_mdgr_alt_obs_web)

    use_mdgr_alt_obs_price = fields.Boolean(
        string="Print Alt Observe Price",
        compute="_compute_use_mdgr_alt_obs_price",
        inverse="_inverse_use_mdgr_alt_obs_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_alt_obs_price(self):
        for record in self:
            record.use_mdgr_alt_obs_price = record.get_static_field(
                "mdgr_alt_obs_price"
            )

    def _inverse_use_mdgr_alt_obs_price(self):
        for record in self:
            record.set_static_field("mdgr_alt_obs_price", record.use_mdgr_alt_obs_price)

    use_mdbg_gmdn = fields.Boolean(
        string="Print GMDN",
        compute="_compute_use_mdbg_gmdn",
        inverse="_inverse_use_mdbg_gmdn",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_gmdn(self):
        for record in self:
            record.use_mdbg_gmdn = record.get_static_field("mdbg_gmdn")

    def _inverse_use_mdbg_gmdn(self):
        for record in self:
            record.set_static_field("mdbg_gmdn", record.use_mdbg_gmdn)

    use_mdbg_umdns = fields.Boolean(
        string="Print UMDNS",
        compute="_compute_use_mdbg_umdns",
        inverse="_inverse_use_mdbg_umdns",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_umdns(self):
        for record in self:
            record.use_mdbg_umdns = record.get_static_field("mdbg_umdns")

    def _inverse_use_mdbg_umdns(self):
        for record in self:
            record.set_static_field("mdbg_umdns", record.use_mdbg_umdns)

    use_mdbg_bda_code = fields.Boolean(
        string="Print BDA Code",
        compute="_compute_use_mdbg_bda_code",
        inverse="_inverse_use_mdbg_bda_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_bda_code(self):
        for record in self:
            record.use_mdbg_bda_code = record.get_static_field("mdbg_bda_code")

    def _inverse_use_mdbg_bda_code(self):
        for record in self:
            record.set_static_field("mdbg_bda_code", record.use_mdbg_bda_code)

    use_mdbg_bda_price = fields.Boolean(
        string="Print BDA Price",
        compute="_compute_use_mdbg_bda_price",
        inverse="_inverse_use_mdbg_bda_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_bda_price(self):
        for record in self:
            record.use_mdbg_bda_price = record.get_static_field("mdbg_bda_price")

    def _inverse_use_mdbg_bda_price(self):
        for record in self:
            record.set_static_field("mdbg_bda_price", record.use_mdbg_bda_price)

    use_mdbg_rei_code = fields.Boolean(
        string="Print NHIF Reimbursement Code",
        compute="_compute_use_mdbg_rei_code",
        inverse="_inverse_use_mdbg_bda_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_rei_code(self):
        for record in self:
            record.use_mdbg_rei_code = record.get_static_field("mdbg_rei_code")

    def _inverse_use_mdbg_bda_price(self):
        for record in self:
            record.set_static_field("mdbg_rei_code", record.use_mdbg_rei_code)

    use_mdbg_rei_price = fields.Boolean(
        string="Print NHIF Reimbursement Price",
        compute="_compute_use_mdbg_rei_price",
        inverse="_inverse_use_mdbg_rei_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_rei_price(self):
        for record in self:
            record.use_mdbg_rei_price = record.get_static_field("mdbg_rei_price")

    def _inverse_use_mdbg_rei_price(self):
        for record in self:
            record.set_static_field("mdbg_rei_price", record.use_mdbg_rei_price)

    use_mdbg_rei_rest_price = fields.Boolean(
        string="Print NHIF Rest Reimbursement Price",
        compute="_compute_use_mdbg_rei_rest_price",
        inverse="_inverse_use_mdbg_rei_rest_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_rei_rest_price(self):
        for record in self:
            record.use_mdbg_rei_rest_price = record.get_static_field(
                "mdbg_rei_rest_price"
            )

    def _inverse_use_mdbg_rei_rest_price(self):
        for record in self:
            record.set_static_field(
                "mdbg_rei_rest_price", record.use_mdbg_rei_rest_price
            )

    use_mdbg_future_code = fields.Boolean(
        string="Print Future Code",
        compute="_compute_use_mdbg_future_code",
        inverse="_inverse_use_mdbg_future_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdbg_future_code(self):
        for record in self:
            record.use_mdbg_future_code = record.get_static_field("mdbg_future_code")

    def _inverse_use_mdbg_future_code(self):
        for record in self:
            record.set_static_field("mdbg_future_code", record.use_mdbg_future_code)

    use_mdcy_cda_code = fields.Boolean(
        string="Print CDA Code",
        compute="_compute_use_mdcy_cda_code",
        inverse="_inverse_use_mdcy_cda_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_cda_code(self):
        for record in self:
            record.use_mdcy_cda_code = record.get_static_field("mdcy_cda_code")

    def _inverse_use_mdcy_cda_code(self):
        for record in self:
            record.set_static_field("mdcy_cda_code", record.use_mdcy_cda_code)

    use_mdcy_cda_price = fields.Boolean(
        string="Print CDA Price",
        compute="_compute_use_mdcy_cda_price",
        inverse="_inverse_use_mdcy_cda_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_cda_price(self):
        for record in self:
            record.use_mdcy_cda_price = record.get_static_field("mdcy_cda_price")

    def _inverse_use_mdcy_cda_price(self):
        for record in self:
            record.set_static_field("mdcy_cda_price", record.use_mdcy_cda_price)

    use_mdcy_rei_code = fields.Boolean(
        string="Print GESY Reimbursement Code",
        compute="_compute_use_mdcy_rei_code",
        inverse="_inverse_use_mdcy_rei_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_rei_code(self):
        for record in self:
            record.use_mdcy_rei_code = record.get_static_field("mdcy_rei_code")

    def _inverse_use_mdcy_rei_code(self):
        for record in self:
            record.set_static_field("mdcy_rei_code", record.use_mdcy_rei_code)

    use_mdcy_rei_price = fields.Boolean(
        string="Print GESY Reimbursement Price",
        compute="_compute_use_mdcy_rei_price",
        inverse="_inverse_use_mdcy_rei_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_rei_price(self):
        for record in self:
            record.use_mdcy_rei_price = record.get_static_field("mdcy_rei_price")

    def _inverse_use_mdcy_rei_price(self):
        for record in self:
            record.set_static_field("mdcy_rei_price", record.use_mdcy_rei_price)

    use_mdcy_future_code = fields.Boolean(
        string="Print Future Code",
        compute="_compute_use_mdcy_future_code",
        inverse="_inverse_use_mdcy_future_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_future_code(self):
        for record in self:
            record.use_mdcy_future_code = record.get_static_field("mdcy_future_code")

    def _inverse_use_mdcy_future_code(self):
        for record in self:
            record.set_static_field("mdcy_future_code", record.use_mdcy_future_code)

    use_mdcy_gesy_desc = fields.Boolean(
        string="Print GESY Description",
        compute="_compute_use_mdcy_gesy_desc",
        inverse="_inverse_use_mdcy_gesy_desc",
    )

    @api.depends("print_properties")
    def _compute_use_mdcy_gesy_desc(self):
        for record in self:
            record.use_mdcy_gesy_desc = record.get_static_field("mdcy_gesy_desc")

    def _inverse_use_mdcy_gesy_desc(self):
        for record in self:
            record.set_static_field("mdcy_gesy_desc", record.use_mdcy_gesy_desc)

    use_mdgr_eof_code = fields.Boolean(
        string="Print EOF Code",
        compute="_compute_use_mdgr_eof_code",
        inverse="_inverse_use_mdgr_eof_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_eof_code(self):
        for record in self:
            record.use_mdgr_eof_code = record.get_static_field("mdgr_eof_code")

    def _inverse_use_mdgr_eof_code(self):
        for record in self:
            record.set_static_field("mdgr_eof_code", record.use_mdgr_eof_code)

    use_mdgr_eof_price = fields.Boolean(
        string="Print EOF Price",
        compute="_compute_use_mdgr_eof_price",
        inverse="_inverse_use_mdgr_eof_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_eof_price(self):
        for record in self:
            record.use_mdgr_eof_price = record.get_static_field("mdgr_eof_price")

    def _inverse_use_mdgr_eof_price(self):
        for record in self:
            record.set_static_field("mdgr_eof_price", record.use_mdgr_eof_price)

    use_mdgr_observe_code = fields.Boolean(
        string="Print OBSERVE Code",
        compute="_compute_use_mdgr_observe_code",
        inverse="_inverse_use_mdgr_observe_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_observe_code(self):
        for record in self:
            record.use_mdgr_observe_code = record.get_static_field("mdgr_observe_code")

    def _inverse_use_mdgr_observe_code(self):
        for record in self:
            record.set_static_field("mdgr_observe_code", record.use_mdgr_observe_code)

    use_mdgr_observe_desc = fields.Boolean(
        string="Print Observe Desc",
        compute="_compute_use_mdgr_observe_desc",
        inverse="_inverse_use_mdgr_observe_desc",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_observe_desc(self):
        for record in self:
            record.use_mdgr_observe_desc = record.get_static_field("mdgr_observe_desc")

    def _inverse_use_mdgr_observe_desc(self):
        for record in self:
            record.set_static_field("mdgr_observe_desc", record.use_mdgr_observe_desc)

    use_mdgr_observe_price = fields.Boolean(
        string="Print OBSERVE Price",
        compute="_compute_use_mdgr_observe_price",
        inverse="_inverse_use_mdgr_observe_price",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_observe_price(self):
        for record in self:
            record.use_mdgr_observe_price = record.get_static_field(
                "mdgr_observe_price"
            )

    def _inverse_use_mdgr_observe_price(self):
        for record in self:
            record.set_static_field("mdgr_observe_price", record.use_mdgr_observe_price)

    use_mdgr_future_code = fields.Boolean(
        string="Print Future Code",
        compute="_compute_use_mdgr_future_code",
        inverse="_inverse_use_mdgr_future_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_future_code(self):
        for record in self:
            record.use_mdgr_future_code = record.get_static_field("mdgr_future_code")

    def _inverse_use_mdgr_future_code(self):
        for record in self:
            record.set_static_field("mdgr_future_code", record.use_mdgr_future_code)

    use_mdgr_ekapty_code = fields.Boolean(
        string="Print EKAPTY Code",
        compute="_compute_use_mdgr_ekapty_code",
        inverse="_inverse_use_mdgr_ekapty_code",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_ekapty_code(self):
        for record in self:
            record.use_mdgr_ekapty_code = record.get_static_field("mdgr_ekapty_code")

    def _inverse_use_mdgr_ekapty_code(self):
        for record in self:
            record.set_static_field("mdgr_ekapty_code", record.use_mdgr_ekapty_code)

    use_mdgr_observe_link = fields.Boolean(
        string="Print OBSERVE Link",
        compute="_compute_use_mdgr_observe_link",
        inverse="_inverse_use_mdgr_observe_link",
    )

    @api.depends("print_properties")
    def _compute_use_mdgr_observe_link(self):
        for record in self:
            record.use_mdgr_observe_link = record.get_static_field("mdgr_observe_link")

    def _inverse_use_mdgr_observe_link(self):
        for record in self:
            record.set_static_field("mdgr_observe_link", record.use_mdgr_observe_link)
