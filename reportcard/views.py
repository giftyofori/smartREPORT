from django.shortcuts import render_to_response
from django import forms
from django.forms.formsets import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseRedirect ,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from forms import *
from models import *
import datetime
from srHttp.HttpRequestPermissionDenied import *
from sptime import getyear as currentTerm
from django.core.exceptions import ObjectDoesNotExist
from spreadsheet.views import addStudentToWksheet
from spreadsheet.models import SPKey
from django.contrib.auth.models import User
from django.shortcuts import redirect


"""
DISPLAY THE MAIN PAGE
"""
def path(path):
	return path

def index_number():
	all = list(Student.objects.all())
	last_entry = all[-1]
	id_number = last_entry.id_number + 1


"""	return id_number
@login_required
def reports():
	user = request.user
	if user.is_staff:
		allstudents =len(Students.objects.all())
	else:return HttpRequestPermissionDenied(template ="error/denied.html" ,message="Permisssion Denied. You Are Not Staff")
"""



@login_required
def openspreadcenter(request):
	if request.method=="GET":
		spreadsheets = SPKey.objects.all()
	return render_to_response('spreadsheet/openspreadsheet.html',dict(spreadsheets=spreadsheets ))

@login_required
def getsp(request):
	key = request.GET.get("spkey","")
	clas=SPKey.objects.get(key=key)
	user = request.user
	klas = clas.clas
	classcode=klas.classcode
	user = User.objects.get(username=user)
	teacher = Teacher.objects.get(user=user)
	teaches = Teaches.objects.filter(teaches=teacher)
	perm_list = []
	for i in teaches:
		perm_list.append(i.classcode)
	if classcode in perm_list:
		url ="https://docs.google.com/spreadsheet/ccc?key=%s#gid=1" %key
		return HttpResponseRedirect(url)
	else:
		return HttpRequestPermissionDenied(template ="error/denied.html" ,message="Permisssion Denied. You Are To A Teacher Of That Class")
	
	return HttpResponse("Done")
		
		
	
	
	
	


@login_required
def main(request):
	user=request.user
	spreadsheets = SPKey.objects.all()
	#quering all reports in the system and displaying the recent 5 added
	recent_reports = list(Report.objects.all().order_by('-date_created'))[:5]
	return render_to_response('home/main.html',dict(user=user , reports = recent_reports))

@login_required
@csrf_exempt
def add_student(request):
	#number = list(Index.objects.all())[-1].number
	user = request.user
	if user.has_perm("reportcard.add_student"):
		try:
			number = list(Index.objects.all())[-1].number
			if not Student.objects.filter(id_number = number) or not Index.objects.filter(number = number):
				new_id_number = number
			else:
				last_student =list(Student.objects.all())[-1]
				new_id_number = last_student.id_number + 1
		except:
			new_id_number = 100000
		

		if request.method == 'GET':
			studentform = StudentForm(initial = {'id_number': new_id_number})
	
	else: return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do Not Have Permisssion To Add Student")
		
	if request.method == "POST":                      
		
		studentform = StudentForm(request.POST)
		postdata = request.POST
		klass = postdata.get("clas",None)
		StudentId = postdata.get("id_number",None)
		StudentName = "%s %s %s" %(postdata.get("first_name",""),postdata.get("middle_name",""),postdata.get("last_name",""))
		data = dict(studentid=StudentId,studentname=StudentName)#,ClassWrk1='',ClassWrk2='',ClassWrk3='',ClassWrk4='',ClassWrk5='',ClassWrk6='',ClassWrk7='',ClassWrk8='',ClassWrk9='',ClassWrk10='',Test1='',Test2='',ExaminationMarks='')
		
		if studentform.is_valid():
			addStudentToWksheet(klass ,data)
			student = studentform.save()
			Index.objects.create(number = new_id_number)
			return HttpResponseRedirect(student.get_absolute_url())
	return render_to_response('reportcard/add_student.html' , dict(studentform = studentform , user = request.user ,idnum = new_id_number ))


@login_required
@csrf_exempt
def edit_student(request,id,studentname):
	user = request.user
	if user.has_perm("reportcard.change_student"):
		student = Student.objects.get(id = id)
		if request.method == "POST":
			studentform = StudentForm(request.POST,instance=student)
			if studentform.is_valid():
				studentform.save()
				return HttpResponseRedirect(student.get_absolute_url())
		else:
			studentform = StudentForm(instance=student)
	else :return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do Not Have Permisssion To Change Student")
	return render_to_response('reportcard/edit_student.html',dict(studentform = studentform , user = request.user ,student=student ,idnum=student.id_number))

	
@login_required
def get_student(request, pk):
	student = Student.objects.filter(id = pk)
	allstudent = Student.objects.all()
	return render_to_response('reportcard/student.html' , dict(student = student , allstudent = allstudent, user = request.user))

@login_required
@csrf_exempt
def compute_reports(request):
	courses = Course.objects.all()
	classes = Class.objects.all()
	class_list = [str(clas.name) for clas in classes]
	course_list=[str(course.course_name) for course in courses]
	data = request.GET
	query = data.get("query","all")
	print query
	if request.method =="GET":
		if query=="all":
			_allstudent = Student.objects.all()
			allstudent = []
			for student in _allstudent:
				try:
					report = Report.objects.get(student=student,term=currentTerm)
				
				except ObjectDoesNotExist:
					allstudent.append(student)
		elif query=="1" or query=="2" or query=="3":
				
			query = int(query)
			_allstudent = Student.objects.filter(form=query)
			print _allstudent
			allstudent = []
			for student in _allstudent:
				try:
					report = Report.objects.get(student=student,term=currentTerm)
				
				except ObjectDoesNotExist:
					allstudent.append(student)
		elif query in class_list:
			clas = Class.objects.get(name=query)
			_allstudent = Student.objects.filter(clas=clas)
			allstudent = []
			print allstudent
			for student in _allstudent:
				try:
					report = Report.objects.get(student=student,term=currentTerm)
				
				except ObjectDoesNotExist:
					allstudent.append(student)
		elif query in course_list:
			_allstudent = Student.objects.filter(course=query)
			allstudent = []
			print allstudent
			for student in _allstudent:
				try:
					report = Report.objects.get(student=student,term=currentTerm)
				
				except ObjectDoesNotExist:
					allstudent.append(student)
	return render_to_response('reportcard/computereport.html' , dict(students = allstudent , user = request.user,courses=courses ,classes=classes))
	pass




@login_required
def all_student(request,query=None,course=None,klass=None):
	courses = Course.objects.all()
	classes = Class.objects.all()
	if not query:
		print 1
		allstudent = Student.objects.all()
	elif query and course=="NoCourse":
		print "2"
		allstudent = Student.objects.filter(form = query)
	elif query and course or klass:
		if course:
			print "in course"
			allstudent = Student.objects.filter(form = query).filter(course = course)
		else :
			print klass
			print "here"
			clas = Class.objects.get(name=klass) 
			allstudent = Student.objects.filter(form=query).filter(clas=clas)
	return render_to_response('reportcard/allstudent.html' , dict(students = allstudent , user = request.user,courses=courses ,classes=classes))

def searchstudent(request):
	courses = Course.objects.all()
	classes = Class.objects.all()
	allstudent = None
	if request.GET:
		allstudent =[]
		query=request.GET.get("searchstudent","No Item searchstudent")
		areastosearch = query.split()
		print areastosearch
		for i in areastosearch:
			try:
				student= Student.objects.get(first_name__icontains=i)
				if student not in allstudent:
					allstudent.append(student)
			except ObjectDoesNotExist:
				pass
			try:
				student = Student.objects.get(last_name__icontains=i)
				if student not in allstudent:
					allstudent.append(student)
			except ObjectDoesNotExist:
				pass
			try:
				student = Student.objects.get(middle_name__icontains=i)
				if student not in allstudent:
					allstudent.append(student)
			except ObjectDoesNotExist:
				pass
				
		
	return render_to_response('reportcard/allstudent.html' , dict(students = allstudent , user = request.user,courses=courses ,classes=classes))
	
	pass


@login_required
@csrf_exempt
def add_StudentReport(request , pk ):
	if request.method == 'GET':
		user = request.user
		if user.has_perm('reportcard.add_report'):
			student = Student.objects.get(id = pk)
			studentreports = Report.objects.filter(student = student)
			hascurent = Report.objects.filter(student=student,term=currentTerm)
			if len(studentreports) > 8:
				return HttpResponseRedirect('/report/syserror__me_ot_mtn9/')
			elif hascurent:
				return HttpResponseRedirect(hascurent[0].get_absolute_url())
			else:
				course = Course.objects.get(course_name = student.course)
				reportform = ReportForm(initial = {'id_number_student': student.id_number , 'student_name': student.last_name +' '+ student.middle_name +' '
						   + student.first_name, 'course': student.course , 'teacher':request.user ,'term':currentTerm})
		# get all the elective subjects based on the course of the student
				elective_subjects = Elective_subjects.objects.filter(course = course.id)
				core_subjects = ['Core Mathematics' ,'English','Intergrated Science','Social Studies']
				subjects = core_subjects + list(elective_subjects)
				report_contentforms = []
				for i in range(8):
					report_contentforms.append(Report_contentForm(prefix = 'f%s'%i, initial={'subject':subjects[i],'exam_mark':random.randint(i+37,100),'test_mark':random.randrange(i+3,30)}))
		else: return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do not Have Permisssion to add report")
			
	if request.method == 'POST':
		student = Student.objects.get(id = pk)
		p= request.POST
		reportform = ReportForm(request.POST)
		report = None
		
		report_contentforms = []
		for i in range(8):
			report_contentforms.append(Report_contentForm(prefix = 'f%s'%i , data = request.POST ))
				
		student = Student.objects.get(id = pk)
	
		if p:
			report = ReportForm(dict(student = student.id,id_number_student=student.id_number, student_name = student.last_name +' '+ student.middle_name +' ' +
					    student.first_name , course = student.course , form = p['form'] , term = p['term'],teacher = request.user , remark= p['remark']))
			report = report.save()
			"""
			report = Report.objects.create(student = student ,id_number_student=student.id_number, student_name = student.last_name +' '+ student.middle_name +' ' +
					       student.first_name , course = student.course , form = p['form'] , term = p['term'],teacher = request.user , remark = p['remark'])
			"""
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
	return render_to_response('reportcard/asr.html' , dict(student = student, rform = reportform  , rcform = report_contentforms, user=request.user))
			
	
	pass

"""
View all report of a student :::vas
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
	else:
		return HttpResponseRedirect('/report/error404_sys_me_ot/')
	return render_to_response('reportcard/vas.html', dict(reportcon = report_contents ,reports = reports ,reportsinfo=studentreports,studentinfo = studentreports[0] , num = num_reports,user = request.user))
	

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

	return render_to_response('reportcard/all.html',dict(allreports = allreports,user = request.user))



@login_required
@csrf_exempt
def add_report(request):
	
	if request.method == 'GET':
		user = request.user
		if user.has_perm('reportcard.add_report'):
			reportform = ReportForm()
			report_contentforms = []
				
			for i in range(8):
				report_contentforms.append(Report_contentForm(prefix = 'f%s'%i))
				
		else: return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do not Have Permisssion to add report")
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

"""
Add Report Wizzard
This function is used to add reports of a particular group of people say sci A
version 0.1
"""
def teaches(user):
	user = User.objects.get(username=user)
	try:
		teacher =  Teacher.objects.get(user=user)
		teaches = Teaches.objects.filter(teaches=teacher)
		klasses = []
		for  i in teaches:
			klass = Class.objects.get(classcode=i.classcode)
			klasses.append(klass)
		
		class_tuple = ()
		for i in range(len(klasses)):
			class_tuple = class_tuple + ((str(klasses[i]),str(klasses[i])),)
		return class_tuple
	except ObjectDoesNotExist:
		return (("None","None"),)	
def teachessubjects(user):
	user = User.objects.get(username=user)
	try:
		teacher =  Teacher.objects.get(user=user)
		teaches = Teaches.objects.filter(teaches=teacher)
		
		teaches_tuple = ()
		for i in range(len(teaches)):
			teaches_tuple = teaches_tuple + ((str(teaches[i].subject),str(teaches[i].subject)),)
		return teaches_tuple
	except ObjectDoesNotExist:
		return (("None","None"),)	



@login_required
def arw_main(request):
	return render_to_response('reportcard/arw_main.html',dict(user=request.user))

def arwstages(request):
	data = request.GET
	user = request.user
	stage=data.get("stage","stageone")
	if stage == "stageone":
		class ClassForm(forms.Form):
			classes = forms.ChoiceField(widget=forms.Select(attrs={'onclick':'nextlink();'}),choices=teaches(user))
		classform=ClassForm()
		return render_to_response('reportcard/arwstage1.html',dict(classform=classform))
def arwstagtwo(request):
	if request.method == "GET":
		data= request.GET
		user=request.user
		klass=data.get("classes","None")
		class SubjectForm(forms.Form):
			clas = forms.CharField(max_length=None,min_length=None,initial=klass, widget=forms.HiddenInput(attrs={}))
			subjects = forms.ChoiceField(widget=forms.Select(attrs={'onclick':'nextlink();'}), choices=teachessubjects(user))
		form = SubjectForm()
	return render_to_response('reportcard/arwstagtwo.html',dict(user=user,form=form))

def arwstagethree(request):
	if request.method =="GET":
		data = request.GET
		clas=data.get('clas','None')
		subjects = data.get('subjects','None')
		clas = Class.objects.get(name=clas)
		allstudent = Student.objects.filter(clas = clas)
		_allstudent = []
		for student in allstudent:
			studentreport = Report.objects.filter(student=student,term=currentTerm)
			if studentreport:
				allstudent.remove(student)
		studentrc={}
		form = Report_contentForm()
		for i in range(len(allstudent)):
			studentrc[allstudent[i]] = form
	if request.method =="POST":
		form = Report_contenForm(request.POST)
		
	
	return render_to_response('reportcard/arwstagethree.html',dict(subjects=subjects,studentrc=studentrc,allstudent=allstudent,form=form,user = request.user))
	

	


@login_required

	

#objects not found
def error404(request):
	return render_to_response('error/error404.html', dict(message="Object Not Found"))
#more than nine(9)
def mt9(request):
	return render_to_response('error/error404.html', dict(message="Student Cannot Have More Than Nine Report Objects", status="mt9",user=request.user))


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
