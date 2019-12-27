from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class account_analytic_tag(models.Model):
    _name = 'account.analytic.tag'
    _inherit = 'account.analytic.tag'

    code = fields.Char("Code", default="TAG CODE")
