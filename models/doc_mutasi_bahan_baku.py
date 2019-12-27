from odoo import models, fields, api
import time 


class MutasiBahan(models.Model):
	_name = 'doc.mutasi.bahan.baku'

	nomor = fields.Char(string='Nomor Dokumen' ,required=True)
	name = fields.Many2one('master.data.doc',string='Jenis Dokumen',required=True)
	tanggal = fields.Date(string="Tanggal" ,default=lambda self:time.strftime("%Y-%m-%d"))
	user = fields.Many2one('res.company', string="Company", required=True)
	

	order_date =fields.One2many('doc.mutasi','bahan_id', string='Product')