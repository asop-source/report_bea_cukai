from odoo import models, fields, api
import time
from odoo.addons import decimal_precision as dp

class Mutasi(models.Model):
		_name='doc.mutasi'

		# no = fields.Integer(compute='_nomor', string="No")
		product_id = fields.Many2one('product.product', string='Nama Barang', domain=[('purchase_ok', '=', True)], change_default=True, required=True)
		satuan	= fields.Many2one('uom.uom', string='Satuan', required=True)
		saldo_awal = fields.Float(string="Saldo Awal",required=True)
		pemasukan = fields.Float(string="Pemasukan",required=True)
		pengeluaran = fields.Float(string="Pengeluaran",required=True)
		penyesuaian = fields.Float(string="Penyesuaian",required=True)
		saldo_buku = fields.Float(compute='_compute_amount', string="Saldo Buku",required=True)
		stock = fields.Integer(string="Stock Of Name",required=True)
		selisih = fields.Integer(compute='_compute_saldo', string="Selisih")
		description = fields.Text(string="Keterangan")

		bahan_id = fields.Many2one('doc.mutasi.bahan.baku')
		barang_id = fields.Many2one('doc.mutasi.barang.jadi')
		mesin_id = fields.Many2one('doc.mutasi.mesin.peralatan')
		reject_id = fields.Many2one('doc.mutasi.reject.scrap')

		@api.depends('saldo_awal','pemasukan','pengeluaran','penyesuaian')
		def _compute_amount(self):
			for rec in self:
				if rec.saldo_awal>0:
					rec.saldo_buku = rec.pemasukan - rec.pengeluaran 
					rec.penyesuaian = rec.saldo_awal - rec.pengeluaran
				else:
					rec.saldo_buku = 0.0
					rec.penyesuaian = 0.0


		@api.depends('saldo_buku','stock')
		def _compute_saldo(self):
			for rec in self:
				if rec.stock>0:
					rec.selisih = rec.saldo_buku - rec.stock 
				else:
					rec.selisih = 0.0

		# def _nomor(self):
		# 	for rec in range(self.no):
