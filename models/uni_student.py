from odoo import models, fields, api
from odoo.exceptions import UserError
from  datetime import datetime

class UniStudent(models.Model):
    _name="uni.student"

    name = fields.Char()
    age = fields.Integer()
    birth_date = fields.Date()
    address = fields.Text()
    image = fields.Binary()
    phone = fields.Integer()
    subject_id = fields.Many2many(comodel_name="uni.subject",string="subject")
    department_id = fields.Many2one("uni.department")