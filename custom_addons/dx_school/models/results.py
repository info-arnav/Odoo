from odoo import api, fields, models

class SchoolResult(models.Model):
    _name = 'school.result'
    _description = 'Result of Students'
    _rec_name = 'name'
    name = fields.Many2one("school.student", string="Student Name")
    result = fields.Char('Student Grade', required=True)
    reference = fields.Char(string='Reference', default="New")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("reference") or vals["reference"] == "New":
                vals["reference"] = self.env["ir.sequence"].next_by_code("school.result")
        return super().create(vals_list)