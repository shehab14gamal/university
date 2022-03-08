from odoo import models, fields, api
from odoo.exceptions import UserError
from  datetime import datetime

class UniDepartment(models.Model):
    _name="uni.department"


    name = fields.Char()
    capacity = fields.Integer()
    is_open = fields.Boolean()
    subject_id = fields.Many2many(comodel_name="uni.subject",string="subject")
    student_id = fields.One2many("uni.student","department_id")
    teacher_id = fields.One2many("uni.teacher","department_id")
