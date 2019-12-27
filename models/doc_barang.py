from odoo import models, fields, api
import time
from odoo.addons import decimal_precision as dp

class productBarang(models.Model):
		_name='doc.barang'

		name = fields.Many2one('master.data.doc',string='Jenis Dokumen',required=True)
		tanggal = fields.Date(string="Tanggal Dokumen",default=lambda self:time.strftime("%Y-%m-%d"))
		no_doc = fields.Char(string='Nomor Dokumen')
		no_pengirim = fields.Char(string='Nomor Pengirim Barang')
		date_planned = fields.Date(string='Tanggal Penerimaan Barang',default=lambda self:time.strftime("%Y-%m-%d"))
		pengirim = fields.Many2one('res.partner', string='Pengirim Barang',)
		product_id = fields.Many2one('product.product', string='Nama Barang',required=True)
		product_qty = fields.Integer(string='Quantity', digits=dp.get_precision('Product Unit of Measure'))
		satuan	= fields.Many2one('uom.uom', string='Satuan', required=True)
		price_unit = fields.Integer(string='Harga')
		price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', store=True)

		pemasukan_id =fields.Many2one('doc.pemasukan.barang')
		pengirim_id	=fields.Many2one('doc.pengiriman.barang')


		@api.depends('product_qty','price_unit')
		def _compute_amount(self):
			for rec in self:
				if rec.price_unit>0:
					rec.price_subtotal = rec.product_qty * rec.price_unit
				else:
					rec.price_subtotal = 0.0