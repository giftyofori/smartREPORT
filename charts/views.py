from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sptime import getyear as currentTerm
from reportcard.models import Report,Report_content
piechart ="""
"""

def rmemptyreports(list):
    for item in list:
        if len(item) is 0:
            list.remove(item)
    


def draw(request):
    return HttpResponse(piechart)


def home(request):
    return render_to_response("charts/base.html",dict(user=request.user))


def piechart(request):
    return render_to_response("charts/piechart.html",dict(user=request.user,data1=2,data2=10,data3=3,data4=5,data5=30,data6=27))

def barchart(request):
    return render_to_response('charts/barchart.html',dict())


def CSAS(request,term=None):
    """
    barchart for Core Subjects and Student How Had More Than The Pass Mark 70
    if term is not spercified system uses the current term
    """
    user = request.user
    if user.is_staff:
        if request.method=="GET":
            print term
            if term:
                reports = Report.objects.filter(term=term)
                coremaths = []
                english =[]
                sos = []
                iS = []
                for report in reports:
                    coremaths.append(Report_content.objects.filter(report=report).filter(subject="Core Mathematics").filter(exam_mark__gte=70))
                    english.append(Report_content.objects.filter(report=report).filter(subject="English").filter(exam_mark__gte=70))
                    sos.append(Report_content.objects.filter(report=report).filter(subject="Social Studies").filter(exam_mark__gte=70))
                    iS.append(Report_content.objects.filter(report=report).filter(subject="Intergrated Science").filter(exam_mark__gte=70))
                
                rmemptyreports(coremaths)
                rmemptyreports(english)
                rmemptyreports(sos)
                rmemptyreports(iS)
                
                print coremaths
                print english
                print sos
                print iS
                
                
                
                
            return render_to_response('charts/barchartCSAS.html',dict(data1=len(coremaths),data2=len(english),data3=len(iS),data4=len(sos),))
    else: return HttpRequestPermissionDenied(template ="error/denied.html" ,message="Permission Denied")

