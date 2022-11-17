from odoo import fields, models


class SchoolProfile(models.Model):
    _name = "school.profile"

    def get_default_rank(self):
        if 1 == 1:
            return 200
        else:
            return 100

    def default_establish_date(self):
        return fields.Date.today()

    name = fields.Char(string="School Name", help="Esse eh o nome da escola!", size=15, index=True, trim=False,
                       required=True, default="escola padroao")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Suport?", help="esse campo eh boolean", readonly=True,
                                      default=True, )
    school_rank = fields.Integer(sting="Rank", required=True, default=lambda lm: lm.get_default_rank())
    result = fields.Float(string="Result", digits=(2, 4))
    address = fields.Text(string="Adress", help="Esse eh o endereço", default="São paulo, centro, numero: 50")
    estalish_date = fields.Date(string="Estabilish Date", help="Aqui voce seleciona data",
                                default=lambda lm: lm.default_establish_date())
    open_date = fields.Datetime(string="Open Date", help="Aqui voce seleciona data e hora",
                                default=fields.Datetime.now())
    school_type = fields.Selection([('public', 'Public School'), ('private', 'Private School')],
                                   string="Type of School", help="Escolha o tipo de escola")
    documents = fields.Binary(string="Documents", help="Esse é o documento")
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100, max_height=100, verify_resolution="False",
                                help="Essa eh a imagem da escola")
    school_description = fields.Html(string="Description")
