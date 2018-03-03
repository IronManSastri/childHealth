from django.shortcuts import render
from littleStar.forms import UserForm,UploadFileForm,UserProfileInfoForm,schoolDetailsForm,kidDetailsForm,anthropometryForm,dentalForm,pediatricForm
import xlrd
from django.core.files.storage import FileSystemStorage
import datetime
from datetime import date
from django.contrib import messages

from littleStar.models import kiddetails,CreateSchool,UserProfileInfo,anthropometry,Dental,Pediatrics
from django.shortcuts import redirect


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request,'littleStar/index.html')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
 
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

            userSuccessCreationMessage = 'DR '+ str(user) + ' profile has been created'
            
            messages.success(request, userSuccessCreationMessage)

            user_form = UserForm()
        
            profile_form = UserProfileInfoForm()

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'littleStar/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           })

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        
        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)


                #cookie set on login to know the doctor specialization thorugh out
                sessionForDoctorSpecialization = UserProfileInfo.objects.get(user = user )
                request.session['doctorSpecialization'] = sessionForDoctorSpecialization.doctorSpecialization


                # Send the user back to some page.
                # In this case their homepage.
                return render(request, 'littleStar/index.html')
                #return render(request, 'littleStar/index.html',{'doctorSpecialization':doctorSpecialization})
            else:
                # If account is not active:
                return render(request, 'littleStar/login.html',{
                'login_message' : 'The user has been removed',})
        else:
            return render(request, 'littleStar/login.html',{
                'login_message' : 'You have entered the wrong credentials',})

    else:
        #Nothing has been provided for username or password.`
        return render(request, 'littleStar/login.html')

def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def createSchool(request):
    duplicateList = []
    #checking for excel upload
    if request.method == 'POST' and request.FILES['excel']:

        #creating the model instance of the scool directly to get rid of form valdiations
        schoolDetailsUpload = CreateSchool()

        #creating the new data for the table
        schoolDetailsUpload.schoolName = request.POST.get('schoolname')
        schoolDetailsUpload.schoolUID = request.POST.get('schooluid')
        schoolDetailsUpload.schoolAddress = request.POST.get('schoolAddress')
        schoolDetailsUpload.principalName = request.POST.get('principalName')
        schoolDetailsUpload.schoolContact = request.POST.get('schoolContactNumber')

        schoolUidDuplicate = CreateSchool.objects.filter(schoolUID = schoolDetailsUpload.schoolUID )

        if not schoolUidDuplicate:
            #saving data to data base
            schoolDetailsUpload.save()
                #getting the data of the excel in to a variable for parsing
            myfile = request.FILES['excel']

            #using xlrd to parse the exel file
            book = xlrd.open_workbook(myfile.name)

            #getting thwe book sequence to the first
            sheet = book.sheet_by_index(0)

            #looping through all the table rows
            for r in range(1,sheet.nrows):

                #getting the new modal instance every time for new student
                article = kiddetails()

                #assinging the table data to the data table rows directly: bypassing form

                article.childname = sheet.cell(r,0).value
                localDateTime =  sheet.cell(r,1).value
                article.dob	=  datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(r,1).value, book.datemode))
                article.sex	= sheet.cell(r,2).value
                article.fathername =sheet.cell(r,3).value
                article.fatherphonenumber = sheet.cell(r,4).value
                article.fatheremail = sheet.cell(r,5).value
                article.mothername = sheet.cell(r,6).value
                article.motherphonenumber = sheet.cell(r,7).value
                article.motheremail  = sheet.cell(r,8).value
                article.address  = sheet.cell(r,9).value
                article.teachername = sheet.cell(r,10).value
                article.teacheremail  = sheet.cell(r,11).value
                article.age  = calculate_age(datetime.datetime.date(article.dob))
                article.childuid = article.childname[:3].upper() + article.mothername[:3].upper() + str(datetime.datetime.date(article.dob)).split('-')[0][2:]
                article.schooluid =  CreateSchool.objects.get(schoolUID= request.POST.get('schooluid'))
            
                #saving data to data base
              
                kidDuplicate = kiddetails.objects.filter(childuid = article.childuid )
                if not kidDuplicate:
                    article.save()
                else:
                    duplicateList.append(article.childname)
        
        else:
            messages.success(request,"School UID already Exists, Please try another")
    
        messages.success(request,duplicateList)
        return render(request, 'littleStar/createSchool.html')
    return render(request, 'littleStar/createSchool.html')



def detailRedirect(request):
    prefillDetails = {}
    if request.method == 'POST':
        kidUID = request.POST.get('kidDetails')

        try:
            kidIndividualDetails = kiddetails.objects.get(childuid = kidUID )

        except kiddetails.DoesNotExist:
            kidIndividualDetails=None

        else:
            print ("Apress is in the database.")

        if not kidIndividualDetails:
            messages.success(request,'Invalid UID')
            return HttpResponseRedirect(reverse('index'))
        else:

            # To know the specality of doctor so that we can navigate to right page
            if request.session.has_key('doctorSpecialization'):
                doctorSpecialization = request.session['doctorSpecialization'].strip()

            #if doctor belongs to anthropometry
            if (doctorSpecialization == 'anthropometry'):
                kidsAntropometry = navigateToAnthropomentry(request.POST.get('kidDetails'))

                if (kidsAntropometry is not None):
                    return render(request,'littleStar/formCompleted.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization})
                else:
                    return render(request,'littleStar/anthropometry.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization})


            #if doctor belongs to dental
            if (doctorSpecialization == 'dental'):
                kidsDental = checkDentalRecord(request.POST.get('kidDetails'))

                dental_form = dentalForm(data=request.POST)
                if (kidsDental is not None):
                    return render(request,'littleStar/formCompleted.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization})
                else:
                    return render(request,'littleStar/dental.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization,'dentalForm':dental_form})  

            #if doctor belongs to pediatrics
            if (doctorSpecialization == 'pediatrics'):
                kidsPediatric = checkPediatricRecord(request.POST.get('kidDetails'))
                
                if (kidsPediatric is not None):
                    return render(request,'littleStar/formCompleted.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization})
                else:
                    pediatricsForm = pediatricForm(data=request.POST)
                    return render(request,'littleStar/pediatrics.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization,'pediatricsForm':pediatricsForm})  

            # return render(request,'littleStar/details.html',{'kidUID':kidIndividualDetails,'doctorSpecialization':doctorSpecialization})


#check for the record of pediatrics with childuid
def checkPediatricRecord(kidChildUid):
    try:
        kidsPediatric = Pediatrics.objects.get(childuid = kidChildUid)
    except:
        kidsPediatric = None

    return kidsPediatric


#check for the record of dental with childuid
def checkDentalRecord(kidChildUid):
    try:
        kidsDental = Dental.objects.get(childuid = kidChildUid)
    except:
        kidsDental = None
    
    return kidsDental

#check for the record of Anthropometry with childuid
def navigateToAnthropomentry(kidChildUid):

    try:
        kidsAntropometry = anthropometry.objects.get(kiduid = kidChildUid , year = datetime.datetime.now().year)
    except:
        kidsAntropometry = None

    return kidsAntropometry



def anthropometryView(request):
    anthropometry_form = anthropometryForm(data=request.POST)

    if anthropometry_form.is_valid():
        anthropometry_form.save(commit=False)
        anthropometry_form.weight= request.POST["weight"] 
        anthropometry_form.height= request.POST["height"] 
        anthropometry_form.bmi=request.POST["bmi"] 
        anthropometry_form.headcircumference=request.POST["headcircumference"]
        anthropometry_form.midupperarmcircumference= request.POST["midupperarmcircumference"]
        anthropometry_form.tricepskinfoldness=request.POST["tricepskinfoldness"]
        anthropometry_form.bsa=request.POST["bsa"] 
        anthropometry_form.year= request.POST["year"] 
        anthropometry_form.kiduid =request.POST.get('kiduid')
        anthropometry_form.save()
        anthropometryCreationMessage = str(request.POST["kiduid"]) + "'s vitals Data has been created"
        messages.success(request, anthropometryCreationMessage)
        return HttpResponseRedirect(reverse('index'))
 
def dental(request):
    dental_form = dentalForm(data=request.POST)
    
    print(request.POST)
    if request.method == 'POST':

        if dental_form.is_valid():
             dental_form.save()
    
    dentalMessage = str(request.POST["childuid"]) + "'s Dental Data has been created"
    messages.success(request, dentalMessage)
    return HttpResponseRedirect(reverse('index'))
   
def pediatrics(request):

    pediatrics_form = pediatricForm(data=request.POST)
    
    print(request.POST)
    if request.method == 'POST':

        if pediatrics_form.is_valid():
             pediatrics_form.save()

    
    pediatricMessage = str(request.POST["childuid"]) + "'s Pediatrics Data has been created"
    messages.success(request, pediatricMessage)
    return HttpResponseRedirect(reverse('index'))