from django import forms
from django.forms import ModelForm
import datetime
from django.forms.widgets import Select,RadioSelect
from models import *
from django.utils.translation import ugettext_lazy as _

errormsg_text = {'required' :'Field is required'}
errormsg_int = {'required': 'Field is Required' , 'invalid':'Invalid Entry' ,'max_value':'Maximum Value Exceeded' , 'min_value':'Minivalue Required'}

def make_index_number():
	try :
		students = list(Student.objects.all())
		last_student = students[-1]
		last_student_id_number = last_student.id_number
		new_id_number = last_student_id_number + 1
		return new_id_number
	except :
		return 1990
"""	
def get_course():
	try:
		courses = Course.objects.all()
		course_tuple = ()
		for i in range(len(courses)):
			course_tuple = course_tuple + ((str(courses[i]),str(courses[i])),)
		return course_tuple
	except:
		return (('No Course Available in The System','Science'),)
"""

class StudentForm(ModelForm):
	id_number = forms.CharField(max_length = 10 ,widget=forms.TextInput(attrs={'onKeyPress':"alert(idnum());"}) )
	course = forms.ChoiceField( widget=Select, choices = get_course())
	form = forms.ChoiceField(widget = Select ,choices = Report.FORMS)
	class Meta:
		model = Student
		widgets = {'first_name': forms.TextInput(attrs={"placeholder":"Sir Name"}),'middle_name': forms.TextInput(attrs={"placeholder":"Other Name"}),
			   'last_name': forms.TextInput(attrs={"placeholder":"Last Name"}),'course': forms.TextInput(attrs={"placeholder":"Course"}),
			   'Email': forms.TextInput(attrs={"placeholder":"Email Address","onKeyPress":"helpemail()"}),
			   'phone_number': forms.TextInput(attrs={"placeholder":"Phone Number" ,'onKeyPress':"helpphone();"}),
			   'city': forms.TextInput(attrs={"placeholder":"Town or City"}),
			   'country': forms.TextInput(attrs={"placeholder":"Nationality"}),}

class ReportForm(ModelForm):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	id_number_student = forms.IntegerField(max_value = 1000000)
	student_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'inputstyle' , 'placeholder':'Enter Sudent Name '}))
	form = forms.ChoiceField(widget=forms.Select, choices=FORMS ,initial = "")
	remark = forms.CharField(max_length = 300, required = False,widget=forms.Textarea(attrs={"style":"width:530px ; height:100px"}) ,initial = "Good Work More Room for Improvement")
	class Meta:
		model = Report



class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = "" , widget=forms.TextInput(attrs={'class':'subject','placeholder':'Enter Subject Name Here'}))
	exam_mark = forms.IntegerField(max_value =  100 ,label = "" , initial =70,widget=forms.TextInput(attrs={'class':'intform' ,'placeholder':'Examination Mark' ,'maxlength':'3'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" ,initial =20, widget=forms.TextInput(attrs={'class':'intform' ,'placeholder':'Test Mark','maxlength':'2'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "" , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform' , 'placeholder':'Percentage'}))
	grade = forms.CharField(max_length = 2, required = False , label = "",widget=forms.TextInput(attrs={'class':'grade', 'placeholder':'Grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		#print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		#print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		if percent >= 70:
			grade = "A"
		elif percent <=69 and percent >=65:
			grade = "B2"
		elif percent <=64 and percent >=60:
			grade = "B3"
		elif percent <=59 and percent >=55:
			grade = "C4"
		elif percent <=54 and percent >=50:
			grade = "C5"
		elif percent <=49 and percent >=45:
			grade = "C6"
		elif percent <=44 and percent >=40:
			grade = "E8"
		elif percent <=39 and percent >=0:
			grade = "F9"
		else:
			return None
		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = grade)
		report_content.save()
	def validate_exam_mark(self):
		if self.cleaned_data['exam_mark'] > 100:
			raise forms.ValidationError(_("Examination Mark Cannot be more than 100"))
		return self.cleaned_data['exam_mark']

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")

"""
This form  id used in add report wizzard by a teacher or system user to choose a class
to get all studets in that class offering that subject
"""
class ClassForm(forms.Form):
	CLASSES = (('SC1','SC1'),('SC2','SC2'),)
	classes = forms.ChoiceField(widget=forms.Select(attrs={}), choices=CLASSES)

"""
class ReportForm(forms.Form):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	date_created = forms.DateField(initial=datetime.date.today)
	student_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'size':'50','class':'inputstyle'}))
	course = forms.CharField(max_length = 50)
	form = forms.ChoiceField(widget=forms.Select, choices=FORMS)
	teacher= forms.CharField(max_length = 100 , initial = 'request.user')
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")

	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(forms.Form, self).__init__(*args, **kwargs)

	def save(self):
		report = Report(student_name = self.cleaned_data['student_name'] , date_created = self.cleaned_data['date_created'] , course = self.cleaned_data['course'] , form = self.cleaned_data['form'] , teacher = self.cleaned_data['teacher'] , remark = self.cleaned_data['remark'])
		report.save()
"""	


'''
class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = ""  ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" , widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def grade(self):
		pass
	
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		#calculate grade from percentage
		if percent in range(79,100):

		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = self.cleaned_data['grade'])
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")


"""
Auto fill form section 
"""


class Report_contentForm(forms.Form):
	subject = forms.CharField(max_length = 50 ,label = ""  ,initial = "Marths" , widget=forms.TextInput(attrs={'class':'subject'}))
	exam_mark = forms.IntegerField(max_value =  200 ,label = "" , error_messages = errormsg_int , initial =23,widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	test_mark = forms.IntegerField(max_value =  200 ,label = "" , widget=forms.TextInput(attrs={'class':'intform' , 'id':'intform'}))
	percentage = forms.IntegerField(max_value = 100 , required = False , label = "",initial =100 , widget=forms.TextInput(attrs={'class':'intform' ,'id':'intform'}))
	grade = forms.CharField(max_length = 1 , required = False , label = "" ,initial = "A",widget=forms.TextInput(attrs={'class':'grade','id':'grade'}))


	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(Report_contentForm , self).__init__(*args , **kwargs)
	def save(self):
		_exam_mark = self.cleaned_data['exam_mark']
		_test_mark = self.cleaned_data['test_mark']
		print '70 % of exam mark ' + str(_exam_mark) +' is '  + str(int(_exam_mark * 0.7))
		print '30 % of test mark ' + str(_test_mark) +' is ' + str(int(_test_mark ))
		percent = int(round((_exam_mark * 0.7) + (_test_mark * 1)))
		report_content = Report_content(report = self.report, subject = self.cleaned_data['subject'] , exam_mark = self.cleaned_data['exam_mark'] , test_mark = self.cleaned_data['test_mark'] , percentage = percent, grade = self.cleaned_data['grade'])
		report_content.save()

class RemarkForm(forms.Form):
	remark = forms.CharField(max_length = 300, widget=forms.Textarea(attrs={'class':'remarkstyle'}) ,initial = "Good Work More Room for Improvement")


'''
