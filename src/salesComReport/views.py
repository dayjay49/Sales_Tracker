from django.shortcuts import render, redirect
from datetime import datetime

from .forms import RawSalesReportForm
from salesStaff.models import SalesStaff
from salesEntry.models import SalesEntry
from drinkOrder.models import DrinkOrder
from lemonade.models import Lemonade

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

    # convert to DateTime objects so that we can make comparisons with other DateTime objects in the database
    parse_format = '%m/%d/%Y %I:%M %p'
    startDate = datetime.strptime(start_date_string, parse_format)
    endDate = datetime.strptime(end_date_string, parse_format)

    # Querying to get required information for the report
    commissionRate = (SalesStaff.objects.get(id=staff_id)).commissionRate
    print(commissionRate)

    # filter all entries of input staff between input start date and end date    
    filteredSalesEntries = SalesEntry.objects.filter(
        staffName=staff_name, 
        date__range=(startDate, endDate)
    ).order_by('date')

    # creating a list of dictionaries to store necessary values for each sales entry of the report
    salesEntry_list = []
    sum_total_price = 0
    for entry in filteredSalesEntries:
        items_sold = []
        total_entry_price = 0
        lemonade_orders = DrinkOrder.objects.filter(saleEntry_id=entry.id)
        # print("LEMONADE", lemonade_orders)

        for order in lemonade_orders:
            # since there are no duplicate orders of same drink brand, just append to items_sold
            items_sold.append(order.lemonade_name)
            price = (Lemonade.objects.get(name=order.lemonade_name)).price
            order_price = order.quantity * price
            total_entry_price += order_price

        commission_earned = total_entry_price * commissionRate
        # print(items_sold)
        # print(total_entry_price)
        # print(commission_earned)
        salesEntry_list.append({
            'date': entry.date.strftime("%b %d, %Y %I:%M %p"),
            'items_sold': items_sold,
            'total_price': total_entry_price,
            'commission_earned': commission_earned
        })
        sum_total_price += total_entry_price

    total_com_earned = sum_total_price * commissionRate
    print(salesEntry_list)
    context = {
        'staffName': staff_name,
        'salesEntriesList': salesEntry_list,
        'sum_total_price': sum_total_price,
        'total_com_earned': total_com_earned
    }
    return render(request, "salesComReport/postSalesReport.html", context)