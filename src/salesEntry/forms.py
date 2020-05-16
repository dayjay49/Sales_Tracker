from django import forms

from salesStaff.models import SalesStaff


class RawSalesEntryForm(forms.Form):
    # Staff Name
    staffs = SalesStaff.objects.all().order_by('name')
    staff_dropdown_list = []
    for staff in staffs:
        staff_dropdown_list.append((staff.name, staff.name))
    
    staffName = forms.ChoiceField(
        label='Staff Name',
        choices=staff_dropdown_list
    )
    
    # # Lemonade Name
    # lemonades = Lemonade.objects.all().order_by('name')
    # drink_dropdown_list = []
    # for drink in lemonades:
    #     drink_dropdown_list.append((drink.name, drink.name))

    # drinkName = forms.ChoiceField(
    #     label='Lemonade Brand Name',
    #     choices=drink_dropdown_list
    # )

    # # Quantity
    # quantity = forms.IntegerField(label='Quantity')