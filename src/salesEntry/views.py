from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .forms import RawSalesEntryForm
from .models import SalesEntry
from drinkOrder.models import DrinkOrder
from drinkOrder.forms import DrinkOrderFormset
from salesStaff.models import SalesStaff
from lemonade.models import Lemonade

def saleEntry_create_view(request):
    
    if request.method == "GET":
        salesEntryForm = RawSalesEntryForm(request.GET or None)
        formset = DrinkOrderFormset(
            queryset=DrinkOrder.objects.none(),
            initial=[{'quantity': 1}]
        )
        # lemonades = Lemonade.objects.all()

    elif request.method == "POST":
        salesEntryForm = RawSalesEntryForm(request.POST)
        formset = DrinkOrderFormset(request.POST)
        # readOnlyField = readOnlySingleFieldForm(request.POST)
        salesEntryValid = salesEntryForm.is_valid()
        formsetValid = formset.is_valid()
        if salesEntryValid and formsetValid:
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
            
            messages.success(request, 'The sales entry was successfully saved!')
            return HttpResponseRedirect(request.path_info)

    context= {
        'salesEntryForm': salesEntryForm,
        'formset': formset
    }
    return render(request, "salesEntry/salesEntry_create.html", context)


def load_price(request):
    drink_name = request.GET.get('lemonade')
    price = (Lemonade.objects.get(name=drink_name)).price
    return render(request, "price.html", {"price": price})