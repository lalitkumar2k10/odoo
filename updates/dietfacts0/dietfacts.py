#--addons-path=customaddons,addons  -u dietfacts -d dietfacts
from openerp import models, fields,api
#from vobject.base import readOne
class DietFacts_product_template(models.Model):
	_name='product.template'
	_inherit='product.template'
	#my fields in existing model product.template
	calories=fields.Integer("Calories")
	serving_size=fields.Float("Serving Size")
	last_updated=fields.Date("Last Updated")
	is_diet_item=fields.Boolean("Is Diet Item")
	nutrient_ids=fields.One2many('product.template.nutrient','product_id','Nutrients')
	@api.one
	@api.depends('nutrient_ids','nutrient_ids.value')
	def _calcscore(self):
		currentscore=0
		
		for nutrient in self.nutrient_ids:
			currentscore=currentscore+nutrient.value
			print '#####################', currentscore
		self.nutrition_score=currentscore
	nutrition_score=fields.Float(string="Nutrition Score",
								store=True,
								compute="_calcscore")
#my custom model
class DietFacts_res_users_meal(models.Model):
	_name='res.users.meal'
	
	name=fields.Char("Meal Name")
	meal_date=fields.Datetime("Meal Date")
	#after adding mealitem class below
	item_ids=fields.One2many('res.users.mealitems','meal_id')
	largemeal=fields.Boolean("Large Meal")
	
	@api.onchange('totalcalories')
	def check_totalcalories(self):
		if self.totalcalories>1:
			self.largemeal=True
		else:
			self.largemeal=False
		
	
	#user_id=fields.Many2one('out of this many-field,
	# user-id will be assigned a single value',"Label")
	user_id=fields.Many2one('res.users',"Meal User")
	notes=fields.Text("Meal Notes")
	@api.one
	@api.depends('item_ids','item_ids.calories')
	def calc_calories(self):
		currentcalories=0
		for mealitem in self.item_ids:
			currentcalories=currentcalories+(mealitem.calories*mealitem.servings)
		self.totalcalories=currentcalories
	
	totalcalories=fields.Integer(string="Total Calories",
								store=True,
								compute="calc_calories")
	
	
class DietFacts_res_users_mealitems(models.Model):
	_name='res.users.mealitems'
	meal_id=fields.Many2one('res.users.meal')
	item_id=fields.Many2one('product.template')
	servings=fields.Float('servings')
	notes=fields.Text("Meal Item Notes")
	calories=fields.Integer(related='item_id.calories',
						string="calories per serving",
						store=True,
						readonly=True)
	
	
class DietFacts_product_nutrient(models.Model):
	_name='product.nutrient'
	name=fields.Char('Nutrient Name')
	uom_id=fields.Many2one('product.uom','Unit of Measure')
	description=fields.Text('Description')

class DietFacts_product_template_nutrient(models.Model):
	_name='product.template.nutrient'
	nutrient_id=fields.Many2one('product.nutrient',strings='Product Nutrient')
	product_id=fields.Many2one('product.template')
	uom=fields.Char(related='nutrient_id.uom_id.name',string="UOM",readonly=True)
	value=fields.Float('Nutrient Value')
	dailypercent=fields.Float('Daily recommended Value')

class DietFacts_res_users_mealitem(models.Model):
	_name='res.users.mealitem'
	meal_id=fields.Many2one('res.users.meal')









