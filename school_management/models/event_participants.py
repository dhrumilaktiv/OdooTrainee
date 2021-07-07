from odoo import api, fields, models

class EventParticipants(models.Model):
    _name = "participants.info"
    _description = "Event participants information"

    # name = fields.Char(string="Participants name")
    name = fields.Many2one('student.info'
         ,default=lambda self: self._context.get('stu_name'))
    events = fields.Char()

    # default_get method use for get default value
    # events = fields.Char(default=lambda self:self._context.get('stdug'))
    # @api.model
    # def default_get(self, fields_list=[]):
    #     rtn =  super(EventParticipants, self).default_get(fields_list)
    #     print(f"\n\n\n\n\ndhrumil{rtn}{self._context.get('stdug')}\n\n\n\n")

        # try:
        #     rtn['name'] = fields.Many2one(
        # 'res.users', default=lambda self: self.env.user)
        #     return rtn
        # except Exception as e:
        #     print("\n\n\nException\n\n\n", e)
        # return rtn

    # @api.model_create_multi
    # def create(self, vals_list):  # vals_list come in list form
    #     print("\n\n\n\n\n\ncontextmaganlal", self._context.get('stu_name'))
    #     res = super(EventParticipants, self).create(vals_list)
    #     print("ressss", res)
    #     return res