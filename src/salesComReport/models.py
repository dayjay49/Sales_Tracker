from django.db import models

# from salesStaff.models import SalesStaff

# class SalesReport(models.Model):

#     staff = models.ForeignKey(
#         SalesStaff,
#         on_delete=models.CASCADE,
#     )

#     startDate = models.DateTimeField(
#         # error_messages={'Invalid': "Please enter in provided format -> MM/DD/YYYY H:M AM/PM"},
#         # label='Start Date and Time',
#         # input_formats = ['%m/%d/%Y %I:%M %p'],
#         # widget=forms.DateInput(attrs={
#         #     'placeholder': 'MM/DD/YYYY H:M AM/PM',
#         #     'required': 'required'
#         # })
#     )

#     endDate = models.DateTimeField(
#         # error_messages={'Invalid': "Please enter in provided format -> MM/DD/YYYY H:M AM/PM"},
#         # label='End Date and Time',
#         # input_formats = ['%m/%d/%Y %I:%M %p'],
#         # widget=forms.DateInput(attrs={
#         #     'placeholder': 'MM/DD/YYYY H:M AM/PM',
#         #     'required': 'required'
#         # })
#     )