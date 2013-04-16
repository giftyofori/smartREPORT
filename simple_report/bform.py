
from django import forms
from django.forms import ModelForm
from models import *
from django.forms.fields import MultipleChoiceField ,ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple , Select
from models import Subject

# auto fill subjects by using subjects saved in the database
def auto_fill_subject():
	subject_tuple = ''
	subjects = Subjects.objects.all()
	for subject in subjects:
		subject_tuple = subject_tuple + "( '%s','%s' )," %(subject , subject )
	print subject_tuple[-1]
		
	final_subject_tuple = "( %s )" % subject_tuple
	print final_subject_tuple
	return  final_subject_tuple
		
		
		
		
#auto_fill_subject()
		


'''
print subjects
print tuple(subjects)

for i in subjects:
	for  j in  range(len(subjects)):
		print j
'''		



SUBJECTS = (("ENGLISH" ,"ENGLISH"),
				("CORE MATHS", "CORE MATHS"),
				("SOCIAL " , "SOCIAL "),
				("E-MATHS", "E-MATHS"),
)

GRADE = (("A", "A"),("B" , "B"),("C", "C"),
			("D" , "D"),
			("E" , "E"),
			("F" , "F"),
)


class ReportForm(ModelForm):
	class Meta:
		model = Report
"""
class SubjectForm(forms.Form):
	subject = forms.ChoiceField(widget=Select,choices= SUBJECTS )
	grade = forms.ChoiceField( widget = Select, choices = GRADE )

"""

##original bform
		
class SubjectForm(forms.Form):
	subject = forms.ChoiceField(widget=Select,choices= SUBJECTS )
	grade = forms.ChoiceField( widget = Select, choices = GRADE )

	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(SubjectForm , self).__init__(*args, **kwargs)
		
	def save(self):
		subject = Subject(report = self.report , subject = self.cleaned_data['subject'] , grade= self.cleaned_data['grade'])
		subject.save()
		
	



'''

class ChoiceForm(forms.Form):
    choice = forms.CharField(max_length = 100, widget = forms.Textarea)

    def __init__(self , poll = None , *args, **kwargs):
        self.poll = poll
        super(ChoiceForm, self).__init__(*args,**kwargs)
		
    def save(self):
        choice = models.Choice(poll = self.poll,choice = self.clean_data['choice'])	
        chocie.put()
		
=======
from django import forms
from django.forms import ModelForm
from models import *
from django.forms.fields import MultipleChoiceField ,ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple , Select
from models import Subjects

# auto fill subjects by using subjects saved in the database
def auto_fill_subject():
	subject_tuple = ''
	subjects = Subjects.objects.all()
	for subject in subjects:
		subject_tuple = subject_tuple + "( '%s','%s' )," %(subject , subject )
	print subject_tuple[-1]
		
	final_subject_tuple = "( %s )" % subject_tuple
	print final_subject_tuple
	return  final_subject_tuple
		
		
		
		
auto_fill_subject()
		


'''
'''
print subjects
print tuple(subjects)

for i in subjects:
	for  j in  range(len(subjects)):

		print j
'''
'''		



SUBJECTS = (("ENGLISH" ,"ENGLISH"),
				("CORE MATHS", "CORE MATHS"),
				("SOCIAL " , "SOCIAL "),
				("E-MATHS", "E-MATHS"),
)

GRADE = (("A", "A"),("B" , "B"),("C", "C"),
			("D" , "D"),
			("E" , "E"),
			("F" , "F"),
)


class ReportForm(ModelForm):
	class Meta:
		model = Report
		
class SubjectForm(forms.Form):
	subject = forms.ChoiceField(widget=Select,choices= SUBJECTS )
	grade = forms.ChoiceField( widget = Select, choices = GRADE )
	
	def __init__(self , report = None , *args , **kwargs):
		self.report = report
		super(SubjectForm , self).__init__(*args, **kwargs)
		
	def save(self):
		subject = models.Subject(report = self.report , subject = self.clean_data['subject'])
		grade = models.Subject(report = self.report , subject = self.clean_data['grade'])
		subject.put()
		grade.put()



'''

class ChoiceForm(forms.Form):
    choice = forms.CharField(max_length = 100, widget = forms.Textarea)

    def __init__(self , poll = None , *args, **kwargs):
        self.poll = poll
        super(ChoiceForm, self).__init__(*args,**kwargs)
		
    def save(self):
        choice = models.Choice(poll = self.poll,choice = self.clean_data['choice'])	
        chocie.put()

