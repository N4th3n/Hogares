# -*- coding: utf-8 -*-
# from odoo import http


# class Fin(http.Controller):
#     @http.route('/fin/fin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fin/fin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fin.listing', {
#             'root': '/fin/fin',
#             'objects': http.request.env['fin.fin'].search([]),
#         })

#     @http.route('/fin/fin/objects/<model("fin.fin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fin.object', {
#             'object': obj
#         })
