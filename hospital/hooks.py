#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    partner_id = env["res.partner"].create(
        {
            "name": "Random patient",
            "display_name": "Random patient",
            "city": "Sofia",
            "country_id": env.ref("base.bg").id,
            "email": "Random.patient@example.com",
            "company_id": env.ref("base.main_company").id,
            "medical_type": "patient",
        }
    )
    _logger.info(f"Crete patient [{partner_id.id}] {partner_id.display_name}")
    env["ir.model.data"].create(
        {
            "module": "hospital",
            "name": "random_patient",
            "model": "res.partner",
            "noupdate": True,
            "res_id": partner_id.id,
            "reference": f"res.partner,{partner_id.id}",
        }
    )
