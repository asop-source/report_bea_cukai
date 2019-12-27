# -*- coding: utf-8 -*-
from odoo import http

# class ReportBc(http.Controller):
#     @http.route('/report_bc/report_bc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_bc/report_bc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_bc.listing', {
#             'root': '/report_bc/report_bc',
#             'objects': http.request.env['report_bc.report_bc'].search([]),
#         })

#     @http.route('/report_bc/report_bc/objects/<model("report_bc.report_bc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_bc.object', {
#             'object': obj
#         })