
import csv
from fileinput import filename
from django.shortcuts import render

from firstapp.models import Employee
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,template_name="home.html")        

def csv_export(request):
    all_active_data = Employee.objects.filter(active= True)
    # print(all_active_data)
    # return HttpResponse(all_active_data)
    response = HttpResponse(content_type="text/csv")
    csv_writer = csv.writer(response)
    csv_writer.writerow(["id","Name","Salary","Company","Designation","Active","DOj"])   # all are heders not nessaey to as it si write as model field

    for emp1 in all_active_data.values_list("id","name","salary","company","designation","active","DOj"):
        csv_writer.writerow(emp1)


    response["content-Disposition"] = 'attachement ; filename:"employee_data.csv"'   # this method is help csv file download from webpage
    return response