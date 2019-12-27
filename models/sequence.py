# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta
import logging
import pytz

"""
struktur odoo:
    user many2one partner
    employee many2one user

company = user.company_id

employee = cari employee user 
    department = cari dept employee
    location = cari location employee (harus sudah account.analytic.tag)

"""

class sequence(models.Model):
    _name = 'ir.sequence'
    _inherit = 'ir.sequence'


    def _get_prefix_suffix(self):
        def _interpolate(s, d):
            return (s % d) if s else ''

        def _interpolation_dict():
            now = range_date = effective_date = datetime.now(pytz.timezone(self._context.get('tz') or 'UTC'))
            if self._context.get('ir_sequence_date'):
                effective_date = fields.Datetime.from_string(self._context.get('ir_sequence_date'))
            if self._context.get('ir_sequence_date_range'):
                range_date = fields.Datetime.from_string(self._context.get('ir_sequence_date_range'))

            sequences = {
                'year': '%Y', 'month': '%m', 'day': '%d', 'y': '%y', 'doy': '%j', 'woy': '%W',
                'weekday': '%w', 'h24': '%H', 'h12': '%I', 'min': '%M', 'sec': '%S'
            }
            res = {}
            for key, format in sequences.items():
                res[key] = effective_date.strftime(format)
                res['range_' + key] = range_date.strftime(format)
                res['current_' + key] = now.strftime(format)

            user = self.env.user
            employee = self.env['hr.employee'].search([('user_id', '=' , user.id )])
            if employee:
                location = employee.work_location.code# analytic tag
                unit = employee.department_id.code #department
            else:
                location = ''
                unit = ''

            res.update({'company': user.company_id.code,
                        'location': location,
                        'unit': unit
                        })
            return res

        d = _interpolation_dict()
        try:
            interpolated_prefix = _interpolate(self.prefix, d)
            interpolated_suffix = _interpolate(self.suffix, d)
        except ValueError:
            raise UserError(_('Invalid prefix or suffix for sequence \'%s\'') % (self.get('name')))
        return interpolated_prefix, interpolated_suffix

