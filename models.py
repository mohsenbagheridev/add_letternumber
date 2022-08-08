# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class homa_letternumber(models.Model):
#     _name = 'homa_letternumber.homa_letternumber'
#     _description = 'homa_letternumber.homa_letternumber'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api


class hr_fields(models.Model):
    _inherit = ['documents.document']

    def _default_name(self):
        ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
        return ops

    title = fields.Char(string='Title', required=True)
    letter_number = fields.Char(string='Number', required=True, copy=False, index=True, default=lambda self: self._default_name())
    ln = fields.Char(compute="_value_pc", string='ln', required=True)
    letter_date = fields.Date(string='Date', index=True)


    @api.depends('folder_id')
    def _value_pc(self):
        for record in self:
            if record.folder_id.name == 'Internal':
                record.ln = record.folder_id.name
            else:
                record.ln = record.folder_id.name + ' O_o'


    @api.model
    def yep(self):
        return 'mohsen'


