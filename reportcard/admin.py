from django.contrib import admin
from models import *

"""
Adminstaration Customization
"""
class TeachesInline(admin.TabularInline):
	model = Teaches
	extra = 2
class TeacherAdmin(admin.ModelAdmin):
	inlines = [TeachesInline]
	list_display = ['id_number','name','user',]
	list_filter = ['teaches','id_number']
	search_fields = ['name','teaches']



class ReportcontentInline(admin.TabularInline):
	model= Report_content
	extra = 1
	classes = ('collapse open',)	
class ReportAdmin(admin.ModelAdmin):
	inlines = [ReportcontentInline]
	list_display = ['student_name' , 'course' , 'teacher','term' , 'date_created']
	list_filter = ['student_name','course','term','date_created','teacher']
	order = 0

class ESInline(admin.TabularInline):
	model = Elective_subjects
	extra = 4

class CourseAdmin(admin.ModelAdmin):
	inlines = [ESInline]
	list_display = ['course_name']
	order = 1
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id_number','first_name','middle_name','last_name','course','form','phone_number','clas']
	list_filter = ['course','form','clas']
	search_fields = ['first_name','middle_name','last_name','course','id_number','city','country','form','phone_number']
	
class ClassADmin(admin.ModelAdmin):
	list_display = ['name','classcode','course']
	#code

#admin.site.register(Student)
#admin.site.register(Student_Info)
admin.site.register(Teacher,TeacherAdmin)
#admin.site.register(Teaches)
admin.site.register(Report, ReportAdmin)
#admin.site.register(Report_content)
admin.site.register(Elective_subjects)
admin.site.register(Core_subjects)
admin.site.register(Course , CourseAdmin)
admin.site.register(Subject)
admin.site.register(Index)
admin.site.register(Class,ClassADmin)
admin.site.register(Student,StudentAdmin)