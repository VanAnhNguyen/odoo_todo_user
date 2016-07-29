from openerp import models, fields, api

class UserModel(models.Model):
    _inherit = 'todo.task'
    name = fields.Char('Fullname', required=True)
    birthday = fields.Date('Birthday')
    is_human = fields.Boolean('Human?', defauly=False)
    active= fields.Boolean('Active?', default=True)

    @api.one
    def do_toggle_done(self):
        self.is_human = not self.is_human
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
