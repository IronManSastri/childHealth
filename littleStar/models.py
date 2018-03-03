from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
class UserProfileInfo(models.Model):
    specialists = (
        ('pediatrics','Pediatrics'),
        ('opthomology', 'Opthomology'),
        ('audiology','Audiology'),
        ('psychology','Psychology'),
        ('nutrition','Nutrition'),
        ('dental','Dental'),
        ('anthropometry','Anthropometry')
    )
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    doctorSpecialization = models.CharField(max_length=15, choices=specialists, default='pediatrics')

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Pediatrics(models.Model):
    options = {
        ('normal','Normal'),
        ('abnormal','Abnormal')
    }

    generalApperance = models.CharField(max_length=150, choices=options, default='normal')
    generalApperanceRemarks = models.CharField(max_length=300)

    scalpandskin = models.CharField(max_length=150, choices=options, default='normal')
    scalpandskinRemarks = models.CharField(max_length=300)

    lymphNodes = models.CharField(max_length=150, choices=options, default='normal')
    lymphNodesRemarks = models.CharField(max_length=300)

    neck = models.CharField(max_length=150, choices=options, default='normal')
    neckRemarks = models.CharField(max_length=300)

    ears = models.CharField(max_length=150, choices=options, default='normal')
    earsRemarks = models.CharField(max_length=300)

    nose = models.CharField(max_length=150, choices=options, default='normal')
    noseRemarks = models.CharField(max_length=300)

    throatAndOralCavity = models.CharField(max_length=150, choices=options, default='normal')
    throatAndOralCavitytRemarks = models.CharField(max_length=300)

    cardioVascularSystem = models.CharField(max_length=150, choices=options, default='normal')
    cardioVascularSystemRemarks = models.CharField(max_length=300)

    respiratatorySystem = models.CharField(max_length=150, choices=options, default='normal')
    respiratatorySystemRemarks = models.CharField(max_length=300)

    abdomen = models.CharField(max_length=150, choices=options, default='normal')
    abdomenRemarks = models.CharField(max_length=300)

    upperAndLowerExtremities = models.CharField(max_length=150, choices=options, default='normal')
    upperAndLowerExtremitiesRemarks = models.CharField(max_length=300)

    spineGaitAndPosture = models.CharField(max_length=150, choices=options, default='normal')
    spineGaitAndPostureRemarks = models.CharField(max_length=300)

    higherMentalPosture = models.CharField(max_length=150, choices=options, default='normal')
    higherMentalPostureRemarks = models.CharField(max_length=300)

    pediatricRecommendations = models.CharField(max_length=300)

    childuid =  models.CharField(max_length=245, unique = True,primary_key = True)

 




class Dental(models.Model):

    options = {
        ('normal','Normal'),
        ('abnormal','Abnormal')
    }

    optionsTwo = {
        ('present','Present'),
        ('absent','Absent')
    }

    provisionalDiagnosisOptions = {
           ('NO ABNORMALITY DETECTED','NO ABNORMALITY DETECTED'),
           ('ABNORMAL FRENUM','ABNORMAL FRENUM'),
           ('PERIODONTAL ABNORMALITY','PERIODONTAL ABNORMALITY'),
           ('CARIES','CARIES'),
           ('FRACTURED TOOTH/TEETH','FRACTURED TOOTH/TEETH'),
           ('ORTHODONTIC/MALOCCLUSION ABNORMALITIES','ORTHODONTIC/MALOCCLUSION ABNORMALITIES'),
           ('ORTHODONTIC/MALOCCLUSION ABNORMALITIES - OTHERS','ORTHODONTIC/MALOCCLUSION ABNORMALITIES - OTHERS'),
           ('HABITS','HABITS'),
           ('FLUOROSIS','FLUOROSIS'),
           ('ORAL LESION/ ULCER','ORAL LESION/ ULCER'),
           ('ATTRITION','ATTRITION'),
           ('DECIDUOUS','DECIDUOUS'),
           ('OTHERS','OTHERS')
    }

    abnormalFrenumOptions = {
            ('Ankyloglossia','Ankyloglossia'),
            ('High maxillary labial frenum with or without midline diastema','High maxillary labial frenum with or without midline diastema'),
            ('High maxillary labial frenum with nodule','High maxillary labial frenum with nodule'),
            ('High maxillary labial frenum with appendix','High maxillary labial frenum with appendix'),
            ('High maxillary labial frenum with nichum','High maxillary labial frenum with nichum'),
            ('High mandibular labial frenum with or without midline diastema','High mandibular labial frenum with or without midline diastema'),
            ('High mandibular labial frenum with nodule','High mandibular labial frenum with nodule'),
            ('High mandibular labial frenum with appendix','High mandibular labial frenum with appendix'),
            ('High mandibular labial frenum with nichum','High mandibular labial frenum with nichum')
    }

    periodontalAbnormalitiesOptions = {
            ('Stains','Stains'),
            ('Gingivitis','Gingivitis'),
            ('Periodontitis','Periodontitis'),
            ('Gingival Recession','Gingival Recession'),
            ('Calculus','Calculus'),
            ('Plaque','Plaque'),
            ('Halitosis','Halitosis')
    }

    cariesOptions = {
        ('Class I','Class I'),
        ('Class II','Class II'),
        ('Class III','Class III'),
        ('Class IV','Class IV'),
        ('Class V','Class V'),
        ('Class VI','Class VI')
    }

    fracturedorcrackedteethOptions = {
        ('Class I','Class I'),
        ('Class II','Class II'),
        ('Class III','Class III'),
        ('Class IV','Class IV'),
        ('Class V','Class V'),
        ('Class VI','Class VI'),
        ('Class VII','Class VII'),
        ('Class VIII','Class VIII'),
        ('Class IX','Class IX'),
        ('Class X','Class X')
    }

    orthodonticmalocculsionabnormalitiesOptions = {
        ('Class I','Class I'),
        ('Class II','Class II'),
        ('Class II Division 1','Class II Division 1'),
        ('Class II Division 2','Class II Division 2'),
        ('Class II Subdivision','Class II Subdivision'),
        ('Class III','Class III'),
        ('Class III Division 1','Class III Division 1'),
        ('Class III Division 2','Class III Division 2'),
        ('Class III Subdivision','Class III Subdivision')
       
    }

    orthodonticmalocculsionabnormalitiesothersOptions = {
        ('Edge to Edge bite','Edge to Edge bite'),
        ('Open bite- Anterior','Open bite- Anterior'),
        ('Open bite- Posterior','Open bite- Posterior'),
        ('Deep Bite','Deep Bite'),
        ('Cross Bite','Cross Bite'),
        ('Over Bite','Over Bite'),
        ('Over Jet','Over Jet'),
        ('Proclined Maxillary Anteriors','Proclined Maxillary Anteriors'),
        ('Proclined Mandibular Anteriors','Proclined Mandibular Anteriors'),
        ('Protruded Maxilla','Protruded Maxilla'),
        ('Protruded Mandible','Protruded Mandible'),
        ('Crowding /Mal-Aligned','Crowding /Mal-Aligned'),
        ('Spacing','Spacing'),
        ('Midline Diastema','Midline Diastema'),
        ('Tipped','Tipped'),
        ('Rotated','Rotated'),
        ('Palatally inclined','Palatally inclined'),
        ('Lingually inclined','Lingually inclined'),
        ('Midline shift','Midline shift'),
    }

    habitsOptions = {
        ('Tongue thrusting','Tongue thrusting'),
        ('Bruxism','Bruxism'),
        ('Lip biting','Lip biting'),
        ('Mouth breathing','Mouth breathing')
    }

    recommendationsOptions = {
        ('Routine Dental Visit Once In 6 Months','Routine Dental Visit Once In 6 Months'),
        ('Further Investigations and Dentist Consultation.','Further Investigations and Dentist Consultation.')
    }


    mouthfloor = models.CharField(max_length=150, choices=options, default='normal')
    mouthfloorRemarks = models.CharField(max_length=300)

    palate = models.CharField(max_length=150, choices=options, default='normal')
    palateRemarks = models.CharField(max_length=300)

    lips = models.CharField(max_length=150, choices=options, default='normal')
    lipsRemarks = models.CharField(max_length=300)

    cheeks = models.CharField(max_length=150, choices=options, default='normal')
    cheeksRemarks = models.CharField(max_length=300)

    tongue = models.CharField(max_length=150, choices=options, default='normal')
    tongueRemarks = models.CharField(max_length=300)

    throat = models.CharField(max_length=150, choices=options, default='normal')
    throatRemarks = models.CharField(max_length=300)

    frenulam = models.CharField(max_length=150, choices=options, default='normal')
    frenulamRemarks = models.CharField(max_length=300)

    ridges = models.CharField(max_length=150, choices=options, default='normal')
    ridgesRemarks = models.CharField(max_length=300)

    plaque = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    plaqueRemarks = models.CharField(max_length=300)

    stain = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    stainRemarks = models.CharField(max_length=300)

    gingivitis = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    gingivitisRemarks = models.CharField(max_length=300)

    caries = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    cariesRemarks = models.CharField(max_length=300)

    infection = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    infectionRemarks = models.CharField(max_length=300)    

    fracturedorcrackedteeth = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    fracturedorcrackedteethRemarks = models.CharField(max_length=300)  

    habits = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    habitsRemarks = models.CharField(max_length=300)  

    calculus = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    calculusRemarks = models.CharField(max_length=300) 

    malocclusion = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    malocclusionRemarks = models.CharField(max_length=300) 

    impactedwisdomteeth= models.CharField(max_length=150, choices=optionsTwo, default='absent')
    impactedwisdomteethRemarks = models.CharField(max_length=300) 

    provisionalDiagnosisoptions= models.CharField(max_length=150, choices=provisionalDiagnosisOptions,default='NO ABNORMALITY DETECTED')

    abnormalfrenum = models.CharField(max_length=150, choices=abnormalFrenumOptions)

    periodontalabnormalities= models.CharField(max_length=150, choices=periodontalAbnormalitiesOptions)

    cariestypes= models.CharField(max_length=150, choices=cariesOptions)

    fracturedorcrackedteethtypes = models.CharField(max_length=150, choices=fracturedorcrackedteethOptions)

    orthodonticmalocculsionabnormalitiestypes = models.CharField(max_length=150, choices=orthodonticmalocculsionabnormalitiesOptions)

    orthodonticmalocculsionabnormalitiesotherstypes = MultiSelectField(max_length=150, choices=orthodonticmalocculsionabnormalitiesothersOptions)

    habitstypes = models.CharField(max_length=150, choices=habitsOptions)
    
    recommendationtypes = models.CharField(max_length=150, choices=recommendationsOptions,default='Routine Dental Visit Once In 6 Months')

    childuid =  models.CharField(max_length=245, unique = True,primary_key = True)

    def __str__(self):
        return self.childuid 

#create Schools  cariesOptions

class CreateSchool(models.Model):

    schoolName = models.CharField(max_length=250)

    #name of the principal
    principalName = models.CharField(max_length=250)

    #schools Address
    schoolAddress = models.CharField(max_length=500)

    #school Contact Number
    schoolContact = models.CharField(max_length=100)

    #school Contact Number
    schoolUID = models.CharField(max_length=100, primary_key = True)

    #school UID
    # schoolUID = models.CharField(max_length=100,unique = True)

    def __str__(self):
       return self.schoolUID    


class kiddetails(models.Model):

    childname= models.CharField(max_length=245, null = True)

    sex = models.CharField(max_length=245,null = True)

    dob = models.DateField(max_length=245,null = True)

    fathername = models.CharField(max_length=245,null = True)

    fatherphonenumber = models.CharField(max_length=245,null = True)

    fatheremail = models.CharField(max_length=245,null = True)

    mothername = models.CharField(max_length=245,null = True)

    motherphonenumber = models.CharField(max_length=245,null = True)

    motheremail  = models.CharField(max_length=245,null = True)

    address  = models.CharField(max_length=245,null = True)

    teachername = models.CharField(max_length=245,null = True)

    teacheremail  = models.CharField(max_length=245,null = True)

    age = models.CharField(max_length=245,null = True)

    childuid =  models.CharField(max_length=245, unique = True,primary_key = True)

    schooluid =  models.ForeignKey(CreateSchool, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.childname
        
   
   #python manage.py migrate --run-syncdb


class anthropometry(models.Model):

    height = models.CharField(max_length=245,null = True)

    weight = models.CharField(max_length=245,null = True)

    headcircumference = models.CharField(max_length=245,null = True)

    midupperarmcircumference = models.CharField(max_length=245,null = True)

    tricepskinfoldness = models.CharField(max_length=245,null = True)

    bmi= models.CharField(max_length=245)
  
    bsa = models.CharField(max_length=245)

    year = models.CharField(max_length=245)

    kiduid =  models.CharField(max_length=245)
    

    def __str__(self):
        return self.kiduid