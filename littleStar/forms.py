from django import forms
from django.contrib.auth.models import User
from littleStar.models import UserProfileInfo, kiddetails,CreateSchool,anthropometry,Dental, Pediatrics,Nutrition, Opthol

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

 
class UserProfileInfoForm(forms.ModelForm):
     
    class Meta():
        model = UserProfileInfo
        fields = ('doctorSpecialization',)


class nutritionForm(forms.ModelForm):
    childuid = forms.CharField()
    observations = forms.CharField(widget=forms.Textarea)
    recommendations = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = Nutrition
        fields = ('childuid','observations','recommendations')

    def __init__(self, *args, **kwargs):
    
       super(nutritionForm, self).__init__(*args, **kwargs)

       for key in self.fields:
          self.fields[key].required = False  
                

class optholForm(forms.ModelForm):
    binocularfunction = forms.CharField(widget=forms.Textarea)
    accomodationandvergence = forms.CharField(widget=forms.Textarea)
    occulomotorfunction  =forms.CharField(widget=forms.Textarea)
    doctorotheradviceoptions = forms.CharField(widget=forms.Textarea)
    recommendationslistothers = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Opthol
    
        fields = ('Unaidedvisualacuityrighteye','UnaidedvisualacuityLefteye','childuid','Unaidedvisualacuitywithpinholerighteye','Unaidedvisualacuitywithpinholelefteye','Unaidedvisualacuitynearrighteye',
        'Unaidedvisualacuitynearlefteye','visionwithpresentglassesdistancerighteye','visionwithpresentglassesdistancelefteye','visionwithpresentglassesdistancewithpinholerighteye',
        'visionwithpresentglassesdistancewithpinholelefteye','visionwithpresentglassesnearrighteye','visionwithpresentglassesnearlefteye',
        'subjectiverefractionrighteyesph','subjectiverefractionlefteyesph','subjectiverefractionrighteyecyl','subjectiverefractionlefteyecyl',
        'subjectiverefractionrighteyeaxis','subjectiverefractionlefteyeaxis','subjectiverefractionrighteyeadd','subjectiverefractionlefteyeadd',
        'externaleyeexaminationnormal','externaleyeexaminationmeibomitis','externaleyeexaminationblepharitis','externaleyeexaminationchalazion','externaleyeexaminationsyte',
        'externaleyeexaminationcoloboma','externaleyeexaminationepicanthus','externaleyeexaminationentropion',
        'corneanormal','corneaclear','corneascar','corneamegalocornea','corneamicrocornea','corneaedema','corneacornealplana',
        'corneacloudycornea','conjunctivanormal','conjunctivapinguicula','conjunctivapteryguim','conjunctivabitotspots','conjunctivacongestion',
        'irisnormal','irisheterocromia','iriscorectopia','irispolycoria','iriscoloboma','lensnormal','lensclear','lenscataract','lenspseudophakia','lenslenticonus',
        'lenscoloboma','lensmicrospherophakia','ambylopia','strabismusesotropia','strabismusexotropia','strabismusesophoria','strabismusexophoria',
        'pupillaryreflex','accomodationandvergence','binocularfunction','colorvision','occulomotorfunction','provisionaldiagnosisnormal',
        'provisionaldiagnosisnormal','provisionaldiagnosismyopia','provisionaldiagnosishyperopia','provisionaldiagnosisastigmatism',
        'provisionaldiagnosisambylopia','provisionaldiagnosisstrabismus','provisionaldiagnosisnystagmus','provisionaldiagnosisptosis',
        'provisionaldiagnosisconvergence','provisionaldiagnosisinsufficiency','provisionaldiagnosisblepharitis','provisionaldiagnosismeibomitis',
        'provisionaldiagnosiscolorvision','provisionaldiagnosisblindness','provisionaldiagnosismyopiaconditions','provisionaldiagnosishyperopiaconditions',
        'provisionaldiagnosisastigmatismconditions','provisionaldiagnosisstrabismuscondtions','doctoradviceoptions','doctorotheradviceoptions','recommendationslist','recommendationslistothers'

        )
    def __init__(self, *args, **kwargs):
    
       super(optholForm, self).__init__(*args, **kwargs)

       for key in self.fields:
          self.fields[key].required = False 




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
        fields = ('height','weight','headcircumference','midupperarmcircumference','tricepskinfoldness','bmi','bsa','year','kiduid','heartrate','temparature','saturation',
        'respiratoryrate','systolic','diastolic','sign'
        )


