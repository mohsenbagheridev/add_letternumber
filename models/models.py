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



    title = fields.Char(string='Title', required=True)
    letter_number = fields.Char(string='Number', required=True, copy=False, index=True, default=lambda self: self.main())
    ln = fields.Char(compute="_value_pc", string='ln', required=True)
    letter_date = fields.Date(string='Date', index=True)

    # @api.depends('folder_id')
    # def _default_name(self):
    #     for record in self:
    #         if len(record.letter_number) != 0:
    #             if record.folder_id.name == 'Internal':
    #                 ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
    #                 return ops
    #             elif record.folder_id.name == 'Finance':
    #                 ops = self.env['ir.sequence'].next_by_code('sale.order.sequence')
    #                 return ops

    @api.depends('folder_id')  
    def main(self):
        ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
        cc = self[0].folder_id
        return cc
        # for record in self:
        #     if(record.folder_id.name == 'Internal'):
        #         ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
        #     elif (record.folder_id.name == 'Finance'):
        #         ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
        #     else:
        #         ops = self.env['ir.sequence'].next_by_code('letter.number.sequence')
        # return ops


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


