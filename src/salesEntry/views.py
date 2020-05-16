from django.shortcuts import render

from .forms import RawSalesEntryForm
from .models import SalesEntry
from drinkOrder.models import DrinkOrder
from drinkOrder.forms import DrinkOrderFormset
from salesStaff.models import SalesStaff

def saleEntry_create_view(request):
    
    if request.method == "GET":
        salesEntryForm = RawSalesEntryForm(request.GET or None)
        formset = DrinkOrderFormset(queryset=DrinkOrder.objects.none())

    elif request.method == "POST":
        salesEntryForm = RawSalesEntryForm(request.POST)
        formset = DrinkOrderFormset(request.POST)
        if salesEntryForm.is_valid() and formset.is_valid():
            print("BOTH FORMS ARE VALID AND ENTRY IS SAVED")
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

    context= {
        'salesEntryForm': salesEntryForm,
        'formset': formset
    }
    return render(request, "salesEntry/salesEntry_create.html", context)

    # my_form = RawSalesEntryForm()
    # if request.method == "POST":
    #     my_form = RawSalesEntryForm(request.POST)
    #     if my_form.is_valid():
    #         # now the data is good
    #         STAFF_NAME = my_form.cleaned_data['staffName']
    #         LEMONADE_NAME = my_form.cleaned_data['drinkName']
    #         QUANTITY = my_form.cleaned_data['quantity']
            
    #         # get ID of corresponding staff
    #         staffID = (SalesStaff.objects.get(name=STAFF_NAME)).id

    #         currentEntry = SalesEntry.objects.create(
    #             staffName=STAFF_NAME,
    #             staffID=staffID
    #         )

    #         DrinkOrder.objects.create(
    #             lemonade_name=LEMONADE_NAME,
    #             quantity=QUANTITY,
    #             saleEntry=currentEntry
    #         )
    #         my_form = RawSalesEntryForm()
    # context = {
    #     'form': my_form
    # }
    # return render(request, "salesEntry/salesEntry_create.html", context)

    
