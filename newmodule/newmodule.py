from openerp import fields, models, exceptions

class NewModule(models.Model):
	_name='newmodule'
	#added below inherit for mail widget
	_inherit='mail.thread'
	name=fields.Many2one('res.partner')
	#create_date
	#__last_update
	description=fields.Char('Description')