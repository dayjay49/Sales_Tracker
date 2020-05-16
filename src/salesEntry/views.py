from django.shortcuts import render

from .forms import RawSalesEntryForm
from .models import SalesEntry
from drinkOrder.models import DrinkOrder
from salesStaff.models import SalesStaff

def saleEntry_create_view(request):
    # my_form = SalesEntryForm(request.POST or None)
    
    # if my_form.is_valid():
    #     my_form.save()
    #     my_form = SalesEntryForm()
    my_form = RawSalesEntryForm()
    if request.method == "POST":
        my_form = RawSalesEntryForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            STAFF_NAME = my_form.cleaned_data['staffName']
            LEMONADE_NAME = my_form.cleaned_data['drinkName']
            QUANTITY = my_form.cleaned_data['quantity']
            
            # get ID of corresponding staff
            staffID = (SalesStaff.objects.get(name=STAFF_NAME)).id

            currentEntry = SalesEntry.objects.create(
                staffName=STAFF_NAME,
                staffID=staffID
            )

            DrinkOrder.objects.create(
                lemonade_name=LEMONADE_NAME,
                quantity=QUANTITY,
                saleEntry=currentEntry
            )
            my_form = RawSalesEntryForm()
    context = {
        'form': my_form
    }
    return render(request, "salesEntry/salesEntry_create.html", context)

    
