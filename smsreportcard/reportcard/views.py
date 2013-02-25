from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseRedirect ,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from forms import *
from models import *
import datetime
import basic_admin


"""
DISPLAY THE MAIN PAGE

"""
def path(path):
	return path

def index_number():
	all = list(Student.objects.all())
	last_entry = all[-1]
	id_number = last_entry.id_number + 1
	return id_number

@login_required
def main(request):
	#quering all reports in the system and displaying the recent 5 added
	recent_reports = list(Report.objects.all().order_by('-date_created'))[:5]
	return render_to_response('home/main.html',dict(user=request.user , reports = recent_reports))

@login_required
@csrf_exempt
def add_student(request):
	#number = list(Index.objects.all())[-1].number
	try:
		number = list(Index.objects.all())[-1].number
		new_id_number = number + 1
	except:
		new_id_number = 100
		

	if request.method == 'GET':
		studentform = StudentForm(initial = {'id_number': new_id_number})
		
	if request.method == "POST":
		
		studentform = StudentForm(request.POST)
		if studentform.is_valid():
			student = studentform.save()
			Index.objects.create(number = new_id_number)
			return HttpResponseRedirect(student.get_absolute_url())
	return render_to_response('reportcard/add_student.html' , dict(studentform = studentform , user = request.user ))
	
@login_required
def get_student(request, pk):
	student = Student.objects.filter(id = pk)
	allstudent = Student.objects.all()
	return render_to_response('reportcard/student.html' , dict(student = student , allstudent = allstudent, user = request.user))
@login_required
def all_student(request):
	allstudent = Student.objects.all()
	return render_to_response('reportcard/allstudent.html' , dict(students = allstudent , user = request.user))

@login_required
@csrf_exempt
def add_StudentReport(request , pk ):
	if request.method == 'GET':
		student = Student.objects.get(id = pk)
		course = Course.objects.get(course_name = student.course)
		reportform = ReportForm(initial = {'id_number_student': student.id , 'student_name': student.last_name +' '+ student.middle_name +' '
						   + student.first_name, 'course': student.course , 'teacher':request.user })
		# get all the elective subjects based on the course of the student
		elective_subjects = Elective_subjects.objects.filter(course = course.id)
		core_subjects = ['Core Mathematics' ,'English','Intergrated Science','Social Studies']
		subjects = core_subjects + list(elective_subjects)
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = 'f%s'%i, initial={'subject':subjects[i]}))
			
	if request.method == 'POST':
		p= request.POST
		reportform = ReportForm(request.POST)
		report = None
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(report = report , prefix = 'f%s'%i , data = request.POST ))
				
		student = Student.objects.get(id = pk)
		
		if p['term'] and p['remark']:
			report = Report.objects.create(student = student ,id_number_student=student.id_number, student_name = student.last_name +' '+ student.middle_name +' ' +
					       student.first_name , course = student.course , form = p['form'] , term = p['term'],teacher = request.user , remark = p['remark'])
			report_contentforms = []
			for i in range(8):
				report_contentforms.append(Report_contentForm(report = report , prefix = 'f%s'%i , data = request.POST ))

			for form in report_contentforms:
				if form.is_valid():
					form.save()
				
		#for i in range(8):
			#Report_content.objects.create(report = report , subject = p['f%s-subject' %i] ,exam_mark = p['f%s-exam_mark' %i]  ,
			#test_mark = p['f%s-test_mark' %i] ,percentage = p['f%s-percentage' %i] , grade = p['f%s-grade' %i])
			return HttpResponseRedirect(report.get_absolute_url())
	return render_to_response('reportcard/asr.html' , dict(rform = reportform  , rcform = report_contentforms, user=request.user))
			
	
	pass

"""
View all report of a student
"""
@login_required
def vas(request , studentid):
	studentreports = Report.objects.filter(id_number_student = studentid).order_by("-date_created")
	report_contents = None
	if studentreports:
		
		report_contents = []
		num_reports = len(studentreports)
		for i in range(len(studentreports)):
			report_contents.append(Report_content.objects.filter(report  = studentreports[i]))
		studentinfo = studentreports[0]
		
		reports = {}
		for i in range(len(studentreports)):
			reports[studentreports[i]] = Report_content.objects.filter(report  = studentreports[i])
		print reports

		
		#print list(report_contents)
	else: return HttpResponseRedirect('/report/error404_sys_me_ot/')
	return render_to_response('reportcard/vas.html', dict(number = 1 ,reportcon = report_contents ,reports = reports ,reportsinfo=studentreports,studentinfo = studentreports[0] , num = num_reports,user = request.user))
	

@login_required
def report_detail(request , pk):
	report = Report.objects.filter(id = pk)
	report_content = Report_content.objects.filter(report = pk)
	if not report:
		#return HttpResponse(status=403)
		#response = HttpResponse()
		#response.write("Go away")
		#response.write("come in")
		#return response
		return HttpResponseRedirect('/report/error404_sys_me_ot/')
	return render_to_response('reportcard/report_detail.html', dict(reports = report , pk = pk , subjects = report_content , user = request.user))
@login_required
def display_forms(request):
	if request.method == 'GET':
		reportform = ReportForm()
		remark = RemarkForm()
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = '%s'%i))
		ReportFormSet = formset_factory(Report_contentForm ,extra=8)
		formset = ReportFormSet()

	return render_to_response('reportcard/add_report.html' ,dict(rform = reportform , rcform = report_contentforms , remark = remark ,formset = formset) )

@login_required
def all_reports(request):
	allreports = Report.objects.all().order_by('-date_created')
	for report in allreports:
		print report.student_name
	return render_to_response('reportcard/all.html',dict(allreports = allreports,user = request.user))



@login_required
@csrf_exempt
def add_report(request):
	if request.method == 'GET':
		reportform = ReportForm()
		report_contentforms = []
				
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = 'f%s'%i))
	if request.method == 'POST':
		reportform = ReportForm(request.POST)
		report_contentforms = Report_contentForm()
		if reportform.is_valid():
			report = reportform.save()
			
			report_contentforms = []
			for i in range(8):
				report_contentforms.append(Report_contentForm(report = report , prefix = 'f%s'%i , data = request.POST ))

			for form in report_contentforms:
				if form.is_valid():
					form.save()
			
			return HttpResponseRedirect(report.get_absolute_url())
	return render_to_response('reportcard/add_report.html' , dict(rform = reportform , rcform = report_contentforms , time = datetime.datetime.now() , user = request.user))
@login_required
def error404(request):
	return render_to_response('error/error404.html', dict())

#some add to student function will work on it latter
"""
def add_report(request):
	if request.method == 'GET':
		reportform = ReportForm()
		report_contentforms = []
		#time = datetime.datetime.now()		
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = 'f%s'%i))
	if request.method == 'POST':
		id_number = request.POST['id_number']
		student = { 'student' : str(Student.objects.get(id = id_number)) }
		reportform = ReportForm(student,request.POST)
		report_contentforms = Report_contentForm()
		if reportform.is_valid():
			report = reportform.save()
			
			report_contentforms = []
			for i in range(8):
				report_contentforms.append(Report_contentForm(report = report , prefix = 'f%s'%i , data = request.POST ))

			for form in report_contentforms:
				if form.is_valid():
					form.save()			
			return HttpResponseRedirect(report.get_absolute_url())
	return render_to_response('_reportcard/add_report.html' , dict(rform = reportform , rcform = report_contentforms , time = datetime.datetime.now() , user = request.user))

"""
