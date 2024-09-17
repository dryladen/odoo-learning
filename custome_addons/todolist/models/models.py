# -*- coding: utf-8 -*-

from odoo import models, fields


class Todolist(models.Model):
    _name = 'todolist.todolist'
    _description = 'Table for todo data'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Is Done')
    deadline = fields.Date(string='Deadline')
    user_id = fields.Many2one('res.users', string='User')
    color = fields.Integer(string='Color Index')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ], string='Priority', default='1')
    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

