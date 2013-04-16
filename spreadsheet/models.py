from django.db import models
class Course(models.Model):
	course_name = models.CharField(max_length = 50)
	number_student = models.IntegerField("Students Offering Course" ,max_length = 4)
	
	def __unicode__(self):
		return self.course_name	

	class Meta:
		db_table = "course"	



class Class(models.Model):
	name = models.CharField(max_length = 20)
	classcode = models.CharField(max_length=5)
	course = models.ForeignKey(Course)
	
	
	def __unicode__(self):
		return self.name
	
	def save(self,*args, **kwargs):
		super(Class,self).save(*args, **kwargs)
		clas_id = self.id 
		create_spreadsheet(self.name,clas_id)
	
	
	class Meta:
		db_table = "class"


#stores each class and it spreadsheet key to db
class SPKey(models.Model):
	key = models.CharField(max_length = 50)
	clas = models.ForeignKey(Class)
	
	def __unicode__(self):
		return self.key
	class Meta:
		db_table="spkey"
		
	


