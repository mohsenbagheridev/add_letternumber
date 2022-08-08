# -*- coding: utf-8 -*-
# from odoo import http


# class HomaLetternumber(http.Controller):
#     @http.route('/homa_letternumber/homa_letternumber/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/homa_letternumber/homa_letternumber/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('homa_letternumber.listing', {
#             'root': '/homa_letternumber/homa_letternumber',
#             'objects': http.request.env['homa_letternumber.homa_letternumber'].search([]),
#         })

#     @http.route('/homa_letternumber/homa_letternumber/objects/<model("homa_letternumber.homa_letternumber"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('homa_letternumber.object', {
#             'object': obj
#         })
