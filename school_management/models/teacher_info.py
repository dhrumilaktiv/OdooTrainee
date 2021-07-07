from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = "teacher.info"
    _description = "teacher Information"
    # _rec_name = "subject"

    name = fields.Char(string="Name", required=True)
    teacher_school_id = fields.Char(string="Teacher ID", required=True, default="0")
    subject = fields.Char(string="Subject")
    experience = fields.Float(string="Experience")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender"
    )
    email = fields.Char(string="Email")
    student_ids = fields.One2many("student.info", "teacher_id")

    # Constraints of the Program

    _sql_constraints = [
        (
            "id_unique",
            "unique (teacher_school_id)",
            "ID already exists, choose another.",
        )
    ]

    # methods of the program

    def name_get(self):
        teacher_list = []
        for teacher in self:
            teacher_list.append((teacher.id, "{}".format(teacher.name)))
        return teacher_list

    @api.model  # used for create new record in dropdown field
    def name_create(self, name):
        print("self data", self)
        res = super(TeacherInfo, self).name_create(name)
        print("res data", res)
