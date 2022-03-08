from odoo import models, fields, api
from odoo.exceptions import UserError
from  datetime import datetime

class UniSubject(models.Model):
    _name="uni.subject"

    name = fields.Char()
    is_open= fields.Boolean()
    department_id = fields.Many2many(comodel_name="uni.department", string="department")
    teacher_id = fields.Many2one("uni.teacher")