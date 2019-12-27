# -*- coding: utf-8 -*-
from odoo import http

# class VitDynamicSequence(http.Controller):
#     @http.route('/vit_dynamic_sequence/vit_dynamic_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_dynamic_sequence/vit_dynamic_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_dynamic_sequence.listing', {
#             'root': '/vit_dynamic_sequence/vit_dynamic_sequence',
#             'objects': http.request.env['vit_dynamic_sequence.vit_dynamic_sequence'].search([]),
#         })

#     @http.route('/vit_dynamic_sequence/vit_dynamic_sequence/objects/<model("vit_dynamic_sequence.vit_dynamic_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_dynamic_sequence.object', {
#             'object': obj
#         })