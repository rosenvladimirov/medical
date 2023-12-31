#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductPropertiesMixin(models.AbstractModel):
    _inherit = "product.properties.mixin"

    mdgp_class = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_class",
    )
    mdgp_material = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_material",
    )
    mdgp_category = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_category",
    )
    mdgp_risk = fields.Many2one(
        "product.properties.static.dropdown", related="product_prop_static_id.mdgp_risk"
    )
    mdgp_mri_allow = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_mri_allow",
    )
    mdgp_mri_type = fields.Char(related="product_prop_static_id.mdgp_mri_type")
    mdgp_steril_hosp = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_steril_hosp",
    )
    mdgp_steril_man = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_steril_man",
    )
    mdgp_useage = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_useage",
    )
    mdgp_service = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_service",
    )
    mdgp_type = fields.Many2one(
        "product.properties.static.dropdown", related="product_prop_static_id.mdgp_type"
    )
    mdgp_anatomy = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_anatomy",
    )
    mdgp_device = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgp_device",
    )
    mdgr_mil_spec = fields.Many2one(
        "product.properties.static.dropdown",
        related="product_prop_static_id.mdgr_mil_spec",
    )
    mdgr_future_c2 = fields.Char(related="product_prop_static_id.mdgr_future_c2")
    mdgr_future_c3 = fields.Char(related="product_prop_static_id.mdgr_future_c3")
    mdgr_alt_obs_code = fields.Char(related="product_prop_static_id.mdgr_alt_obs_code")
    mdgr_alt_obs_desc = fields.Char(related="product_prop_static_id.mdgr_alt_obs_desc")
    mdgr_alt_obs_web = fields.Char(related="product_prop_static_id.mdgr_alt_obs_web")
    mdgr_alt_obs_price = fields.Monetary(
        related="product_prop_static_id.mdgr_alt_obs_price",
        currency_field="gr_currency_id",
    )

    mdbg_gmdn = fields.Char(related="product_prop_static_id.mdbg_gmdn")
    mdbg_umdns = fields.Char(related="product_prop_static_id.mdbg_umdns")
    mdbg_bda_code = fields.Char(related="product_prop_static_id.mdbg_bda_code")
    mdbg_bda_price = fields.Monetary(
        related="product_prop_static_id.mdbg_bda_price", currency_field="bg_currency_id"
    )
    mdbg_rei_code = fields.Char(related="product_prop_static_id.mdbg_rei_code")
    mdbg_rei_price = fields.Monetary(
        related="product_prop_static_id.mdbg_rei_price", currency_field="bg_currency_id"
    )
    mdbg_future_code = fields.Char(
        related="product_prop_static_id.mdbg_future_code",
    )

    mdcy_cda_code = fields.Char(
        related="product_prop_static_id.mdcy_cda_code",
    )
    mdcy_cda_price = fields.Monetary(
        related="product_prop_static_id.mdcy_cda_price",
        currency_field="cy_currency_id",
    )
    mdcy_rei_code = fields.Char(
        related="product_prop_static_id.mdcy_rei_code",
        string="Product NHIF Reimbursement Code",
    )
    mdcy_rei_price = fields.Monetary(
        related="product_prop_static_id.mdcy_rei_price", currency_field="cy_currency_id"
    )
    mdcy_future_code = fields.Char(related="product_prop_static_id.mdcy_future_code")
    mdcy_gesy_desc = fields.Text(related="product_prop_static_id.mdcy_gesy_desc")

    mdgr_eof_code = fields.Char(related="product_prop_static_id.mdgr_eof_code")
    mdgr_eof_price = fields.Monetary(
        related="product_prop_static_id.mdgr_eof_price", currency_field="gr_currency_id"
    )
    mdgr_observe_code = fields.Char(related="product_prop_static_id.mdgr_observe_code")
    mdgr_observe_desc = fields.Char(related="product_prop_static_id.mdgr_observe_desc")
    mdgr_observe_price = fields.Monetary(
        related="product_prop_static_id.mdgr_observe_price",
        currency_field="gr_currency_id",
    )
    mdgr_future_code = fields.Char(related="product_prop_static_id.mdgr_future_code")
    mdgr_ekapty_code = fields.Char(related="product_prop_static_id.mdgr_ekapty_code")
    mdgr_observe_link = fields.Char(related="product_prop_static_id.mdgr_observe_link")

    bg_currency_id = fields.Many2one(
        "res.currency", related="product_prop_static_id.bg_currency_id"
    )
    cy_currency_id = fields.Many2one(
        "res.currency", related="product_prop_static_id.cy_currency_id"
    )
    gr_currency_id = fields.Many2one(
        "res.currency", related="product_prop_static_id.gr_currency_id"
    )

    @api.onchange("mdgr_observe_link")
    def onchange_mdgr_observe_link(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_observe_link()

    @api.onchange("mdgr_alt_obs_web")
    def onchange_mdgr_mdgr_alt_obs_web(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_mdgr_alt_obs_web()

    def update_mdgr_observe_link(self):
        for record in self:
            record.product_prop_static_id.onchange_mdgr_observe_link()
            record.product_prop_static_id.onchange_mdgr_mdgr_alt_obs_web()

    def _currencies_vals(self, vals):
        values = {}
        _logger.info("VALS %s" % vals)
        if not vals.get("bg_currency_id") and not self.bg_currency_id:
            values["bg_currency_id"] = self.env.ref("base.BGN").id
        if not vals.get("cy_currency_id") and not self.cy_currency_id:
            values["cy_currency_id"] = self.env.ref("base.EUR").id
        if not vals.get("gr_currency_id") and not self.gr_currency_id:
            values["gr_currency_id"] = self.env.ref("base.EUR").id
        return values

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for record, vals in zip(res, vals_list, strict=True):
            values = record._currencies_vals(vals)
            if values:
                record.update(values)
        return res

    def write(self, vals):
        for record in self:
            values = record._currencies_vals(vals)
            if values:
                vals.update(values)
        # _logger.info("VALS Mixin %s" % vals)
        return super().write(vals)
