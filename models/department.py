from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class department(models.Model):
    _name = 'hr.department'
    _inherit = 'hr.department'


    code = fields.Char("Code", default="DEPT CODE")
