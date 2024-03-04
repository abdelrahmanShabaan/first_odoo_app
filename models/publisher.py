from odoo import fields, models, api


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'Publisher'
    _rec_name = 'f_name'

    f_name = fields.Char()
    l_name = fields.Char()
    date_join = fields.Date()
    active = fields.Boolean(default=True)
    national_id = fields.Char()
    image = fields.Binary()
    book_ids = fields.One2many('library.book', 'publisher_id')
    library_book_ids = fields.Many2many('library.book')



