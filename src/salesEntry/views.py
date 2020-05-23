from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime

from .forms import RawSalesEntryForm, DrinkOrderFormset, RawSalesReportForm
from .models import SalesEntry, DrinkOrder
from salesStaff.models import SalesStaff
from lemonade.models import Lemonade

def saleEntry_create_view(request):
    
    if request.method == "GET":
        salesEntryForm = RawSalesEntryForm(request.GET or None)
        formset = DrinkOrderFormset(
            queryset=DrinkOrder.objects.none(),
            initial=[{'quantity': 1}],
        )

    elif request.method == "POST":
        salesEntryForm = RawSalesEntryForm(request.POST)
        formset = DrinkOrderFormset(request.POST)
        
        salesEntryValid = salesEntryForm.is_valid()
        formsetValid = formset.is_valid()
        if salesEntryValid and formsetValid:
            # first save the sales entry form, as its reference will be used in
            # 'DrinkOrder'
            STAFF_NAME = salesEntryForm.cleaned_data['staffName']
            staffID = (SalesStaff.objects.get(name=STAFF_NAME)).id
            currentEntry = SalesEntry.objects.create(
                staffName=STAFF_NAME,
                staffID=staffID
            )
            # create drinkOrder instances
            for form in formset:
                drink_order = form.save(commit=False)
                drink_order.saleEntry = currentEntry
                drink_order.save()
            
            messages.success(request, 'The sales entry was successfully saved!')
            return HttpResponseRedirect(request.path_info)

    context = {
        'salesEntryForm': salesEntryForm,
        'formset': formset
    }
    return render(request, "salesEntry/salesEntry_create.html", context)


def load_price(request):
    drink_name = request.GET.get('lemonade')
    price = (Lemonade.objects.get(name=drink_name)).price
    return JsonResponse({'price': price})


def getSalesReport_view(request):
    report_form = RawSalesReportForm()
    if request.method == "POST":
        report_form = RawSalesReportForm(request.POST)
        if report_form.is_valid():
            staffName = report_form.cleaned_data['staffName'].name
            staffID = (SalesStaff.objects.get(name=staffName)).id
            
            startDateTimeObj = report_form.cleaned_data['startDate']
            endDateTimeObj = report_form.cleaned_data['endDate']
            # converting dateTime objects to string so we can send them to next url
            startDateTimeString = startDateTimeObj.strftime("%m/%d/%Y %I:%M %p")
            endDateTimeString = endDateTimeObj.strftime("%m/%d/%Y %I:%M %p")

            request.session['staffName'] = staffName
            request.session['startDate'] = startDateTimeString
            request.session['endDate'] = endDateTimeString

            redirect_url = "/sales/report/" + str(staffID)
            return redirect(redirect_url)
    context = {
        'form': report_form
    }
    return render(request, "salesEntry/salesReport_form.html", context)


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

    # filter all entries of input staff between input start date and end date    
    filteredSalesEntries = SalesEntry.objects.filter(
        staffName=staff_name, 
        date__range=(startDate, endDate)
    ).order_by('date')

    # Only show table if at least one entry made within given datetime range
    if (filteredSalesEntries.count() > 0):
        # creating a list of dictionaries to store necessary values for each sales entry of the report
        salesEntry_list = []
        sum_total_price = 0
        for entry in filteredSalesEntries:

            items_sold = []
            total_entry_price = 0
            lemonade_orders = DrinkOrder.objects.filter(saleEntry_id=entry.id)

            for order in lemonade_orders:
                # make sure there are no duplicates in items_sold list
                if order.lemonade not in items_sold:
                    items_sold.append(order.lemonade)
                price = (Lemonade.objects.get(name=order.lemonade)).price
                order_price = order.quantity * price
                total_entry_price += order_price
            
            # make sure not to show any submitted entry with no sales
            if total_entry_price != 0:
                commission_earned = total_entry_price * commissionRate

                salesEntry_list.append({
                    'date': entry.date.strftime("%b %d, %Y %I:%M %p"),
                    'items_sold': items_sold,
                    'total_price': total_entry_price,
                    'commission_earned': commission_earned
                })
                sum_total_price += total_entry_price

        total_com_earned = sum_total_price * commissionRate
        
        context = {
            'staffName': staff_name,
            'salesEntriesList': salesEntry_list,
            'sum_total_price': sum_total_price,
            'total_com_earned': total_com_earned,
        }
        return render(request, "salesEntry/postSalesReport.html", context)
    else:
        context = {
            'staffName': staff_name,
        }
        return render(request, "salesEntry/noSales.html", context)