from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sptime import getyear as currentTerm
from reportcard.models import Report,Report_content,Class,Elective_subjects,Student
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
    
    title ="The Performace of All Student In Core Subjects"
    if user.is_staff:
        if request.method=="GET":
            classes = Class.objects.all()
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
                
                for i in range(10):
                    rmemptyreports(coremaths)
                    rmemptyreports(english)
                    rmemptyreports(sos)
                    rmemptyreports(iS)
                
                
                fcoremaths = [] #students how failed core maths
                fenglish =[]#student how failed
                fsos = []#student how failed social studies
                fiS = []#students who failed IS
                
                for report in reports:
                    fcoremaths.append(Report_content.objects.filter(report=report).filter(subject="Core Mathematics").filter(exam_mark__lte=30))
                    fenglish.append(Report_content.objects.filter(report=report).filter(subject="English").filter(exam_mark__lte=30))
                    fsos.append(Report_content.objects.filter(report=report).filter(subject="Social Studies").filter(exam_mark__lte=30))
                    fiS.append(Report_content.objects.filter(report=report).filter(subject="Intergrated Science").filter(exam_mark__lte=30))
                for i in range(10):    
                    rmemptyreports(fcoremaths)
                    rmemptyreports(fenglish)
                    rmemptyreports(fsos)
                    rmemptyreports(fiS)
                
            
            else :
                term = currentTerm
                reports = Report.objects.filter(term=term)
                coremaths = [] #students how passed core maths
                english =[]#student how passed 
                sos = []#student how passed social studies
                iS = []#students how passed  intergrated science
                for report in reports:
                    coremaths.append(Report_content.objects.filter(report=report).filter(subject="Core Mathematics").filter(exam_mark__gte=70))
                    english.append(Report_content.objects.filter(report=report).filter(subject="English").filter(exam_mark__gte=70))
                    sos.append(Report_content.objects.filter(report=report).filter(subject="Social Studies").filter(exam_mark__gte=70))
                    iS.append(Report_content.objects.filter(report=report).filter(subject="Intergrated Science").filter(exam_mark__gte=70))
                
                for i in range(10):
                    rmemptyreports(coremaths)
                    rmemptyreports(english)
                    rmemptyreports(sos)
                    rmemptyreports(iS)
                fcoremaths = [] #students how failed core maths
                fenglish =[]#student how failed
                fsos = []#student how failed social studies
                fiS = []#students who failed IS
                
                for report in reports:
                    fcoremaths.append(Report_content.objects.filter(report=report).filter(subject="Core Mathematics").filter(exam_mark__lte=30))
                    fenglish.append(Report_content.objects.filter(report=report).filter(subject="English").filter(exam_mark__lte=30))
                    fsos.append(Report_content.objects.filter(report=report).filter(subject="Social Studies").filter(exam_mark__lte=30))
                    fiS.append(Report_content.objects.filter(report=report).filter(subject="Intergrated Science").filter(exam_mark__lte=30))
                
                for i in range(10):    
                    rmemptyreports(fcoremaths)
                    rmemptyreports(fenglish)
                    rmemptyreports(fsos)
                    rmemptyreports(fiS)
                
                
            return render_to_response('charts/barchartCSAS.html',dict(user=user,classes=classes,title=title,data1=len(coremaths),data2=len(english),data3=len(iS),data4=len(sos),fdata1=len(fcoremaths),fdata2=len(fenglish),fdata3=len(fiS),fdata4=len(fsos),))
    else: return HttpRequestPermissionDenied(template ="error/denied.html" ,message="Permission Denied")

def POC(request):
    """
    the performance of a class
    """
    user = request.user
    if user.is_staff:
        if request.method =="GET":
            data = request.GET
            klass = data.get("class",None)
            classes = Class.objects.all()
            print klass
            term = data.get("term",None)
            title="Performace of Students in Class %s"%klass
            if klass:
                if term:
                    term = term
                else:
                    term = currentTerm
                klass = Class.objects.get(name=klass)
                course = klass.course
                elect_sub = Elective_subjects.objects.filter(course=course)
                students = Student.objects.filter(clas=klass)
                print students
                reports = []
                for student in students:
                    report = Report.objects.filter(student=student,term=term).order_by("-date_created")
                    if len(report)==0 or report is None:
                        pass
                    else:
                        reports.append(report[0])
                    
                pcoremaths = []
                penglish =[]
                pIS =[]
                pSos=[]
                pelect0=[]
                pelect1=[]
                pelect2=[]
                pelect3=[]
                for report in reports:
                    pcm = Report_content.objects.filter(report=report,subject="Core Mathematics",exam_mark__gte=70)
                    if len(pcm)==0 or pcm is None:
                        pass
                    else:
                        pcoremaths.append(pcm)
                    peng = Report_content.objects.filter(report=report,subject="English",exam_mark__gte=70)
                    if len(peng) ==0 or peng is None:
                        pass
                    else:
                        penglish.append(peng)
                    pis = Report_content.objects.filter(report=report,subject="Intergrated Science",exam_mark__gte=70)
                    if len(pis) ==0 or pis is None:
                        pass
                    else:
                        pIS.append(pis)
                        
                    psos = Report_content.objects.filter(report=report,subject="Social Studies",exam_mark__gte=70)
                    if len(psos) ==0 or psos is None:
                        pass
                    else:
                        pSos.append(psos)
                    pel0 = Report_content.objects.filter(report=report,subject=str(elect_sub[0]),exam_mark__gte=70)
                    if len(pel0)==0 or pel0 is None:
                        pass
                    else:
                        pelect0.append(pel0)
                    pel1 = Report_content.objects.filter(report=report,subject=str(elect_sub[1]),exam_mark__gte=70)
                    if len(pel1)==0 or pel1 is None:
                        pass
                    else:
                        pelect1.append(pel1)
                    pel2 = Report_content.objects.filter(report=report,subject=str(elect_sub[2]),exam_mark__gte=70)
                    if len(pel2)==0 or pel2 is None:
                        pass
                    else:
                        pelect2.append(pel2)
                    pel3 = Report_content.objects.filter(report=report,subject=str(elect_sub[3]),exam_mark__gte=70)
                    if len(pel0)==0 or pel3 is None:
                        pass
                    else:
                        pelect3.append(pel3)
                        
                fcoremaths = []
                fenglish =[]
                fIS =[]
                fSos=[]
                felect0=[]
                felect1=[]
                felect2=[]
                felect3=[]      
                for report in reports:
                    fcm = Report_content.objects.filter(report=report,subject="Core Mathematics",exam_mark__lte=30)
                    if len(fcm)==0 or fcm is None:
                        pass
                    else:
                        fcoremaths.append(fcm)
                    feng = Report_content.objects.filter(report=report,subject="English",exam_mark__lte=30)
                    if len(feng) ==0 or feng is None:
                        pass
                    else:
                        fenglish.append(feng)
                    fis = Report_content.objects.filter(report=report,subject="Intergrated Science",exam_mark__lte=30)
                    if len(fis) ==0 or fis is None:
                        pass
                    else:
                        fIS.append(fis)
                        
                    fsos = Report_content.objects.filter(report=report,subject="Social Studies",exam_mark__lte=30)
                    if len(fsos) ==0 or fsos is None:
                        pass
                    else:
                        fSos.append(psos)
                    fel0 = Report_content.objects.filter(report=report,subject=str(elect_sub[0]),exam_mark__lte=30)
                    if len(fel0)==0 or fel0 is None:
                        pass
                    else:
                        felect0.append(pel0)
                    fel1 = Report_content.objects.filter(report=report,subject=str(elect_sub[1]),exam_mark__lte=30)
                    if len(fel1)==0 or fel1 is None:
                        pass
                    else:
                        felect1.append(fel1)
                    fel2 = Report_content.objects.filter(report=report,subject=str(elect_sub[2]),exam_mark__lte=30)
                    if len(fel2)==0 or fel2 is None:
                        pass
                    else:
                        felect2.append(fel2)
                    fel3 = Report_content.objects.filter(report=report,subject=str(elect_sub[3]),exam_mark__lte=30)
                    if len(fel0)==0 or fel3 is None:
                        pass
                    else:
                        felect3.append(fel3)
                        
                data = dict(user=user,title=title,classes=classes,klass=klass,elect0=elect_sub[0],elect1=elect_sub[1],elect2=elect_sub[2],elect3=elect_sub[3],pdata1=len(pcoremaths),fdata1=len(fcoremaths),pdata2=len(penglish),fdata2=len(fenglish)
                            ,pdata3=len(pIS),fdata3=len(fIS),pdata4=len(pSos),fdata4=len(fSos),pdata5=len(pelect0),
                            fdata5=len(felect0),pdata6=len(pelect1),fdata6=len(felect1),pdata7=len(pelect2),fdata7=len(felect2),pdata8=len(pelect3),fdata8=len(felect3),)        
                
            return render_to_response('charts/barchartPOC.html',data)
    else:
        return HttpRequestPermissionDenied(template ="error/denied.html" ,message="Permission Denied")

    






"""
                
                fcoremaths = [] #students how failed core maths
                fenglish =[]#student how failed
                fsos = []#student how failed social studies
                fiS = []#students who failed IS
                
                for report in reports:
                    cmenteries=Report_content.objects.filter(report=report)
                    cmenteries.filter(subject="Core Mathematics")
                    cmenteries.filter(exam_mark__lte=30)
                    if len(cmenteries) != 0:
                        fcoremaths.append(cmenteries)
                    
                    enenteries=Report_content.objects.filter(report=report)
                    enenteries.filter(subject="English")
                    enenteries.filter(exam_mark__lte=30)
                    if len(enenteries) != 0:
                        fenglish.append(enenteries)
                        
                    sosenteries=Report_content.objects.filter(report=report)
                    sosenteries.filter(subject="Social Studies")
                    sosenteries.filter(exam_mark__lte=30)
                    if len(sosenteries) != 0:
                        fsos.append(sosenteries)
                        
                    isenteries=Report_content.objects.filter(report=report)
                    isenteries.filter(subject="Intergrated Science")
                    isenteries.filter(exam_mark__lte=30)
                    if len(isenteries) != 0:
                        fiS.append(isenteries)
                
                print fcoremaths
                print
                print fenglish
                print
                print fsos
                print fiS
            
"""