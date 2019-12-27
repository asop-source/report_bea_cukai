# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class MasterDoc(models.Model):
	_name = 'master.data.doc'

	nomor = fields.Char(string='Code Dokumen' ,required=True)
	name = fields.Char(string='Jenis Dokumen' ,required=True)