from django.contrib import admin
from models import *
import basic_admin
"""
Adminstaration Customization
"""
class ReportcontentInline(admin.TabularInline):
	model= Report_content
	extra = 1
	classes = ('collapse open',)	
class ReportAdmin(admin.ModelAdmin):
	inlines = [ReportcontentInline]
	list_display = ['student_name' , 'course' , 'teacher','term' , 'date_created']
	list_filter = ['course','term','date_created','teacher']
	order = 0

class ESInline(admin.TabularInline):
	model = Elective_subjects
	extra = 4

class CourseAdmin(admin.ModelAdmin):
	inlines = [ESInline]
	list_display = ['course_name' , 'number_student']
	order = 1
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id_number','first_name','middle_name','last_name','course','form','phone_number']
	list_filter = ['course','form']
	search_fields = ('first_name','middle_name','last_name','course','id_number','city','country','form','phone_number')
	
#admin.site.register(Student)
#admin.site.register(Student_Info)
admin.site.register(Teacher)
#admin.site.register(Teaches)
admin.site.register(Report, ReportAdmin)
#admin.site.register(Report_content)
admin.site.register(Elective_subjects)
admin.site.register(Core_subjects)
admin.site.register(Course , CourseAdmin)
admin.site.register(Subject)
admin.site.register(Index)
basic_admin.site.register(Student,StudentAdmin)