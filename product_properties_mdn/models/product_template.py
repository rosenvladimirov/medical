#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_multi_variant = fields.Boolean(compute="_compute_is_multi_variant")
    is_single_variant = fields.Boolean(compute="_compute_single_variant")

    # -----------
    # vmdgp_class
    # -----------
    @api.depends("mdgp_class", "product_variant_id")
    def _compute_vmdgp_class(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_class = record.product_variant_id.mdgp_class
            else:
                record.vmdgp_class = record.mdgp_class

    @api.depends("mdgp_class", "product_variant_id")
    def _inverse_vmdgp_class(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_class = record.vmdgp_class
            else:
                record.mdgp_class = record.vmdgp_class

    def _search_vmdgp_class(self, operator, value):
        return [("product_variant_id.mdgp_class", operator, value)]

    vmdgp_class = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_class",
        inverse="_inverse_vmdgp_class",
        search="_search_vmdgp_class",
    )

    # --------------
    # vmdgp_material
    # --------------
    @api.depends("mdgp_material", "product_variant_id")
    def _compute_vmdgp_material(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_material = record.product_variant_id.mdgp_material
            else:
                record.vmdgp_material = record.mdgp_material

    @api.depends("mdgp_material", "product_variant_id")
    def _inverse_vmdgp_material(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_material = record.vmdgp_material
            else:
                record.mdgp_material = record.vmdgp_material

    def _search_vmdgp_material(self, operator, value):
        return [("product_variant_id.mdgp_material", operator, value)]

    vmdgp_material = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_material",
        inverse="_inverse_vmdgp_material",
        search="_search_vmdgp_material",
    )

    # --------------
    # vmdgp_category
    # --------------
    @api.depends("mdgp_category", "product_variant_id")
    def _compute_vmdgp_category(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_category = record.product_variant_id.mdgp_category
            else:
                record.vmdgp_category = record.mdgp_category

    @api.depends("mdgp_category", "product_variant_id")
    def _inverse_vmdgp_category(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_category = record.vmdgp_category
            else:
                record.mdgp_category = record.vmdgp_category

    def _search_vmdgp_category(self, operator, value):
        return [("product_variant_id.mdgp_category", operator, value)]

    vmdgp_category = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_category",
        inverse="_inverse_vmdgp_category",
        search="_search_vmdgp_category",
    )

    # --------------
    # vmdgp_risk
    # --------------
    @api.depends("mdgp_risk", "product_variant_id")
    def _compute_vmdgp_risk(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_risk = record.product_variant_id.mdgp_risk
            else:
                record.vmdgp_risk = record.mdgp_risk

    @api.depends("mdgp_risk", "product_variant_id")
    def _inverse_vmdgp_risk(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_risk = record.vmdgp_risk
            else:
                record.mdgp_risk = record.vmdgp_risk

    def _search_vmdgp_risk(self, operator, value):
        return [("product_variant_id.mdgp_risk", operator, value)]

    vmdgp_risk = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_risk",
        inverse="_inverse_vmdgp_risk",
        search="_search_vmdgp_risk",
    )

    # --------------
    # vmdgp_mri_allow
    # --------------
    @api.depends("mdgp_mri_allow", "product_variant_id")
    def _compute_vmdgp_mri_allow(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_mri_allow = record.product_variant_id.mdgp_mri_allow
            else:
                record.vmdgp_mri_allow = record.mdgp_mri_allow

    @api.depends("mdgp_mri_allow", "product_variant_id")
    def _inverse_vmdgp_mri_allow(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_mri_allow = record.vmdgp_mri_allow
            else:
                record.mdgp_mri_allow = record.vmdgp_mri_allow

    def _search_vmdgp_mri_allow(self, operator, value):
        return [("product_variant_id.mdgp_mri_allow", operator, value)]

    vmdgp_mri_allow = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_mri_allow",
        inverse="_inverse_vmdgp_mri_allow",
        search="_search_vmdgp_mri_allow",
    )

    # --------------
    # vmdgp_mri_type
    # --------------
    @api.depends("mdgp_mri_type", "product_variant_id")
    def _compute_vmdgp_mri_type(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_mri_type = record.product_variant_id.mdgp_mri_type
            else:
                record.vmdgp_mri_type = record.mdgp_mri_type

    @api.depends("mdgp_mri_type", "product_variant_id")
    def _inverse_vmdgp_mri_type(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_mri_type = record.vmdgp_mri_type
            else:
                record.mdgp_mri_type = record.vmdgp_mri_type

    def _search_vmdgp_mri_type(self, operator, value):
        return [("product_variant_id.mdgp_mri_type", operator, value)]

    vmdgp_mri_type = fields.Char(
        "Product MD MRI Condition",
        compute="_compute_vmdgp_mri_type",
        inverse="_inverse_vmdgp_mri_type",
        search="_search_vmdgp_mri_type",
    )

    # --------------
    # vmdgp_steril_hosp
    # --------------
    @api.depends("mdgp_steril_hosp", "product_variant_id")
    def _compute_vmdgp_steril_hosp(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_steril_hosp = record.product_variant_id.mdgp_steril_hosp
            else:
                record.vmdgp_steril_hosp = record.mdgp_steril_hosp

    @api.depends("mdgp_mri_type", "product_variant_id")
    def _inverse_vmdgp_steril_hosp(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_steril_hosp = record.vmdgp_steril_hosp
            else:
                record.mdgp_steril_hosp = record.vmdgp_steril_hosp

    def _search_vmdgp_steril_hosp(self, operator, value):
        return [("product_variant_id.mdgp_steril_hosp", operator, value)]

    vmdgp_steril_hosp = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_steril_hosp",
        inverse="_inverse_vmdgp_steril_hosp",
        search="_search_vmdgp_steril_hosp",
    )

    # --------------
    # vmdgp_steril_man
    # --------------
    @api.depends("mdgp_steril_man", "product_variant_id")
    def _compute_vmdgp_steril_man(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_steril_man = record.product_variant_id.mdgp_steril_man
            else:
                record.vmdgp_steril_man = record.mdgp_steril_man

    @api.depends("mdgp_steril_man", "product_variant_id")
    def _inverse_vmdgp_steril_man(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_steril_man = record.vmdgp_steril_man
            else:
                record.mdgp_steril_man = record.vmdgp_steril_man

    def _search_vmdgp_steril_man(self, operator, value):
        return [("product_variant_id.mdgp_steril_man", operator, value)]

    vmdgp_steril_man = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_steril_man",
        inverse="_inverse_vmdgp_steril_man",
        search="_search_vmdgp_steril_man",
    )

    # --------------
    # vmdgp_steril_man
    # --------------
    @api.depends("mdgp_useage", "product_variant_id")
    def _compute_vmdgp_useage(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_useage = record.product_variant_id.mdgp_useage
            else:
                record.vmdgp_useage = record.mdgp_useage

    @api.depends("mdgp_useage", "product_variant_id")
    def _inverse_vmdgp_useage(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_useage = record.vmdgp_useage
            else:
                record.mdgp_useage = record.vmdgp_useage

    def _search_vmdgp_useage(self, operator, value):
        return [("product_variant_id.mdgp_useage", operator, value)]

    vmdgp_useage = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_useage",
        inverse="_inverse_vmdgp_useage",
        search="_search_vmdgp_useage",
    )

    # --------------
    # vmdgp_service
    # --------------
    @api.depends("mdgp_service", "product_variant_id")
    def _compute_vmdgp_service(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_service = record.product_variant_id.mdgp_service
            else:
                record.vmdgp_service = record.mdgp_service

    @api.depends("mdgp_service", "product_variant_id")
    def _inverse_vmdgp_service(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_service = record.vmdgp_service
            else:
                record.mdgp_service = record.vmdgp_service

    def _search_vmdgp_service(self, operator, value):
        return [("product_variant_id.mdgp_service", operator, value)]

    vmdgp_service = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_service",
        inverse="_inverse_vmdgp_service",
        search="_search_vmdgp_service",
    )

    # --------------
    # vmdgp_service
    # --------------
    @api.depends("mdgp_type", "product_variant_id")
    def _compute_vmdgp_type(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_type = record.product_variant_id.mdgp_type
            else:
                record.vmdgp_type = record.mdgp_type

    @api.depends("mdgp_type", "product_variant_id")
    def _inverse_vmdgp_type(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_type = record.vmdgp_type
            else:
                record.mdgp_type = record.vmdgp_type

    def _search_vmdgp_type(self, operator, value):
        return [("product_variant_id.mdgp_type", operator, value)]

    vmdgp_type = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_type",
        inverse="_inverse_vmdgp_type",
        search="_search_vmdgp_type",
    )

    # --------------
    # vmdgp_anatomy
    # --------------
    @api.depends("mdgp_anatomy", "product_variant_id")
    def _compute_vmdgp_anatomy(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_anatomy = record.product_variant_id.mdgp_anatomy
            else:
                record.vmdgp_anatomy = record.mdgp_anatomy

    @api.depends("mdgp_anatomy", "product_variant_id")
    def _inverse_vmdgp_anatomy(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_anatomy = record.vmdgp_anatomy
            else:
                record.mdgp_anatomy = record.vmdgp_anatomy

    def _search_vmdgp_anatomy(self, operator, value):
        return [("product_variant_id.mdgp_anatomy", operator, value)]

    vmdgp_anatomy = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_anatomy",
        inverse="_inverse_vmdgp_anatomy",
        search="_search_vmdgp_anatomy",
    )

    # --------------
    # vmdgp_device
    # --------------
    @api.depends("mdgp_device", "product_variant_id")
    def _compute_vmdgp_device(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgp_device = record.product_variant_id.mdgp_device
            else:
                record.vmdgp_device = record.mdgp_device

    @api.depends("mdgp_device", "product_variant_id")
    def _inverse_vmdgp_device(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgp_device = record.vmdgp_device
            else:
                record.mdgp_device = record.vmdgp_device

    def _search_vmdgp_device(self, operator, value):
        return [("product_variant_id.mdgp_device", operator, value)]

    vmdgp_device = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgp_device",
        inverse="_inverse_vmdgp_device",
        search="_search_vmdgp_device",
    )

    # --------------
    # vmdgr_mil_spec
    # --------------
    @api.depends("mdgr_mil_spec", "product_variant_id")
    def _compute_vmdgr_mil_spec(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_mil_spec = record.product_variant_id.mdgr_mil_spec
            else:
                record.vmdgr_mil_spec = record.mdgr_mil_spec

    @api.depends("mdgr_mil_spec", "product_variant_id")
    def _inverse_vmdgr_mil_spec(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_mil_spec = record.vmdgr_mil_spec
            else:
                record.mdgr_mil_spec = record.vmdgr_mil_spec

    def _search_vmdgr_mil_spec(self, operator, value):
        return [("product_variant_id.mdgr_mil_spec", operator, value)]

    vmdgr_mil_spec = fields.Many2one(
        "product.properties.static.dropdown",
        compute="_compute_vmdgr_mil_spec",
        inverse="_inverse_vmdgr_mil_spec",
        search="_search_vmdgr_mil_spec",
    )

    # ---------------
    # vmdgr_future_c2
    # ---------------
    @api.depends("mdgr_future_c2", "product_variant_id")
    def _compute_vmdgr_future_c2(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_future_c2 = record.product_variant_id.mdgr_future_c2
            else:
                record.vmdgr_future_c2 = record.mdgr_future_c2

    @api.depends("mdgr_future_c2", "product_variant_id")
    def _inverse_vmdgr_future_c2(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_future_c2 = record.vmdgr_future_c2
            else:
                record.mdgr_future_c2 = record.vmdgr_future_c2

    def _search_vmdgr_future_c2(self, operator, value):
        return [("product_variant_id.mdgr_future_c2", operator, value)]

    vmdgr_future_c2 = fields.Char(
        "Product Future R Code 2",
        compute="_compute_vmdgr_future_c2",
        inverse="_inverse_vmdgr_future_c2",
        search="_search_vmdgr_future_c2",
    )

    # ---------------
    # vmdgr_future_c3
    # ---------------
    @api.depends("mdgr_future_c3", "product_variant_id")
    def _compute_vmdgr_future_c3(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_future_c3 = record.product_variant_id.mdgr_future_c3
            else:
                record.vmdgr_future_c3 = record.mdgr_future_c3

    @api.depends("mdgr_future_c3", "product_variant_id")
    def _inverse_vmdgr_future_c3(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_future_c3 = record.vmdgr_future_c3
            else:
                record.mdgr_future_c3 = record.vmdgr_future_c3

    def _search_vmdgr_future_c3(self, operator, value):
        return [("product_variant_id.mdgr_future_c3", operator, value)]

    vmdgr_future_c3 = fields.Char(
        "Product Future R Code 3",
        compute="_compute_vmdgr_future_c3",
        inverse="_inverse_vmdgr_future_c3",
        search="_search_vmdgr_future_c3",
    )

    # ------------------
    # vmdgr_alt_obs_code
    # ------------------
    @api.depends("mdgr_alt_obs_code", "product_variant_id")
    def _compute_vmdgr_alt_obs_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_alt_obs_code = record.product_variant_id.mdgr_alt_obs_code
            else:
                record.vmdgr_alt_obs_code = record.mdgr_alt_obs_code

    @api.depends("mdgr_alt_obs_code", "product_variant_id")
    def _inverse_vmdgr_alt_obs_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_alt_obs_code = record.vmdgr_alt_obs_code
            else:
                record.mdgr_alt_obs_code = record.vmdgr_alt_obs_code

    def _search_vmdgr_alt_obs_code(self, operator, value):
        return [("product_variant_id.mdgr_alt_obs_code", operator, value)]

    vmdgr_alt_obs_code = fields.Char(
        "Product Alt Observe Code",
        compute="_compute_vmdgr_alt_obs_code",
        inverse="_inverse_vmdgr_alt_obs_code",
        search="_search_vmdgr_alt_obs_code",
    )

    # ------------------
    # vmdgr_alt_obs_desc
    # ------------------
    @api.depends("mdgr_alt_obs_desc", "product_variant_id")
    def _compute_vmdgr_alt_obs_desc(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_alt_obs_desc = record.product_variant_id.mdgr_alt_obs_desc
            else:
                record.vmdgr_alt_obs_desc = record.mdgr_alt_obs_desc

    @api.depends("mdgr_alt_obs_desc", "product_variant_id")
    def _inverse_vmdgr_alt_obs_desc(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_alt_obs_desc = record.vmdgr_alt_obs_desc
            else:
                record.mdgr_alt_obs_code = record.vmdgr_alt_obs_desc

    def _search_vmdgr_alt_obs_desc(self, operator, value):
        return [("product_variant_id.mdgr_alt_obs_desc", operator, value)]

    vmdgr_alt_obs_desc = fields.Char(
        "Product Alt Observe Desc",
        compute="_compute_vmdgr_alt_obs_desc",
        inverse="_inverse_vmdgr_alt_obs_desc",
        search="_search_vmdgr_alt_obs_desc",
    )

    # ------------------
    # vmdgr_alt_obs_desc
    # ------------------
    @api.depends("mdgr_alt_obs_web", "product_variant_id")
    def _compute_vmdgr_alt_obs_web(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_alt_obs_web = record.product_variant_id.mdgr_alt_obs_web
            else:
                record.vmdgr_alt_obs_web = record.mdgr_alt_obs_web

    @api.depends("vmdgr_alt_obs_desc", "product_variant_id")
    def _inverse_vmdgr_alt_obs_web(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_alt_obs_web = record.vmdgr_alt_obs_web
            else:
                record.mdgr_alt_obs_web = record.vmdgr_alt_obs_web

    def _search_vmdgr_alt_obs_web(self, operator, value):
        return [("product_variant_id.mdgr_alt_obs_web", operator, value)]

    vmdgr_alt_obs_web = fields.Char(
        "Product Alt Observe Web",
        compute="_compute_vmdgr_alt_obs_web",
        inverse="_inverse_vmdgr_alt_obs_web",
        search="_search_vmdgr_alt_obs_web",
    )

    # -------------------
    # vmdgr_alt_obs_price
    # -------------------
    @api.depends("mdgr_alt_obs_price", "product_variant_id")
    def _compute_vmdgr_alt_obs_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_alt_obs_price = (
                    record.product_variant_id.mdgr_alt_obs_price
                )
            else:
                record.vmdgr_alt_obs_price = record.mdgr_alt_obs_price

    @api.depends("mdgr_alt_obs_price", "product_variant_id")
    def _inverse_vmdgr_alt_obs_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_alt_obs_price = (
                    record.vmdgr_alt_obs_price
                )
            else:
                record.mdgr_alt_obs_price = record.vmdgr_alt_obs_price

    def _search_vmdgr_alt_obs_price(self, operator, value):
        return [("product_variant_id.mdgr_alt_obs_price", operator, value)]

    vmdgr_alt_obs_price = fields.Monetary(
        "Product Alt Observe Price",
        compute="_compute_vmdgr_alt_obs_price",
        inverse="_inverse_vmdgr_alt_obs_price",
        search="_search_vmdgr_alt_obs_price",
        currency_field="vgr_currency_id",
    )

    # -------------------
    # vmdbg_gmdn
    # -------------------
    @api.depends("mdbg_gmdn", "product_variant_id")
    def _compute_vmdbg_gmdn(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_gmdn = record.product_variant_id.mdbg_gmdn
            else:
                record.vmdbg_gmdn = record.mdbg_gmdn

    @api.depends("mdbg_gmdn", "product_variant_id")
    def _inverse_vmdbg_gmdn(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_gmdn = record.vmdbg_gmdn
            else:
                record.mdbg_gmdn = record.vmdbg_gmdn

    def _search_vmdbg_gmdn(self, operator, value):
        return [("product_variant_id.mdbg_gmdn", operator, value)]

    vmdbg_gmdn = fields.Char(
        "Product GMDN",
        compute="_compute_vmdbg_gmdn",
        inverse="_inverse_vmdbg_gmdn",
        search="_search_vmdbg_gmdn",
    )

    # -------------------
    # vmdbg_umdns
    # -------------------
    @api.depends("mdbg_umdns", "product_variant_id")
    def _compute_vmdbg_umdns(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_umdns = record.product_variant_id.mdbg_umdns
            else:
                record.vmdbg_umdns = record.mdbg_umdns

    @api.depends("mdbg_umdns", "product_variant_id")
    def _inverse_vmdbg_umdns(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_umdns = record.vmdbg_umdns
            else:
                record.mdbg_umdns = record.vmdbg_umdns

    def _search_vmdbg_umdns(self, operator, value):
        return [("product_variant_id.mdbg_umdns", operator, value)]

    vmdbg_umdns = fields.Char(
        "Product UMDN",
        compute="_compute_vmdbg_umdns",
        inverse="_inverse_vmdbg_umdns",
        search="_search_vmdbg_umdns",
    )

    # --------------
    # vmdbg_bda_code
    # --------------
    @api.depends("mdbg_bda_code", "product_variant_id")
    def _compute_vmdbg_bda_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_bda_code = record.product_variant_id.mdbg_bda_code
            else:
                record.vmdbg_bda_code = record.mdbg_bda_code

    @api.depends("mdbg_bda_code", "product_variant_id")
    def _inverse_vmdbg_bda_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_bda_code = record.vmdbg_bda_code
            else:
                record.mdbg_bda_code = record.vmdbg_bda_code

    def _search_vmdbg_bda_code(self, operator, value):
        return [("product_variant_id.mdbg_bda_code", operator, value)]

    vmdbg_bda_code = fields.Char(
        "Product BDA",
        compute="_compute_vmdbg_bda_code",
        inverse="_inverse_vmdbg_bda_code",
        search="_search_vmdbg_bda_code",
    )

    # ---------------
    # vmdbg_bda_price
    # ---------------
    @api.depends("mdbg_bda_price", "product_variant_id")
    def _compute_vmdbg_bda_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_bda_price = record.product_variant_id.mdbg_bda_price
            else:
                record.vmdbg_bda_price = record.mdbg_bda_price

    @api.depends("mdbg_bda_price", "product_variant_id")
    def _inverse_vmdbg_bda_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_bda_price = record.vmdbg_bda_price
            else:
                record.mdbg_bda_price = record.vmdbg_bda_price

    def _search_vmdbg_bda_price(self, operator, value):
        return [("product_variant_id.mdbg_bda_price", operator, value)]

    vmdbg_bda_price = fields.Monetary(
        "Product BDA price",
        compute="_compute_vmdbg_bda_price",
        inverse="_inverse_vmdbg_bda_price",
        search="_search_vmdbg_bda_price",
        currency_field="vbg_currency_id",
    )

    # --------------
    # vmdbg_rei_code
    # --------------
    @api.depends("mdbg_rei_code", "product_variant_id")
    def _compute_vmdbg_rei_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_rei_code = record.product_variant_id.mdbg_rei_code
            else:
                record.vmdbg_rei_code = record.mdbg_rei_code

    @api.depends("mdbg_rei_code", "product_variant_id")
    def _inverse_vmdbg_rei_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_rei_code = record.vmdbg_rei_code
            else:
                record.mdbg_rei_code = record.vmdbg_rei_code

    def _search_vmdbg_rei_code(self, operator, value):
        return [("product_variant_id.mdbg_rei_code", operator, value)]

    vmdbg_rei_code = fields.Char(
        "Product REI",
        compute="_compute_vmdbg_rei_code",
        inverse="_inverse_vmdbg_rei_code",
        search="_search_vmdbg_rei_code",
    )

    # ---------------
    # vmdbg_rei_price
    # ---------------
    @api.depends("mdbg_rei_price", "product_variant_id")
    def _compute_vmdbg_rei_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_rei_price = record.product_variant_id.mdbg_rei_price
            else:
                record.vmdbg_rei_price = record.mdbg_rei_price

    @api.depends("mdbg_rei_price", "product_variant_id")
    def _inverse_vmdbg_rei_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_rei_price = record.vmdbg_rei_price
            else:
                record.mdbg_rei_price = record.vmdbg_rei_price

    def _search_vmdbg_rei_price(self, operator, value):
        return [("product_variant_id.mdbg_rei_price", operator, value)]

    vmdbg_rei_price = fields.Monetary(
        "Product REI price",
        compute="_compute_vmdbg_rei_price",
        inverse="_inverse_vmdbg_rei_price",
        search="_search_vmdbg_rei_price",
        currency_field="vbg_currency_id",
    )

    # --------------------
    # vmdbg_rei_rest_price
    # --------------------
    @api.depends("product_variant_id")
    def _compute_vmdbg_rei_rest_price(self):
        for record in self:
            for record in self:
                if not record.bg_currency_id:
                    record.bg_currency_id = self.env.ref("base.BGN")
                if self._context.get("force_price"):
                    record.vmdbg_rei_rest_price = (
                        self._context["force_price"] - record.vmdbg_rei_price
                    )
                else:
                    # _logger.info("PRICE %s" % self.env.user)
                    price = record.list_price
                    taxes = record.taxes_id.filtered(
                        lambda r: not self.env.user.company_id
                        or r.company_id == self.env.user.company_id
                    )
                    vmdbg_rei_rest_price = taxes.compute_all(
                        price, self.env.user.company_id.currency_id, 1.0, product=record
                    )["total_included"]
                    record.vmdbg_rei_rest_price = (
                        vmdbg_rei_rest_price - record.vmdbg_rei_price
                    )

    vmdbg_rei_rest_price = fields.Monetary(
        "Product REI rest price",
        compute="_compute_vmdbg_rei_rest_price",
        currency_field="vbg_currency_id",
    )

    # -----------------
    # vmdbg_future_code
    # -----------------
    @api.depends("mdbg_future_code", "product_variant_id")
    def _compute_vmdbg_future_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdbg_future_code = record.product_variant_id.mdbg_future_code
            else:
                record.vmdbg_future_code = record.mdbg_future_code

    @api.depends("mdbg_future_code", "product_variant_id")
    def _inverse_vmdbg_future_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdbg_future_code = record.vmdbg_future_code
            else:
                record.mdbg_future_code = record.vmdbg_future_code

    def _search_vmdbg_future_code(self, operator, value):
        return [("product_variant_id.mdbg_future_code", operator, value)]

    vmdbg_future_code = fields.Char(
        "Product Future code",
        compute="_compute_vmdbg_future_code",
        inverse="_inverse_vmdbg_future_code",
        search="_search_vmdbg_future_code",
    )

    # --------------
    # vmdcy_cda_code
    # --------------
    @api.depends("mdcy_cda_code", "product_variant_id")
    def _compute_vmdcy_cda_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_cda_code = record.product_variant_id.mdcy_cda_code
            else:
                record.vmdcy_cda_code = record.mdcy_cda_code

    @api.depends("mdcy_cda_code", "product_variant_id")
    def _inverse_vmdcy_cda_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_cda_code = record.vmdcy_cda_code
            else:
                record.mdcy_cda_code = record.vmdcy_cda_code

    def _search_vmdcy_cda_code(self, operator, value):
        return [("product_variant_id.mdcy_cda_code", operator, value)]

    vmdcy_cda_code = fields.Char(
        "Product CDA coda Code",
        compute="_compute_vmdcy_cda_code",
        inverse="_inverse_vmdcy_cda_code",
        search="_search_vmdcy_cda_code",
    )

    # ---------------
    # vmdcy_cda_price
    # ---------------
    @api.depends("mdcy_cda_price", "product_variant_id")
    def _compute_vmdcy_cda_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_cda_price = record.product_variant_id.mdcy_cda_price
            else:
                record.vmdcy_cda_price = record.mdcy_cda_price

    @api.depends("mdcy_cda_price", "product_variant_id")
    def _inverse_vmdcy_cda_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_cda_code = record.vmdcy_cda_price
            else:
                record.mdcy_cda_price = record.vmdcy_cda_price

    def _search_vmdcy_cda_price(self, operator, value):
        return [("product_variant_id.mdcy_cda_price", operator, value)]

    vmdcy_cda_price = fields.Monetary(
        "Product CDA price ",
        compute="_compute_vmdcy_cda_price",
        inverse="_inverse_vmdcy_cda_price",
        search="_search_vmdcy_cda_price",
        currency_field="vcy_currency_id",
    )

    # ---------------
    # vmdcy_rei_code
    # ---------------
    @api.depends("mdcy_rei_code", "product_variant_id")
    def _compute_vmdcy_rei_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_rei_code = record.product_variant_id.mdcy_rei_code
            else:
                record.vmdcy_rei_code = record.mdcy_rei_code

    @api.depends("mdcy_rei_code", "product_variant_id")
    def _inverse_vmdcy_rei_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_rei_code = record.vmdcy_rei_code
            else:
                record.mdcy_rei_code = record.vmdcy_rei_code

    def _search_vmdcy_rei_code(self, operator, value):
        return [("product_variant_id.mdcy_rei_code", operator, value)]

    vmdcy_rei_code = fields.Char(
        "Product REI code",
        compute="_compute_vmdcy_rei_code",
        inverse="_inverse_vmdcy_rei_code",
        search="_search_vmdcy_rei_code",
    )

    # ---------------
    # vmdcy_rei_price
    # ---------------
    @api.depends("mdcy_rei_price", "product_variant_id")
    def _compute_vmdcy_rei_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_rei_price = record.product_variant_id.mdcy_rei_price
            else:
                record.vmdcy_rei_price = record.mdcy_rei_price

    @api.depends("mdcy_rei_price", "product_variant_id")
    def _inverse_vmdcy_rei_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_rei_price = record.vmdcy_rei_price
            else:
                record.mdcy_rei_price = record.vmdcy_rei_price

    def _search_vmdcy_rei_price(self, operator, value):
        return [("product_variant_id.mdcy_rei_price", operator, value)]

    vmdcy_rei_price = fields.Monetary(
        "Product REI price",
        compute="_compute_vmdcy_rei_price",
        inverse="_inverse_vmdcy_rei_price",
        search="_search_vmdcy_rei_price",
        currency_field="vcy_currency_id",
    )

    # -----------------
    # vmdcy_future_code
    # -----------------
    @api.depends("mdcy_future_code", "product_variant_id")
    def _compute_vmdcy_future_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_future_code = record.product_variant_id.mdcy_future_code
            else:
                record.vmdcy_future_code = record.mdcy_future_code

    @api.depends("mdcy_future_code", "product_variant_id")
    def _inverse_vmdcy_future_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_future_code = record.vmdcy_future_code
            else:
                record.mdcy_future_code = record.vmdcy_future_code

    def _search_vmdcy_future_code(self, operator, value):
        return [("product_variant_id.mdcy_future_code", operator, value)]

    vmdcy_future_code = fields.Char(
        "Product Future code",
        compute="_compute_vmdcy_future_code",
        inverse="_inverse_vmdcy_future_code",
        search="_search_vmdcy_future_code",
    )

    # ---------------
    # vmdcy_gesy_desc
    # ---------------
    @api.depends("mdcy_gesy_desc", "product_variant_id")
    def _compute_vmdcy_gesy_desc(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdcy_gesy_desc = record.product_variant_id.mdcy_gesy_desc
            else:
                record.vmdcy_gesy_desc = record.mdcy_gesy_desc

    @api.depends("mdcy_future_code", "product_variant_id")
    def _inverse_vmdcy_gesy_desc(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdcy_gesy_desc = record.vmdcy_gesy_desc
            else:
                record.mdcy_gesy_desc = record.vmdcy_gesy_desc

    def _search_vmdcy_gesy_desc(self, operator, value):
        return [("product_variant_id.mdcy_gesy_desc", operator, value)]

    vmdcy_gesy_desc = fields.Text(
        "Product GESY description",
        compute="_compute_vmdcy_gesy_desc",
        inverse="_inverse_vmdcy_gesy_desc",
        search="_search_vmdcy_gesy_desc",
    )

    # ---------------
    # vmdgr_eof_code
    # ---------------
    @api.depends("mdgr_eof_code", "product_variant_id")
    def _compute_vmdgr_eof_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_eof_code = record.product_variant_id.mdgr_eof_code
            else:
                record.vmdgr_eof_code = record.mdgr_eof_code

    @api.depends("mdgr_eof_code", "product_variant_id")
    def _inverse_vmdgr_eof_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_eof_code = record.vmdgr_eof_code
            else:
                record.mdgr_eof_code = record.vmdgr_eof_code

    def _search_vmdgr_eof_code(self, operator, value):
        return [("product_variant_id.mdgr_eof_code", operator, value)]

    vmdgr_eof_code = fields.Char(
        "Product EOF code",
        compute="_compute_vmdgr_eof_code",
        inverse="_inverse_vmdgr_eof_code",
        search="_search_vmdgr_eof_code",
    )

    # ---------------
    # vmdgr_eof_price
    # ---------------
    @api.depends("mdgr_eof_price", "product_variant_id")
    def _compute_vmdgr_eof_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_eof_price = record.product_variant_id.mdgr_eof_price
            else:
                record.vmdgr_eof_price = record.mdgr_eof_price

    @api.depends("mdgr_eof_price", "product_variant_id")
    def _inverse_vmdgr_eof_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_eof_price = record.vmdgr_eof_price
            else:
                record.mdgr_eof_price = record.vmdgr_eof_price

    def _search_vmdgr_eof_price(self, operator, value):
        return [("product_variant_id.mdgr_eof_price", operator, value)]

    vmdgr_eof_price = fields.Monetary(
        "Product EOF price",
        compute="_compute_vmdgr_eof_price",
        inverse="_inverse_vmdgr_eof_price",
        search="_search_vmdgr_eof_price",
        currency_field="vgr_currency_id",
    )

    # ------------------
    # vmdgr_observe_code
    # ------------------
    @api.depends("mdgr_observe_code", "product_variant_id")
    def _compute_vmdgr_observe_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_observe_code = record.product_variant_id.mdgr_observe_code
            else:
                record.vmdgr_observe_code = record.mdgr_observe_code

    @api.depends("mdgr_observe_code", "product_variant_id")
    def _inverse_vmdgr_observe_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_observe_code = record.vmdgr_observe_code
            else:
                record.mdgr_observe_code = record.vmdgr_observe_code

    def _search_vmdgr_observe_code(self, operator, value):
        return [("product_variant_id.mdgr_observe_code", operator, value)]

    vmdgr_observe_code = fields.Char(
        "Product observe code",
        compute="_compute_vmdgr_observe_code",
        inverse="_inverse_vmdgr_observe_code",
        search="_search_vmdgr_observe_code",
    )

    # ------------------
    # vmdgr_observe_desc
    # ------------------
    @api.depends("mdgr_observe_desc", "product_variant_id")
    def _compute_vmdgr_observe_desc(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_observe_desc = record.product_variant_id.mdgr_observe_desc
            else:
                record.vmdgr_observe_desc = record.mdgr_observe_desc

    @api.depends("mdgr_observe_desc", "product_variant_id")
    def _inverse_vmdgr_observe_desc(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_observe_desc = record.vmdgr_observe_desc
            else:
                record.mdgr_observe_desc = record.vmdgr_observe_desc

    def _search_vmdgr_observe_desc(self, operator, value):
        return [("product_variant_id.mdgr_observe_desc", operator, value)]

    vmdgr_observe_desc = fields.Char(
        "Product observe description",
        compute="_compute_vmdgr_observe_desc",
        inverse="_inverse_vmdgr_observe_desc",
        search="_search_vmdgr_observe_desc",
    )

    # -------------------
    # vmdgr_observe_price
    # -------------------
    @api.depends("mdgr_observe_price", "product_variant_id")
    def _compute_vmdgr_observe_price(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_observe_price = (
                    record.product_variant_id.mdgr_observe_price
                )
            else:
                record.vmdgr_observe_price = record.mdgr_observe_price

    @api.depends("mdgr_observe_price", "product_variant_id")
    def _inverse_vmdgr_observe_price(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_observe_price = (
                    record.vmdgr_observe_price
                )
            else:
                record.mdgr_observe_price = record.vmdgr_observe_price

    def _search_vmdgr_observe_price(self, operator, value):
        return [("product_variant_id.mdgr_observe_price", operator, value)]

    vmdgr_observe_price = fields.Monetary(
        "Product observe price",
        compute="_compute_vmdgr_observe_price",
        inverse="_inverse_vmdgr_observe_price",
        search="_search_vmdgr_observe_price",
        currency_field="vgr_currency_id",
    )

    # -----------------
    # vmdgr_future_code
    # -----------------
    @api.depends("mdgr_future_code", "product_variant_id")
    def _compute_vmdgr_future_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_future_code = record.product_variant_id.mdgr_future_code
            else:
                record.vmdgr_future_code = record.mdgr_future_code

    @api.depends("mdgr_future_code", "product_variant_id")
    def _inverse_vmdgr_future_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_future_code = record.vmdgr_future_code
            else:
                record.mdgr_future_code = record.vmdgr_future_code

    def _search_vmdgr_future_code(self, operator, value):
        return [("product_variant_id.mdgr_future_code", operator, value)]

    vmdgr_future_code = fields.Char(
        "Product future code",
        compute="_compute_vmdgr_future_code",
        inverse="_inverse_vmdgr_future_code",
        search="_search_vmdgr_future_code",
    )

    # -----------------
    # vmdgr_ekapty_code
    # -----------------
    @api.depends("mdgr_ekapty_code", "product_variant_id")
    def _compute_vmdgr_ekapty_code(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_ekapty_code = record.product_variant_id.mdgr_ekapty_code
            else:
                record.vmdgr_ekapty_code = record.mdgr_ekapty_code

    @api.depends("mdgr_ekapty_code", "product_variant_id")
    def _inverse_vmdgr_ekapty_code(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_ekapty_code = record.vmdgr_ekapty_code
            else:
                record.mdgr_ekapty_code = record.vmdgr_ekapty_code

    def _search_vmdgr_ekapty_code(self, operator, value):
        return [("product_variant_id.mdgr_ekapty_code", operator, value)]

    vmdgr_ekapty_code = fields.Char(
        "Product ekapty code",
        compute="_compute_vmdgr_ekapty_code",
        inverse="_inverse_vmdgr_ekapty_code",
        search="_search_vmdgr_ekapty_code",
    )

    # -----------------
    # vmdgr_observe_link
    # -----------------
    @api.depends("mdgr_observe_link", "product_variant_id")
    def _compute_vmdgr_observe_link(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vmdgr_observe_link = record.product_variant_id.mdgr_observe_link
            else:
                record.vmdgr_observe_link = record.mdgr_observe_link

    @api.depends("mdgr_observe_link", "product_variant_id")
    def _inverse_vmdgr_observe_link(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.mdgr_observe_link = record.vmdgr_observe_link
            else:
                record.mdgr_observe_link = record.vmdgr_observe_link

    def _search_vmdgr_observe_link(self, operator, value):
        return [("product_variant_id.mdgr_observe_link", operator, value)]

    vmdgr_observe_link = fields.Char(
        "Product observe link",
        compute="_compute_vmdgr_observe_link",
        inverse="_inverse_vmdgr_observe_link",
        search="_search_vmdgr_observe_link",
    )

    # -----------------
    # vbg_currency_id
    # -----------------
    @api.depends("bg_currency_id", "product_variant_id")
    def _compute_vbg_currency_id(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vbg_currency_id = record.product_variant_id.bg_currency_id
            else:
                record.vbg_currency_id = record.bg_currency_id

    @api.depends("bg_currency_id", "product_variant_id")
    def _inverse_vbg_currency_id(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.bg_currency_id = record.vbg_currency_id
            else:
                record.bg_currency_id = record.vbg_currency_id

    def _search_vbg_currency_id(self, operator, value):
        return [("product_variant_id.bg_currency_id", operator, value)]

    vbg_currency_id = fields.Many2one(
        "res.currency",
        "Product BG currency",
        compute="_compute_vbg_currency_id",
        inverse="_inverse_vbg_currency_id",
        search="_search_vbg_currency_id",
    )

    # -----------------
    # vcy_currency_id
    # -----------------
    @api.depends("cy_currency_id", "product_variant_id")
    def _compute_vcy_currency_id(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vcy_currency_id = record.product_variant_id.cy_currency_id
            else:
                record.vcy_currency_id = record.cy_currency_id

    @api.depends("cy_currency_id", "product_variant_id")
    def _inverse_vcy_currency_id(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.cy_currency_id = record.vcy_currency_id
            else:
                record.cy_currency_id = record.vcy_currency_id

    def _search_vcy_currency_id(self, operator, value):
        return [("product_variant_id.cy_currency_id", operator, value)]

    vcy_currency_id = fields.Many2one(
        "res.currency",
        "Product CY currency",
        compute="_compute_vcy_currency_id",
        inverse="_inverse_vcy_currency_id",
        search="_search_vcy_currency_id",
    )

    # -----------------
    # vgr_currency_id
    # -----------------
    @api.depends("gr_currency_id", "product_variant_id")
    def _compute_vgr_currency_id(self):
        for record in self:
            if (
                record.product_variant_id
                and len(record.product_variant_ids) == 1
                and not record.attribute_line_ids
            ):
                record.vgr_currency_id = record.product_variant_id.gr_currency_id
            else:
                record.vgr_currency_id = record.gr_currency_id

    @api.depends("gr_currency_id", "product_variant_id")
    def _inverse_vgr_currency_id(self):
        for record in self:
            if len(record.product_variant_ids) == 1 and not record.attribute_line_ids:
                record.product_variant_id.gr_currency_id = record.vgr_currency_id
            else:
                record.gr_currency_id = record.vgr_currency_id

    def _search_vgr_currency_id(self, operator, value):
        return [("product_variant_id.gr_currency_id", operator, value)]

    vgr_currency_id = fields.Many2one(
        "res.currency",
        "Product GR currency",
        compute="_compute_vgr_currency_id",
        inverse="_inverse_vgr_currency_id",
        search="_search_vgr_currency_id",
    )

    def _compute_is_multi_variant(self):
        for record in self:
            record.is_multi_variant = not record.attribute_line_ids.ids

    def _compute_single_variant(self):
        for record in self:
            record.is_single_variant = record.attribute_line_ids.ids

    @api.onchange("mdgr_observe_link")
    def onchange_mdgr_observe_link(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_observe_link()

    @api.onchange("mdgr_alt_obs_web")
    def onchange_mdgr_mdgr_alt_obs_web(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_mdgr_alt_obs_web()

    @api.onchange("vmdgr_observe_link")
    def onchange_vmdgr_observe_link(self):
        for record in self:
            record.product_variant_id.product_prop_static_id.onchange_mdgr_observe_link()

    @api.onchange("vmdgr_alt_obs_web")
    def onchange_vmdgr_mdgr_alt_obs_web(self):
        for record in self:
            record.product_variant_id.product_prop_static_id.onchange_mdgr_mdgr_alt_obs_web()

    def update_mdgr_observe_link(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_observe_link()
            record.product_variant_id.product_prop_static_id.onchange_mdgr_observe_link()
