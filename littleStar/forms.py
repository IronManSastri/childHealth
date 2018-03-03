from django import forms
from django.contrib.auth.models import User
from littleStar.models import UserProfileInfo, kiddetails,CreateSchool,anthropometry,Dental, Pediatrics

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

 
class UserProfileInfoForm(forms.ModelForm):
     
    class Meta():
        model = UserProfileInfo
        fields = ('doctorSpecialization',)


class dentalForm(forms.ModelForm):

    class Meta():
        model = Dental

        fields = ('mouthfloor','mouthfloorRemarks','palate','palateRemarks','lips','lipsRemarks','cheeks','cheeksRemarks','tongue','tongueRemarks','throat','throatRemarks','frenulam','frenulamRemarks','ridges','ridgesRemarks'
,'plaque','plaqueRemarks','stain','stainRemarks','gingivitis','gingivitisRemarks','caries','cariesRemarks','infection','infectionRemarks','fracturedorcrackedteeth','fracturedorcrackedteethRemarks','habits','habitsRemarks','calculus','calculusRemarks','malocclusion','malocclusionRemarks','impactedwisdomteeth','impactedwisdomteethRemarks','provisionalDiagnosisoptions','abnormalfrenum',
'periodontalabnormalities','cariestypes','fracturedorcrackedteethtypes','orthodonticmalocculsionabnormalitiestypes','orthodonticmalocculsionabnormalitiesotherstypes','habitstypes',
'recommendationtypes','childuid')

    def __init__(self, *args, **kwargs):
    
       super(dentalForm, self).__init__(*args, **kwargs)

       for key in self.fields:
          self.fields[key].required = False 


class pediatricForm(forms.ModelForm):

    class Meta():
        model=Pediatrics

        fields = ('generalApperance','generalApperanceRemarks','scalpandskin','scalpandskinRemarks','lymphNodes','lymphNodesRemarks','neck','neckRemarks','ears','earsRemarks',
                'nose','noseRemarks','throatAndOralCavity','throatAndOralCavitytRemarks','cardioVascularSystem','cardioVascularSystemRemarks','respiratatorySystem','respiratatorySystemRemarks',
                'abdomen','abdomenRemarks','upperAndLowerExtremities','upperAndLowerExtremitiesRemarks','spineGaitAndPosture','spineGaitAndPostureRemarks','higherMentalPosture','higherMentalPostureRemarks',
                'pediatricRecommendations','childuid')
        
    def __init__(self, *args, **kwargs):
    
       super(pediatricForm, self).__init__(*args, **kwargs)

       for key in self.fields:
          self.fields[key].required = False 
          

class UploadFileForm(forms.Form):
    file = forms.FileField()


class schoolDetailsForm(forms.Form):

    class Meta():
        model = CreateSchool
        fields = ('schoolname','schoolAddress','principalName','schoolContactNumber')

class kidDetailsForm(forms.ModelForm):

    class Meta():
        model = kiddetails
        fields = ("childname","dob","sex")

class anthropometryForm(forms.ModelForm):
    # KID_DETAILS = forms.CharField(widget=forms.HiddenInput, label='')
    class Meta():
        model = anthropometry
        fields = ('height','weight','headcircumference','midupperarmcircumference','tricepskinfoldness','bmi','bsa','year','kiduid')


