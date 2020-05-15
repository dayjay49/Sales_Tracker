from django.shortcuts import render

from .forms import RawSalesEntryForm
from .models import SalesEntry
from drinkOrder.models import DrinkOrder

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
            print(my_form.cleaned_data) 
            currentEntry = SalesEntry.objects.create(staffName=my_form.cleaned_data['staffName'])
            DrinkOrder.objects.create(
                lemonade_name=my_form.cleaned_data['drinkName'],
                quantity=my_form.cleaned_data['quantity'],
                saleEntry_id=currentEntry.id
            )
            my_form = RawSalesEntryForm()
    context = {
        'form': my_form
    }
    return render(request, "salesEntry/salesEntry_create.html", context)

    
