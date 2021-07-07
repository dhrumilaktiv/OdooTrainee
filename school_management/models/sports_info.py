import random

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ContactModelSearch(models.Model):
    _inherit = "res.partner"

    """name_search is used for search, by multiple fields in ManytoOne field"""
    try:

        @api.model
        def name_search(self, name, args=None, operator="ilike", limit=100):
            print("self", self)
            print("name", name)
            print("args", args)
            args = args or []
            if name:
                record = self.search(
                    [
                        "|",
                        "|",
                        ("city", operator, name),
                        ("parent_id", operator, name),
                        ("state_id", operator, name),
                    ]
                )
                return record.name_get()
            return super(ContactModelSearch, self).name_search(
                name=name, args=args, operator=operator, limit=limit
            )

    except Exception as e:
        print(e)

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', '|', ('city', operator, name), ('parent_id', operator, name), ('state_id', operator, name)]
    #     contact_id = self.search(domain + args, limit=limit)
    #     return contact_id.name_get()


class SportInfo(models.Model):
    _name = "sport.info"
    _description = "Sports Information"
    _rec_name = "sport_name"

    sport_name = fields.Char(string="Name")
    entry_fee = fields.Integer(string="Entry Fee")
    is_national_level = fields.Boolean(string="National level", default=True)
    contact_name = fields.Many2one("res.partner", string="contact_model_name")
    color = fields.Integer(string="Color Index", default=0)

    # sql Constraints of the Program

    # _sql_constraints = [('fees_check', 'check(entry_fee<501)', 'Maximum fee is 500.')]

    """Python Constraints"""

    @api.constrains("entry_fee")
    def entry_fee_check(self):
        for rec in self:
            if rec.entry_fee > 501:
                raise ValidationError(_("Maximum fee is 500."))

    """if copy data created then (is_national_level) field is default True"""

    def copy(self, default={}):
        print("\n\n\ndefault data\n\n\n", default)
        default["is_national_level"] = True
        res = super(SportInfo, self).copy(default=default)
        return res

    # @api.model_create_multi
    # def create(self, vals_list):
    #     # vals_list.append({'stu_uids': [(0, 0, {}), ()]})
    #     return super(SportInfo, self).create(vals_list)

    # def write(self, vals):
    #     return super(SportInfo, self).write(vals)

    # @api.model_create_multi
    
        
     