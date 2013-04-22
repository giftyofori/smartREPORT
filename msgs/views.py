from reportcard.models import Student , Report ,Report_content
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import Email , Sms
from forms import Emailform , SMSform
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from dj_simple_sms.models import SMS
from django.core.mail import EmailMessage , send_mail, BadHeaderError ,send_mass_mail
from smsreportcard.settings import EMAIL_SUBJECT_PREFIX as subprfx
from django.contrib.auth.decorators import login_required
from srHttp.HttpRequestPermissionDenied import *
from sptime import getyear as currentTerm


###system email
systememail = "kwawannor@gmail.com"
###
@login_required
@csrf_exempt
def sendemail(request , id ):
    """
    For send emails toa partitcular student parents
    """
    #first checking users permission to send email
    user = request.user
    if user.has_perm("msgs.add_email"):
        p = request.POST
        student = Student.objects.get(id = id)
        studentemail = "scentedvolume3@gmail.com" #str(student.Email)
        if request.method == 'GET':
            emailform = Emailform()
    
        if request.method =='POST':
            emailform = Emailform(request.POST)
            if emailform.is_valid():
                subject = p.get('subject','')
                body = p.get('body','')
                emailsubject = "%(subprfx)s %(subject)s" % {'subprfx':subprfx , 'subject':subject}
                try:
                    email = EmailMessage(emailsubject,body,"kwawannor@gmail.com",['fhim50@gmail.com',])
                    email.send()
                    print "Email sent"
                except:
                    print "Msg not sent"
                try:    
                    Email.objects.create(student = student , subject = subject ,body = body, sent_by=request.user)
                except:
                    print "Email was not saves"
                return HttpResponse("Msg Sent")
        return render_to_response('msgs/sendmsg.html', dict(student = student ,emailform = emailform , user = request.user ,action="email"))
    return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do not Have Permisssion To Send EMAIL To Students")
@login_required
@csrf_exempt
def sendsms(request ,pk):
    student = Student.objects.get(id = pk)
    phone_number = student.phone_number
    user = request.user
    if user.has_perm("msgs.add_sms"):
        if request.method == 'GET':
           smsform = SMSform()
        if request.method == 'POST':
            smsform = SMSform(request.POST)
            #if smsform.is_valid():
            smsbody = request.POST.get('body','')
            smsmsg = SMS(to_number = phone_number , from_number = "SHS" , body = smsbody)
            smsmsg.send()
            try:
                Sms.objects.create(student = student , body = smsbody ,sent_by = request.user)
            except:
                pass
        return render_to_response('msgs/sendmsg.html' ,dict(student = student ,smsform = smsform , user = request.user, action="sms"))
    return HttpRequestPermissionDenied(template ="error/denied.html" ,message="You Do not Have Permisssion To Send SMS To Students")        
  


def _sendsms(request , pk):
    if request.method == "GET":
        report = Report.objects.get(pk = pk)
        reports = Report.objects.filter(pk = pk)
        student = Student.objects.get(id_number = report.id_number_student)
        reportcontent = Report_content.objects.filter(report = report)
        student_details = "%(fname)s %(lname)s\nCourse:%(course)s\n" %{'fname':student.first_name , 'lname':student.last_name ,'course':student.course[:3]}
        message = ''
        for item in reportcontent:
            message = message + "%s %s\n" %(item.subject,item.grade)
        #print student_details+message ; print len(student_details+message)
        message = SMS(to_number = student.phone_number , from_number = "SHS" , body = student_details + message)
        message.send()
        if message:
            status = "Report Sent"
        else:status = "Report Not Sent"
        return render_to_response("reportcard/report_detail.html",dict(reports = reports , subjects = reportcontent,user=request.user,status=status))


#name: sendallreports v0.1
def sarts(request):
    if request.method =="GET":
        currentReports = Report.objects.filter(term = currentTerm)
        #student = Student.objects.get(id_number = report.id_number_student)
        reportsdict = {}
        for report in currentReports:
            reportsdict[report] = Report_content.objects.filter(report = report)
        for report ,reportcontent in reportsdict.items():
            student_number = report.student.phone_number
            student_name = report.student_name
            student_course = report.course
            student_details = 'Name %s\nCourse %s\n' %(student_name,student_course[:3])
            report_details = ''
            for item in reportcontent:
                report_details = report_details + "%s %s\n" %(item.subject,item.grade)
            message = SMS(to_number = student_number,from_number = "SmartReport" ,body = student_details+report_details)
            message.send()
        return HttpResponse("Sending reports")

def sendcurrenetreports(request):
    term = currentTerm
    reports = Report.objects.filter(term = term)
    return render_to_response('msgs/sendcurrenetreports.html',dict(reports=reports,term=term,user=request.user))



def sndmsg(request):
    return render_to_response('msgs/create_msg.html',dict(user=request.user))


def sendbulksms(request , to):
    if request.method == "GET":
        if to == "getform":
            return render_to_response('msgs/sendbulksms.html',dict(smsform = SMSform()))
        if to =="all":
            smsform = SMSform(request.GET)
            return render_to_response('msgs/sendbulksms.html',dict())
        
    pass


@csrf_exempt
def sendsmstoallstudent(request):
    if request.method == "GET":
        smsform = SMSform()
    if request.method =="POST":
        smsmessage = request.POST.get("body","No such Meassage")
        students = Student.objects.all()
        for student in students:
            message = SMS(to_number = student.phone_number , from_number = "SHS" , body = smsmessage)
            message.send()
        return HttpResponse('Sent Messages <a href="/kab234/">GO HOME</a>')
    return render_to_response('msgs/sendsmstoallstudent.html',dict(smsform = smsform))


"""
@csrf_exempt
def sndemail(request , id ):
    p = request.POST
    student = Student.objects.get(id = id)
    studentemail = "scentedvolume3@gmail.com" #str(student.Email)
    if request.method == 'GET':
        emailform = Emailform()

    if request.method =='POST':
            print "Inside post"
            emailform = Emailform(request.POST)
            
        #if p['subject'] and p['body']:
            print "inside studject and body"
            
            #creating msg container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = p['subject']
            msg['From'] = systememail
            msg['To'] = studentemail
            body= str(p['body'])
            #record the MIME types for text/palin
            message = MIMEText(body,"plain")
            #attach parts into message container
            msg.attach(message)
            
            #send the message via  gamil
            
            s = smtplib.SMTP('smtp.gmail.com')
            s.sendmail(systememail,studentemail ,msg.as_string())
            s.quit
            print "email sent"
            
            #print "Error: unable to send email"
            #Email.objects.create(student = student , subject = p['subject'] ,emailmsg = p['body'], sentby=request.user)
            #return HttpResponse("Msg Sent")
    return render_to_response('msgs/sndemail.html', dict(student = student ,emailform = emailform , user = request.user))     
            
        
"""
    
    


