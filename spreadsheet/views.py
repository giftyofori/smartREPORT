"""
Connections to Google Docs and Spreadsheet Here
"""
from gdata.docs import client , data
import gdata.spreadsheet.service as service
from models import SPKey,Class

email ="smartreport21@gmail.com"
password = "0243637783"

# connection to Google Docs
def gd_connection():
	gd_client = client.DocsClient(source = "Smart Report")
	gd_client.http_client.debug = False
	gd_client.client_login(email="smartreport21@gmail.com",password="0243637783", source="smart report", service="writely")
	return gd_client

def gd_client_connection(spreadsheetkey):
	gd_client = service.SpreadsheetsService(spreadsheetkey)
	gd_client.email = email
	gd_client.password = password
	gd_client.ProgrammaticLogin()
	return gd_client
	


#create a spreadsheet
def create_spreadsheet(title,clas_id):
	client = gd_connection()
	document = data.Resource(type="spreadsheet",title=title)
	document = client.CreateResource(document)
	#get spreadsheet key
	spreadsheetkey = document.GetId().rsplit("%3A")[1]
	#create worksheet or subjects for a class
	createwlksheet(spreadsheetkey)
	#create column headers
	wksheetids = getwksheetID(spreadsheetkey)
	print wksheetids
	for wksheetid in wksheetids:
		createvar(spreadsheetkey,wksheetid)
	clas = Class.objects.get(id=clas_id)
	save_key(clas=clas,spreadsheetkey=spreadsheetkey)
	#client.DeleteResource(document)


#save spreadsheet key to db
def save_key(clas,spreadsheetkey):
    key = SPKey(key=spreadsheetkey,clas=clas)
    key.save()
    
#create the variables for a class spreadsheet
def createwlksheet(spreadsheetkey):
	gd_client = service.SpreadsheetsService(spreadsheetkey)
	gd_client.email = email
	gd_client.password = password
	gd_client.ProgrammaticLogin()
	subjects = ["Core Mathematics","Engilsh","Social Studies","Intergrated Science"]
	for subject in subjects:
		gd_client.AddWorksheet(title=subject,row_count=50,col_count=15,key=spreadsheetkey)
		
def createvar(spreadsheetkey,worksheetkey):
	gd_client = service.SpreadsheetsService(spreadsheetkey,worksheetkey)
	gd_client.email = email
	gd_client.password = password
	gd_client.ProgrammaticLogin()
	var = ["StudentId","StudentName","ClassWrk1","ClassWrk2","ClassWrk3","ClassWrk4","ClassWrk5","ClassWrk6","ClassWrk7","ClassWrk8","ClassWrk9","ClassWrk10","Test1","Test2","ExaminationMarks"]
	for i in range(len(var)):
		gd_client.UpdateCell(row=1,col=i+1,inputValue=var[i],key=spreadsheetkey,wksht_id=worksheetkey)
	return 1

def getwksheetID(spreadsheetkey):
	gd_client = service.SpreadsheetsService(spreadsheetkey)
	gd_client.email = email
	gd_client.password = password
	gd_client.ProgrammaticLogin()
	feed = gd_client.GetWorksheetsFeed(key=spreadsheetkey)
	keys =[]
	for i, entry in enumerate(feed.entry):
		keys.append(entry.id.text.split('/')[-1])
	return keys


def addStudentToWksheet(klass,data):
	spreadsheetkey = str(SPKey.objects.get(clas=klass).key)
	gd_client = gd_client_connection(spreadsheetkey)
	wksheetids= getwksheetID(spreadsheetkey)
	for wksheetid in wksheetids:
		gd_client.InsertRow(row_data=data,key=spreadsheetkey, wksht_id=wksheetid)
	


    

	





