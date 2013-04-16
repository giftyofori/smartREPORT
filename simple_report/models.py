from django.db import models
from django.contrib import admin


class Report(models.Model):
	COURSE = (("BUSINESS","BUSINESS"),("SCIENCE","SCIENCE"))


	name = models.CharField("Student Name",max_length=50)
	course = models.CharField( "Student Cource",choices = COURSE , max_length = 20 , default = COURSE[0][0])
	phone = models.IntegerField("Phone Number" , max_length = 10 , default = "0243637783")
	
	def __unicode__(self):
		return self.name
		
	def get_absolute_url(self):
		return '/detail/%s/' % self.id
		
#print Report.objects.get(course = "BUSINESS")	


class Subject(models.Model):

	def select_subject():
		
		pass
	
	GRADE = (
				("A","Grade A"),
				("B" , "Grade B"),
				("C", "Grade C"),
				("D", "Grade D"),
				("E" ,"Grade E"),
				("F" , "Grade F"),
			)
	
	
	
	subject = models.CharField(max_length = 20)
	grade = models.CharField(max_length = 1 , choices = GRADE ,default = GRADE[0][0])
	report = models.ForeignKey(Report)
	
	def __unicode__(self):
		 return self.subject
		 
	def save(self):
		self.title = "maths"
		super(Subject , self).save()
	 
# model created to auto fill the subject column when filling a report	 
class Subjects(models.Model):
	title = models.CharField(max_length = 30)
	
	
	def __unicode__(self):
		return self.title

'''	
	def create(self):
		core_subjects = ['Eng' , 'Math' , 'Sci' , 'SoS']
		for i in core_subject:
			b= 
'''		

class SubjectInline(admin.TabularInline): 
	model = Subject
	extra = 8
		 
class ReportAdmin(admin.ModelAdmin):
	inlines=[SubjectInline]
	list_display = ["name" , "course"]
	
class SubjectAdmin(admin.ModelAdmin):
	extra = 8

# admin interface for class Stubjects	
class SubjectsAdmin(admin.ModelAdmin):
	list_display = ["title"]


# registering models to the admin site to displayed and edited
admin.site.register(Report , ReportAdmin)		
admin.site.register(Subject , SubjectAdmin)		
admin.site.register(Subjects , SubjectsAdmin)		
		 
"""
from django.db import models
from django.contrib import admin


class Report(models.Model):
	COURSE = (("BUSINESS","BUSINESS"),("SCIENCE","SCIENCE"))


	name = models.CharField("Student Name",max_length=50)
	course = models.CharField( "Student Cource",choices = COURSE , max_length = 20 , default = COURSE[0][0])
	phone = models.IntegerField("Phone Number" , max_length = 10 , default = "0243637783")
	
	def __unicode__(self):
		return self.name
		
	def get_absolute(self):
		return 'sr/detail/%s/' % self.id
		
#print Report.objects.get(course = "BUSINESS")	


class Subject(models.Model):

	def select_subject():
		
		pass
	
	GRADE = (
				("A","Grade A"),
				("B" , "Grade B"),
				("C", "Grade C"),
				("D", "Grade D"),
				("E" ,"Grade E"),
				("F" , "Grade F"),
			)
	
	
	
	subject = models.CharField(max_length = 20)
	grade = models.CharField(max_length = 1 , choices = GRADE ,default = GRADE[0][0])
	report = models.ForeignKey(Report)
	
	def __unicode__(self):
		 return self.subject
		 
	def save(self):
		self.title = "maths"
		super(Subject , self).save()
	 
# model created to auto fill the subject column when filling a report	 
class Subjects(models.Model):
	title = models.CharField(max_length = 30)
	
	
	def __unicode__(self):
		return self.title

'''	
	def create(self):
		core_subjects = ['Eng' , 'Math' , 'Sci' , 'SoS']
		for i in core_subject:
			b= 
'''		

class SubjectInline(admin.TabularInline): 
	model = Subject
	extra = 8
		 
class ReportAdmin(admin.ModelAdmin):
	inlines=[SubjectInline]
	list_display = ["name" , "course"]
	
class SubjectAdmin(admin.ModelAdmin):
	extra = 8

# admin interface for class Stubjects	
class SubjectsAdmin(admin.ModelAdmin):
	list_display = ["title"]


# registering models to the admin site to displayed and edited
#admin.site.register(Report , ReportAdmin)		
#admin.site.register(Subject , SubjectAdmin)		
#admin.site.register(Subjects , SubjectsAdmin)		
"""
