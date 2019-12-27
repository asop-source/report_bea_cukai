# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class PengirimBarang(models.Model):
	_name = 'doc.pengiriman.barang'

	name = fields.Char(string='Nomor Dokumen',required=True)
	jenis = fields.Many2one('master.data.doc',string='Jenis Dokumen',required=True)
	tanggal = fields.Date(string="Tanggal",default=lambda self:time.strftime("%Y-%m-%d"))
	user = fields.Many2one('res.company', string="Company", required=True)

	order_date =fields.One2many('doc.barang', 'pengirim_id', string='Product')