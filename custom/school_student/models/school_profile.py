from odoo import models, fields, api


class SchoolProfile(models.Model):
    _inherit = "school.profile"
    school_list = fields.One2many("school.student", "school_id", string="School List")
