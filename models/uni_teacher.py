from odoo import models, fields, api
from odoo.exceptions import UserError
from  datetime import datetime

class UniTeacher(models.Model):
    _name="uni.teacher"

    name = fields.Char()
    department_id = fields.Many2one("uni.department")
    subject_id = fields.One2many("uni.subject","teacher_id")