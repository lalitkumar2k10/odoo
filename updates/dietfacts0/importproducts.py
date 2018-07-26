import xmlrpclib
import csv

server="http://localhost:8069"
database='dietfacts2'
user='lalit.kumar@prolitus.com'
pwd='dietfacts2'

common=xmlrpclib.ServerProxy('%s/xmlrpc/2/common'% server)

print common.version()

uid=common.authenticate(database,user,pwd,{})

print uid

OdooApi=xmlrpclib.ServerProxy('%s/xmlrpc/2/object'% server)

filter=[[('categ_id.name','=','Diet Items')]]
#product_count=OdooApi.execute_kw(database,uid,pwd,'product.template','search_count',[[]])
##product_count=OdooApi.execute_kw(database,uid,pwd,'product.template','search_count',filter)

##print product_count


filename='importdata.csv'
reader=csv.reader(open(filename,'rb'))
for row in reader:
	productname=row[0]
	calories=row[1]
	#print productname,calories
	record=[{'name':productname,'calories':calories}]
	OdooApi.execute_kw(database,uid,pwd,'product.template','create',record)
