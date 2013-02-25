
from django.http import HttpResponse, HttpResponseRedirect
from models import *
import bform
from form import ReportForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from dj_simple_sms.models import SMS



def recent(request):
	reports = Report.objects.all()
	
	
	return render_to_response('simple_report/recent.html' , dict(reports = reports))

def detail(request , pk ):
	reports = Report.objects.filter(id = pk)
	subjects = Subject.objects.filter(report = pk)
	return render_to_response('simple_report/detail.html' , dict(reports = reports , pk = pk , subjects = subjects))
	
def report(request , pk):
	""" listing subjects in a report """
	subjects = Subject.objects.filter(report =pk)
	report = Report.objects.get(pk =pk )
	return render_to_response("simple_report/report_detail.html" , dict( subjects = subjects , report = report , pk = pk , name = report.name ))
	

	
	

@csrf_exempt
def add_report(request):
	if request.method == 'GET':
		reportform = bform.ReportForm()
		
		subjectforms = []
		for i in range(8):
			subjectforms.append(bform.SubjectForm(prefix = 'f%s'%i))
	
	if request.method == "POST":
		reportform = bform.ReportForm(request.POST)
		
		subjectform = bform.SubjectForm()
		if reportform.is_valid():
			print reportform.cleaned_data['name']
			report = reportform.save()
			current_report = list(Report.objects.all())[-1].id
			reportid = current_report + 1  
			for i in range(8):

				subject = Subject(report = report, subject = str(request.POST.get('f%d-subject' %i ,'was not found')) , grade = str(request.POST.get('f%d-grade' %i ,'was not found')))
				subject.save()
			return HttpResponseRedirect(report.get_absolute_url())
	return render_to_response('simple_report/add_report.html' , dict(reportform = reportform , subjectforms = subjectforms ))

	
def send_report(request , pk):
	message_one = ""
	message_two = ""
	report = Report.objects.filter(id = pk)
	subjects = Subject.objects.filter(report = pk)
	#phone = Report.objects.get(phone)
	for item in report:
		message_one = message_one + "Name: " + item.name + " Course " + item.course
	for subject in subjects:
		message_two = message_two +" " + subject.subject +":>>" + subject.grade + " " 
	
	response = SMS(to_number = "" , from_number = "SHS" , body = message_one + message_two)
	response.send()
	

	return render_to_response('simple_report/sent.html', dict(message = message_one + message_two))





#original add_form function

@csrf_exempt
def add_report_main(request):
	if request.method == 'GET':
		reportform = bform.ReportForm()
		subjectforms = []
		for i in range(8):
			subjectforms.append(bform.SubjectForm(prefix = 'f%s'%i))
	
	if request.method == "POST":
		reportform = bform.ReportForm(request.POST)
		subjectform = bform.SubjectForm()
		if reportform.is_valid():
			report = reportform.save()
			subjectforms = []
			#data['subject'] = request.POST.get('f%d-subject' %i ,'was not found')
			#data['grade'] = request.POST.get('f%d-grade' %i ,'was not found')
			for i in range(8):
				#subject = request.POST.get('f%d-subject' %i ,'was not found')
				#grade = request.POST.get('f%d-grade' %i ,'was not found')
				#print subject , grade
				subjectforms.append(bform.SubjectForm(report = report , prefix = 'f%s'%i , data = request.POST))
			
			for form in subjectforms:
				if form.is_valid():
					form.save()
			return HttpResponseRedirect(report.get_absolute_url())
	
	return render_to_response('simple_report/add_report.html' , dict(reportform = reportform , subjectforms = subjectforms ))

