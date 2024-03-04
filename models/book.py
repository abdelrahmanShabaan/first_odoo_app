from dateutil.relativedelta import relativedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _rec_name = 'code'
    _order = 'id desc'
    _sql_constraints = [
        ('name_unique', 'unique (name)', 'Book name must be unique!'),
    ]

    name = fields.Char('Title', index=True, copy=False)
    code = fields.Char()
    active = fields.Boolean(default=True, readonly=True)
    published_date = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published'),
    ])
    image = fields.Binary()
    publisher_id = fields.Many2one('library.publisher')

    @api.constrains('publisher_id')
    def check_publisher_id(self):
        for rec in self:
            if not rec.publisher_id:
                raise ValidationError('Publisher is required!')

    @api.onchange('code')
    def _onchange_code(self):
        for book in self:
            print('inside _onchange_code Method', book)

    @api.depends('published_date')
    def _compute_age(self):
        for rec in self:
            if rec.published_date:
                rec.age = relativedelta(fields.Date.today(), rec.published_date).years
            else:
                rec.age = False





