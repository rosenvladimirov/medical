# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class MedicalDataIcd11(models.Model):
    _name = "medical.data.icd11"
    _description = "The medical data icd11"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = "complete_name"
    _order = "complete_name"

    name = fields.Char(
        required=True,
        index=True,
        translate=True,
        help="The name of the medical device nomenclature",
    )
    code = fields.Char("code")
    url = fields.Char(help="URL of the medical device nomenclature")
    url_description = fields.Char(
        help="URL descriptions of the medical device nomenclature"
    )
    description = fields.Text(
        translate=True, help="The description of the medical device nomenclature"
    )
    complete_name = fields.Char(
        compute="_compute_complete_name",
        recursive=True,
        store=True,
    )

    parent_id = fields.Many2one(
        "medical.data.icd11", "Parent Category", index=True, ondelete="cascade"
    )
    parent_path = fields.Char(index=True, unaccent=False)
    child_id = fields.One2many("medical.data.icd11", "parent_id", "Child Categories")

    @api.depends("name", "code")
    def name_get(self):
        result = []
        for type_deal in self:
            if type_deal.code:
                name = f"[{type_deal.code}] {type_deal.name}"
            else:
                name = type_deal.name
            result.append((type_deal.id, name))
        return result

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = (
                    f"{category.parent_id.complete_name} / {category.name}"
                )
            else:
                category.complete_name = category.name

    @api.constrains("parent_id")
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_("Error ! You cannot create recursive categories."))
        return True

    @api.model
    def name_create(self, name):
        return self.create({"name": name}).name_get()[0]


# class MedicalDataGmdn(models.Model):
#    _name = "medical.data.gmdn"
#    _description = "The GMDN"
#    _order = "code, name"

#    name = fields.Char('Name', required=True, index=True, translate=True)
#    code = fields.Char('code')

#    @api.depends('name', 'code')
#    def name_get(self):
#        result = []
#        for gmdn in self:
#            if gmdn.code:
#                name = "[%s] %s" % (gmdn.code, gmdn.name)
#            else:
#                name = gmdn.name
#            result.append((gmdn.id, name))
#        return result

# class MedicalDataUmdns(models.Model):
#    _name = "medical.data.umdns"
#    _description = "The UMDNS"
#    _order = "code, name"

#    name = fields.Char('Name', required=True, index=True, translate=True)
#    code = fields.Char('code')

#    @api.depends('name', 'code')
#    def name_get(self):
#        result = []
#        for umdns in self:
#            if umdns.code:
#                name = "[%s] %s" % (umdns.code, umdns.name)
#            else:
#                name = umdns.name
#            result.append((umdns.id, name))
#        return result
