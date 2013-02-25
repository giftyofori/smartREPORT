from reportcard.models import Student
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


###system email
systememail = "kwawannor@gmail.com"
###
@login_required
@csrf_exempt
def sendemail(request , id ):
    """
    For send emails toa partitcular student parents
    """
    print request.path
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

@login_required
@csrf_exempt
def sendsms(request ,pk):
    student = Student.objects.get(id = pk)
    phone_number = student.phone_number
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
    
    


