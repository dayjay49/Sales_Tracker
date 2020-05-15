from django.shortcuts import render, redirect

# Create your views here.
from .forms import RawSalesReportForm
from salesStaff.models import SalesStaff

def getSalesReport_view(request):
    report_form = RawSalesReportForm()
    if request.method == "POST":
        report_form = RawSalesReportForm(request.POST)
        if report_form.is_valid():
            print(report_form.cleaned_data)
            staffID = (SalesStaff.objects.get(name=report_form.cleaned_data['staffName'])).id
            request.session['staffName'] = report_form.cleaned_data['staffName']
            # request.session['startDate'] = report_form.cleaned_data['startDate']
            # request.session['endDate'] = report_form.cleaned_data['endDate']
            redirect_url = "report/" + str(staffID)
            return redirect(redirect_url)
    context = {
        'form': report_form
    }
    return render(request, "salesComReport/salesReport_form.html", context)


def postSalesReport_view(request, staff_id):
    staff_name = request.session.get('staffName')
    # start_date = request.session.get('startDate')
    # end_date = request.session.get('endDate')
    return render(request, "salesComReport/postSalesReport.html", {})