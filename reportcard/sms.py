from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseRedirect ,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from forms import *
from models import *
from dj_simple_sms.models import SMS


def send_sms(request , id):
    # get student object by the id 
    student = Student.objects.get(id = id)
    #get phone number of a student by add the country code and the phone number :: ouput example 2332662829525
    phone_number = student.phone_number.country_code + student.phone_number.national_number
    # with a student object get the report and report content
    report = Report.objects.get(student = id)
    report_content = Report_content.objects.get(report = id)
    
    student_msg = ""
    report_msg = ""
    report_content_msg =""
    
    
    
    for field in report :
        report_msg = report_smg + "Name " + field.student_name +  " Form " + field.form
    
    
    
    
def send_all_sms(request):
    pass
