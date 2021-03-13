# Utility imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Local imports
from .filehandler import reader, upload2SQL
from .forms import UploadFileForm

# Dictionary containing Table Description
# {Table_ID: Table_name}

tablename = {
    1: 'Rates',
    2: 'Adj_LTV_Credit_Score',
    3: 'Adj_Cash_Out',
    4: 'Adj_Occupancy_Type',
    5: 'Adj_Loan_Amount',
    6: 'Adj_Property_Type',
    7: 'Adj_Loan_Purpose',
    8: 'Adj_HighBalance',
    9: 'Adj_State',
    10: 'Adj_Other',
}

@login_required
def home(request):
    '''
    Handles the request for route: import

    Recieves the form POST & GET request, saves the posted excel file calls the function to handle and update
    Excel files to DATABASE.
    '''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) #Refernce to form in forms.py
       # print('Recieved POST') # Debug statement for post request
        if form.is_valid():
            # print('Form is Valid') # Debug statement for form validation
            # Saves the uploaded excel file.
            form.save() 

            # function reference filehandler.py
            tables = reader(request.FILES['file']) 

            print('Tables Loaded Successfully!!')

            # Looping through the table description for Table_ID and Table Name.
            for i in tables:
                res = upload2SQL(tables[i], tablename[i]) # function refernce filehandler.py

                # Check for every successully updated Table.
                if res:
                    print(tablename[i]+' Updated')
                else:
                    # Warning Message for any failure during table updation
                    messages.warning(request, f'Database NOT Updated due to some errors!')
                    return redirect('home') # redirection to home route after failure

            # Success Message of Database updation.
            messages.success(request, f'Database Successfully Updated!')
        else:
            # If form submitted is not valid or throughs some errors
            print('Form is invalid')
            messages.warning(request, f'Form not submitted. Error in submitting form! Only Excel files are supported')
    else:
        '''
        If the request in import page is GET request a webpage with empty form is returned
        '''
        form = UploadFileForm()
    return render(request, 'data_import/import_data.html', {'form': form}) # parameters: request type, webpage template and form instance.
