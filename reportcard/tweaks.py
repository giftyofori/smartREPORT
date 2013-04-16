from reportcard.models import *
"""
Get all the Subjects in the system and make a dict out of them
"""
def subjectdict():
	core = Core_subjects.objects.all()
	dict1 = {}
	for i in range(4):
		dict1[str(core[i])] = str(core[i])
	return dict1

"""
Get all subjects in the  system and make a tuple out of them
"""

def subjectstuple():
	core = Core_subjects.objects.all()
	tuple = ((str(core[1]) ,str(core[1])),(str(core[2]) ,str(core[2])),)
	return tuple
"""
def subjectstuple():
	core = Core_subjects.objects.all()
	matuple = ()
	for i in range(len(core)):
		matuple = matuple + ((str(core[i]) ,str(core[i]))
"""
