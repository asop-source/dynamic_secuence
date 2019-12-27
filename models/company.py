from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)



class company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    code = fields.Char("Code", default='COMP CODE')
