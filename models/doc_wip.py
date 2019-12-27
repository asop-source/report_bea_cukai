from odoo import models, fields, api
import time
from odoo.addons import decimal_precision as dp

class DocWIP(models.Model):
		_name='doc.wip'


		product_id = fields.Many2one('product.product', string='Nama Barang',required=True)
		product_qty = fields.Integer(string='Quantity', digits=dp.get_precision('Product Unit of Measure'))
		satuan	= fields.Many2one('uom.uom', string='Satuan', required=True)

		wip_id =fields.Many2one('doc.posisi.wip')
