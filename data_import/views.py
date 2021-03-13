from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .filehandler import reader, upload2SQL
from .forms import UploadFileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print('Recieved POST')
        if form.is_valid():
            print('Form is Valid')
            form.save()
            tables = reader(request.FILES['file'])
            print('Tables Loaded Successfully!!')
            for i in tables:
                res = upload2SQL(tables[i], tablename[i])
                if res:
                    print(tablename[i]+' Updated')
                else:
                    messages.warning(request, f'Database NOT Updated due to some errors!')
                    return redirect('home')
                messages.success(request, f'Database Successfully Updated!')
        else:
            print('Form is invalid')
            messages.warning(request, f'Form not submitted. Error in submitting form! Only Excel files are supported')
    else:
        form = UploadFileForm()
    return render(request, 'data_import/import_data.html', {'form': form})
