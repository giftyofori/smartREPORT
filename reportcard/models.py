from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

 
#from _reportcard.views import index_number
class Index(models.Model):
	number = models.IntegerField(max_length = 10)
	
	def __unicode__(self):
		return str(self.number)
	
	class Meta:
		db_table = 'index'
		
# Funx to create Index Numbers oor system numbers
def get_id_number():
	try:
		id_number = list(Index.objects.all())[-1]
		id_number = id_number.number
		id_number = id_number + 1
		Index.objects.create(number = id_number)
		return id_number
	except : #DoesNotExist :
		return 100


	
	



"""
Course Model
"""
class Course(models.Model):
	course_name = models.CharField(max_length = 50)
	number_student = models.IntegerField("Students Offering Course" ,max_length = 4)
	
	def __unicode__(self):
		return self.course_name	

	class Meta:
		db_table = "course"	
	
# Get All course
def get_course():
	try:
		courses = Course.objects.all()
		course_tuple = ()
		for i in range(len(courses)):
			course_tuple = course_tuple + ((str(courses[i]),str(courses[i])),)
		return course_tuple
	except:
		return (('ATSB','Science'),)


"""
class or SHS level model
"""
class Class(models.Model):
	name = models.CharField(max_length = 20)
	classcode = models.CharField(max_length=5)
	course = models.ForeignKey(Course)
	
	
	def __unicode__(self):
		return self.name
	class Meta:
		db_table = "class"
	

	

		

class Student(models.Model):

	id_number = models.PositiveIntegerField(max_length = 6 , default = get_id_number() , unique = True)
	first_name = models.CharField(max_length = 50 )
	middle_name = models.CharField(max_length = 50 , blank = True , null = True)
	last_name = models.CharField(max_length = 50)
	course = models.CharField(max_length = 50 , choices = get_course())
	form = models.IntegerField(max_length = 1)
	Email = models.EmailField(max_length = 50, blank = True , help_text = "optional" )
	phone_number = PhoneNumberField("Phone Number" , max_length = 13)
	city = models.CharField("City or Town" , max_length = 50)
	country = models.CharField("Nationality" , max_length = 50)
	clas = models.ForeignKey(Class,null = True, blank = True)
	
	
	#created_on = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return str(self.id_number)
	
	def get_absolute_url(self):
		return '/report/student/%s/' % self.id
		
	class Meta: 
		db_table = 'students'
		

class Teaches(models.Model):
	teacher_id = models.IntegerField(max_length= 8)
	subject_name = models.CharField(max_length = 50)

	class_name = models.CharField(max_length = 50)
	period = None
	
	
	def __unicode__(self):
		return self.id


	class Meta:
		db_table = 'teaches'

class Teacher(models.Model):
	#subject = models.ForeignKey(Subject)
	id_number = models.IntegerField(max_length = 6)
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.name
	class Meta:
		db_table = "teacher"


class Student_Info(models.Model):
	student = models.ForeignKey(Student)
	#class_id = models.ForeignKey(Class)
	class_teacher_id = models.ForeignKey(Teacher)
	course = models.CharField(max_length = 50)
	mother_name = models.CharField(max_length = 50)
	father_name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.id

	class Meta:
		db_table = 'student_info'
		verbose_name = "Student Infomation"
		verbose_name_plural = "Student Infomations"


class Subject(models.Model):
	
	name  = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'subject'


class Core_subjects(models.Model):
	subject_name = models.CharField(max_length = 40)

	def __unicode__ (self):
		return self.subject_name

	class Meta:
		db_table = "core subjects"
		verbose_name = "Core Subject"
		permissions = (("Add", "Add Core Subject"),)
'''
# auto save core subjects
core_subjects = ['English', 'Integrated Science', 'Core Mathematics' , 'Social Studies' ]
for i in core_subjects:
	Core_subjects(subject_name = i).save()
'''


class Elective_subjects(models.Model):
	subject_name= models.CharField(max_length = 50)
	course  = models.ForeignKey(Course)

	def __unicode__(self):
		return self.subject_name

	class Meta:
		db_table = "elective subjects"
		verbose_name = "Elective Subject"
		verbose_name_plural = "Elective Subjects"

"""
Get all the Subjects in the system and make a dict out of them
"""
def subjectstuple():
	try:
		core = Subject.objects.all()
		matuple = ()
		for i in range(len(core)):
			matuple = matuple + ((str(core[i]),str(core[i])),)
		return matuple
	except:
		return (("", "Please Go To Subjects and add subjects first"),)

class Report(models.Model):
	FORMS = ((1,"One") ,(2,"Two") , (3 , "Three"))
	TERMS = (("First" ,"First"), ("Second" , "Second") , ("Third", "Third"))
	id_number_student = models.IntegerField("student Id Number" , max_length = 10000)
	date_created = models.DateTimeField(auto_now = True)
	student_name = models.CharField(max_length = 100)
	course = models.CharField(max_length = 50)
	form = models.IntegerField(max_length = 2, choices = FORMS)
	teacher = models.CharField(max_length = 50, default = "logged in user" )
	term = models.CharField(max_length = 10 ,choices = TERMS , default = "First")
	remark = models.TextField(max_length = 300)
	student = models.ForeignKey(Student ,null=True , blank = True)

	def __unicode__(self):
		return self.student_name
	
	def get_absolute_url(self):
		return '/report/detail/%s/' % self.id
	@property
	def get_next(self):
		return '/report/detail/%s/' % self.id


		
	
	def get_prev(self):
		#self.id = self.id - 1
		return 'report/detail/%s/' % self.id

	class Meta:
		db_table = "report"
	

class Report_content(models.Model):
	GRADE = (('A','A'),('B2','B2'),('B3','B3'),('C4','C4'),('C5','C5'),('C6','C6'),('E7','E7'),('E8','E8'),('F9','F9'))
	report = models.ForeignKey(Report)
	subject = models.CharField(max_length = 50 , choices = subjectstuple())
	exam_mark = models.IntegerField("Examination Mark", max_length = 3)
	test_mark = models.IntegerField("Class Test Mark" , max_length = 3)
	percentage = models.IntegerField(max_length = 3)
	grade = models.CharField(max_length = 1, choices = GRADE)

	def __unicode__(self):
		return self.subject

	class Meta:
		db_table = "report content"
		verbose_name = "Report Content"
		
		
