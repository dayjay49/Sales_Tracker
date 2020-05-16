from django.shortcuts import render, redirect
from datetime import datetime

from .forms import RawSalesReportForm
from salesStaff.models import SalesStaff

def getSalesReport_view(request):
    report_form = RawSalesReportForm()
    if request.method == "POST":
        report_form = RawSalesReportForm(request.POST)
        if report_form.is_valid():
            staffName = report_form.cleaned_data['staffName']
            staffID = (SalesStaff.objects.get(name=staffName)).id
            startDateTimeObj = report_form.cleaned_data['startDate']
            endDateTimeObj = report_form.cleaned_data['endDate']
            # converting dateTime objects to string so we can send them to next url
            startDateTimeString = startDateTimeObj.strftime("%m/%d/%Y %I:%M %p")
            endDateTimeString = endDateTimeObj.strftime("%m/%d/%Y %I:%M %p")
            request.session['staffName'] = staffName
            request.session['startDate'] = startDateTimeString
            request.session['endDate'] = endDateTimeString
            redirect_url = "report/" + str(staffID)
            return redirect(redirect_url)
    context = {
        'form': report_form
    }
    return render(request, "salesComReport/salesReport_form.html", context)


def postSalesReport_view(request, staff_id):
    staff_name = request.session.get('staffName')
    start_date_string = request.session.get('startDate')
    end_date_string = request.session.get('endDate')

    # convert to DateTime objects so that we can make comparisons with
    # other DateTime objects in the database
    parse_format = '%m/%d/%Y %I:%M %p'
    startDate = datetime.strptime(start_date_string, parse_format)
    endDate = datetime.strptime(end_date_string, parse_format)

    # TO DO: querying to get required information for the report
    commissionRate = (SalesStaff.objects.get(id=staff_id)).commissionRate

    context = {
        'staffName': staff_name,
        'commisionRate': commissionRate
    }
    return render(request, "salesComReport/postSalesReport.html", context)