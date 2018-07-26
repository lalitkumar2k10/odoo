from openerp import models, fields


#inherited the existing model
#for initial learning
class Hr_product_template(models.Model):
	_name='product.template'
	_inherit='product.template'
	testdata=fields.Integer("Test Data")

#using
class Hr(models.Model):
	_name='hr'
	_inherit='product.template'
	testdata=fields.Integer("Test Data")

#using
class Hr_detail(models.Model):

	#model name
	_name='hr.detail'

	#simple fields
	name=fields.Char("User Name")
	join_date=fields.Date("Join Date")
	notes=fields.Text("Notes")

	#related fields
	#the _id format means it willbe many2one 
	#the _ids format means it willbe one2many
	#note:-res.users is predefined model
	user_id=fields.Many2one('res.users','Hr User')

	#to link with relative_ids of hr.salary class 
	relative_id=fields.Many2one('hr.team')


#using
class Hr_team(models.Model):

	#model name
	_name='hr.team'

	#simple fields
	name=fields.Char("User Name")
	salary=fields.Integer("Salary")
	remark=fields.Text("Remark")

	#related fields
	#the _id format means it willbe many2one 
	#the _ids format means it willbe one2many
	#note:-res.users is predefined model
	
	#to link with relative_id of hr.detail class 
	relative_ids=fields.One2many('hr.detail','relative_id')
	