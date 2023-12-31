#  Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

import requests
from bs4 import BeautifulSoup

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductPropertiesStatic(models.Model):
    _inherit = "product.properties.static"

    mdgp_class = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Class",
        domain="[('field_name', '=', 'mdgp_class')]",
    )
    mdgp_material = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Material",
        domain="[('field_name', '=', 'mdgp_material')]",
    )
    mdgp_category = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Category",
        domain="[('field_name', '=', 'mdgp_category')]",
    )
    mdgp_risk = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Risk",
        domain="[('field_name', '=', 'mdgp_risk')]",
    )
    mdgp_mri_allow = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD MRI Allow",
        domain="[('field_name', '=', 'mdgp_mri_allow')]",
    )
    mdgp_mri_type = fields.Char("MD MRI Condition")
    mdgp_steril_hosp = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Hospital Sterilisation",
        domain="[('field_name', '=', 'mdgp_steril_hosp')]",
    )
    mdgp_steril_man = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Manufacturer Sterisisation",
        domain="[('field_name', '=', 'mdgp_steril_man')]",
    )
    mdgp_useage = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Usage",
        domain="[('field_name', '=', 'mdgp_useage')]",
    )
    mdgp_service = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Service",
        domain="[('field_name', '=', 'mdgp_service')]",
    )
    mdgp_type = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Type",
        domain="[('field_name', '=', 'mdgp_type')]",
    )
    mdgp_anatomy = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Anatomy",
        domain="[('field_name', '=', 'mdgp_anatomy')]",
    )
    mdgp_device = fields.Many2one(
        "product.properties.static.dropdown",
        string="MD Device",
        domain="[('field_name', '=', 'mdgp_device')]",
    )
    mdgr_mil_spec = fields.Many2one(
        "product.properties.static.dropdown",
        string="Military Specifications",
        domain="[('field_name', '=', 'mdgr_mil_spec')]",
    )
    mdgr_future_c2 = fields.Char("Future R Code 2")
    mdgr_future_c3 = fields.Char("Future R Code 3")
    mdgr_alt_obs_code = fields.Char("Alt Observe Code")
    mdgr_alt_obs_desc = fields.Char("Alt Observe Desc")
    mdgr_alt_obs_web = fields.Char("Alt Observe Web")
    mdgr_alt_obs_price = fields.Monetary(
        "Alt Observe Price", currency_field="gr_currency_id"
    )

    mdbg_gmdn = fields.Char("GMDN")
    mdbg_umdns = fields.Char("UMDNS")

    mdbg_bda_code = fields.Char("BDA Code")
    mdbg_bda_price = fields.Monetary("BDA Price", currency_field="bg_currency_id")
    mdbg_rei_code = fields.Char("NHIF Reimbursement Code")
    mdbg_rei_price = fields.Monetary(
        "NHIF Reimbursement Price", currency_field="bg_currency_id"
    )
    mdbg_rei_rest_price = fields.Monetary(
        "NHIF Rest Reimbursement Price",
        compute="_compute_mdbg_rei_rest_price",
        currency_field="bg_currency_id",
    )
    mdbg_future_code = fields.Char("Future Code")

    mdcy_cda_code = fields.Char("CDA Code")
    mdcy_cda_price = fields.Monetary("CDA Price", currency_field="cy_currency_id")
    mdcy_rei_code = fields.Char("GESY Reimbursement Code")
    mdcy_rei_price = fields.Monetary(
        "GESY Reimbursement Price", currency_field="cy_currency_id"
    )
    mdcy_future_code = fields.Char("Future Code")
    mdcy_gesy_desc = fields.Text("GESY Description", translate=True)

    mdgr_eof_code = fields.Char("EOF Code")
    mdgr_eof_price = fields.Monetary("EOF Price", currency_field="gr_currency_id")
    mdgr_observe_code = fields.Char("OBSERVE Code")
    mdgr_observe_desc = fields.Char("Observe Desc")
    mdgr_observe_price = fields.Monetary(
        "OBSERVE Price", currency_field="gr_currency_id"
    )
    mdgr_future_code = fields.Char("Future Code")
    mdgr_ekapty_code = fields.Char("EKAPTY Code")
    mdgr_observe_link = fields.Char("OBSERVE Link")

    bg_currency_id = fields.Many2one(
        "res.currency",
        string="[BG] Currency",
        default=lambda self: self.env.ref("base.BGN").id,
    )
    cy_currency_id = fields.Many2one(
        "res.currency",
        string="[CY] Currency",
        default=lambda self: self.env.ref("base.EUR").id,
    )
    gr_currency_id = fields.Many2one(
        "res.currency",
        string="[GR] Currency",
        default=lambda self: self.env.ref("base.EUR").id,
    )

    @api.depends("bg_currency_id", "mdbg_rei_price", "object_id")
    def _compute_mdbg_rei_rest_price(self):
        for record in self:
            if not record.bg_currency_id:
                record.bg_currency_id = self.env.ref("base.BGN")
            if self._context.get("force_price"):
                record.mdbg_rei_rest_price = (
                    self._context["force_price"] - record.mdbg_rei_price
                )
            else:
                if record.object_id and record.object_id._name in (
                    "product.product" or "product.template"
                ):
                    # _logger.info("PRICE %s" % self.env.user)
                    price = record.object_id.price
                    if record.object_id._name == "product.product":
                        taxes = record.object_id.taxes_id.filtered(
                            lambda r: not self.env.user.company_id
                            or r.company_id == self.env.user.company_id
                        )
                    else:
                        taxes = record.object_id.product_tmpl_id.taxes_id.filtered(
                            lambda r: not self.env.user.company_id
                            or r.company_id == self.env.user.company_id
                        )
                    if record.object_id._name == "product.product":
                        price += record.object_id.price_extra
                    record.mdbg_rei_rest_price = taxes.compute_all(
                        price,
                        self.env.user.company_id.currency_id,
                        1.0,
                        product=record.object_id,
                    )["total_included"]
                    record.mdbg_rei_rest_price = (
                        record.mdbg_rei_rest_price - record.mdbg_rei_price
                    )
                else:
                    record.mdbg_rei_rest_price = 0.0

    @api.model
    def ignore_fields(self):
        res = super().ignore_fields()
        res.append("bg_currency_id")
        res.append("gr_currency_id")
        res.append("cy_currency_id")
        res.append("mdbg_rei_rest_price")
        # res.append('issue_user_id')
        return res

    # @api.multi
    # @api.depends('name', 'code')
    # def name_get(self):
    #     result = []
    #     for properties in self:
    #         name = 'Medical print properties'
    #         result.append((properties.id, name))
    #     return result

    @api.onchange("mdbg_bda_price", "mdbg_rei_price")
    def onchange_bg_price(self):
        if not self.bg_currency_id:
            self.bg_currency_id = self.env.ref("base.BGN")

    @api.onchange("mdcy_cda_price", "mdcy_rei_price")
    def onchange_cy_price(self):
        if not self.cy_currency_id:
            self.cy_currency_id = self.env.ref("base.EUR")

    @api.onchange("mdgr_eof_price", "mdgr_observe_price", "mdgr_observe_link")
    def onchange_gr_price(self):
        if not self.gr_currency_id:
            self.gr_currency_id = self.env.ref("base.EUR")

    @api.onchange("mdgr_observe_link")
    def onchange_mdgr_observe_link(self):
        for record in self:
            if record.mdgr_observe_link:
                html_text = requests.get(
                    record.mdgr_observe_link, timeout=(3.05, 27)
                ).text
                soup = BeautifulSoup(html_text, "html.parser")
                record.mdgr_observe_code = (
                    soup.find_all("tbody")[0]
                    .find_all("tr")[0]
                    .find_all("td")[0]
                    .text.replace("\r\n", "")
                    .strip()
                )
                record.mdgr_observe_desc = (
                    soup.find_all("tbody")[0]
                    .find_all("tr")[1]
                    .find_all("td")[0]
                    .text.replace("\r\n", "")
                    .strip()
                )
                record.mdgr_observe_price = float(
                    soup.find_all("tbody")[2]
                    .find_all("tr")[0]
                    .find_all("td")[1]
                    .text.replace("\r\n", "")
                    .strip()
                )

    @api.onchange("mdgr_alt_obs_web")
    def onchange_mdgr_mdgr_alt_obs_web(self):
        for record in self:
            if record.mdgr_alt_obs_web:
                html_text = requests.get(
                    record.mdgr_alt_obs_web, timeout=(3.05, 27)
                ).text
                soup = BeautifulSoup(html_text, "html.parser")
                record.mdgr_alt_obs_code = (
                    soup.find_all("tbody")[0]
                    .find_all("tr")[0]
                    .find_all("td")[0]
                    .text.replace("\r\n", "")
                    .strip()
                )
                record.mdgr_alt_obs_desc = (
                    soup.find_all("tbody")[0]
                    .find_all("tr")[1]
                    .find_all("td")[0]
                    .text.replace("\r\n", "")
                    .strip()
                )
                record.mdgr_alt_obs_price = float(
                    soup.find_all("tbody")[2]
                    .find_all("tr")[0]
                    .find_all("td")[1]
                    .text.replace("\r\n", "")
                    .strip()
                )

    @api.model
    def property_data_sub(self, vals):
        sub_vals = {}
        static_properties_obj = self.env["product.properties.static"]
        static_ids = list(
            filter(
                lambda r: r not in static_properties_obj.ignore_fields(),
                static_properties_obj._fields,
            )
        ) + ["bg_currency_id", "gr_currency_id", "cy_currency_id"]

        for field in static_ids:
            if "v" + field in list(vals.keys()):
                sub_vals[field] = vals["v" + field]
                del vals["v" + field]
        return sub_vals

    @api.model
    def static_property_fields(self):
        static_ids = super().static_property_fields()
        static_ids += ["bg_currency_id", "gr_currency_id", "cy_currency_id"]
        return static_ids

    @api.model
    # @job
    def schedule_codes(self):
        properties = self.search(
            ["|", ("mdgr_observe_link", "!=", False), ("mdgr_alt_obs_web", "!=", False)]
        )
        for line in properties:
            _logger.info(
                "GR Line code {line.mdgr_observe_link} or {line.mdgr_alt_obs_web}"
            )
            try:
                line.onchange_mdgr_observe_link()
                line.onchange_mdgr_mdgr_alt_obs_web()
            except ValueError:
                _logger.info("Exeption error from gr code collections")
                pass
