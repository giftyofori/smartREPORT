"""
Connections to Google Docs and Spreadsheet Here
"""
from gdata.docs import client , data
from models import SPKey,Class




# connection to Google Docs
def gd_connection():
	gd_client = client.DocsClient(source = "Smart Report")
	gd_client.http_client.debug = False
	gd_client.client_login(email="smartreport21@gmail.com",password="0243637783", source="smart report", service="writely")
	return gd_client

#create a spreadsheet
def create_spreadsheet(title,clas_id):
	client = gd_connection()
	document = data.Resource(type="spreadsheet",title=title)
	document = client.CreateResource(document)
        clas = Class.objects.get(id=clas_id)
        save_key(document=document,clas=clas)
        #client.DeleteResource(document)
        
        
#save spreadsheet key to db
def save_key(document,clas):
    spkey = document.GetId()
    spkey = spkey.rsplit("%3A")[1]
    key = SPKey(key=spkey,clas=clas)
    key.save()
    

	





