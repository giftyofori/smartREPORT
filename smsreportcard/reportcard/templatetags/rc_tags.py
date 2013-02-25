from django import template
from reportcard.models import Report
register = template.Library()

#register.filter('cnvt', cnvt)
def cnvt(value,arg):
    studentreports = Report.objects.filter(id_number_student = arg).order_by("-date_created")
    value = studentreports[1][1]
    print "valuse", value
    return value
register.filter('cnvt', cnvt)
