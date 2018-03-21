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

class Opthol(models.Model):

    sightOptions = {
        ('lesstThanSixBySixty','<6/60'),
        ('sixBySixty','6/60'),
        ('sixByThirtySix','6/36'),
        ('sixByTwentyFour','6/24'),
        ('sixByEighteen','6/18'),
        ('sixByTwelve','6/12'),
        ('sixByNine','6/9'),
        ('sixBySix','6/6')
    } 
    nearSightOptions = {
        ('nthirtysix','N36'),
        ('ntwentyfour','N24'),
        ('neighteen','N18'),
        ('ntwelve','N12'),
        ('nten','N10'),
        ('neight','N8'),
        ('nsix','N6')
    }

    eyeConditions = {
        ('right','Right'),
        ('left','Left'),
        ('both','Both'),
        ('none','None')
    }

    reflex = {
        ('roundandreacting','Round and Reacting'),
        ('irregular','Irregular')
    }

    colorvisionoptions = {
        ('redgreencolorblindness','RED-GREEN COLOR BLINDNESS'),
        ('blueyellowcolorblindness','BLUE-YELLOW COLOR BLINDNESS'),
        ('completecolorblindness','COMPLETE COLOR BLINDNESS'),
        ('abnormal','Abnormal'),
        ('normal','Normal')
    }

    provisionaldiagnosisoptions = {
        ('suspectingrighteye','SUSPECTING RIGHT EYE'),
        ('suspectinglefteye','SUSPECTING LEFT EYE'),
        ('bilateral','Bilateral'),
        ('knowncaseof','Known Case Of'),
        ('none','None')
    }
    provisionaldiagnosismyopiaconditionsoptions = {
        ('axialmyopia','Axial Myopia'),
        ('curvaturalmyopia','Curvatural Myopia'),
        ('positionalmyopia','Positional Myopia'),
        ('indexmyopia','Index Myopia'),
        ('myopiaduetoexcessiveaccommodation','Myopia due to excessive accommodation')
    }

    provisionaldiagnosishyperopiaconditionoptions = {
        ('axialhypermetropia','Axial Hypermetropia'),
        ('curvaturalhypermetropia','Curvatural Hypermetropia'),
        ('indexhypermetropia','Index Hypermetropia'),
        ('positionalhypermetropia','Positional Hypermetropia'),
        ('absenceofcrystallinelens','Absence of Crystalline Lens')
    }

    provisionaldiagnosisastigmatismconditionsoptions = {
        ('simpleastigmatism','Simple Astigmatism'),
        ('compoundastigmatism','Compound Astigmatism'),
        ('mixedastigmatism','Mixed Astigmatism')
    }

    provisionaldiagnosisstrabismuscondtionsoptions = {
        ('esotropia','Esotropia'),
        ('exotropia','Exotropia'),
        ('esophoria','Esophoria'),
        ('exophoria','Exophoria')
    }

    adviceoptions = {
        ('visitaneyehospitalattheearliest','Visit an eye hospital at the earliest'),
        ('needsroutineeyetestafter6months','Needs routine eye test after 6 months'),
        ('needsroutineeyetesteveryyear','Needs routine eye test every year'),
        ('others','Others')
    }

    recommendationsoptions = {
        ('noactionrequiredimmediately','No action required immediately'),
        ('continuewiththesameglasses','Continue with the same glasses'),
        ('duetorefractive','Due to Refractive (Power) change, needs to change glasses'),
        ('advisedglassesatschoolhealthprescriptiongiven','Advised glasses at School Health, Prescription given'),
        ('needsreconfirmation','Advised glasses at School Health, Needs Re-Confirmation'),
        ('pleasecontact','Please contact an Ophthalmologist / Eye Hospital for consultation'),
        ('confirmation','Please contact an Optometrist for detailed re-evaluation &amp; confirmation'),
        ('others','Others')
    }



    Unaidedvisualacuityrighteye = models.CharField(max_length=150,choices=sightOptions)
    UnaidedvisualacuityLefteye = models.CharField(max_length=150,choices=sightOptions)

    Unaidedvisualacuitywithpinholerighteye = models.CharField(max_length=150,choices=sightOptions)
    Unaidedvisualacuitywithpinholelefteye = models.CharField(max_length=150,choices=sightOptions)

    Unaidedvisualacuitynearrighteye = models.CharField(max_length=150,choices=nearSightOptions)
    Unaidedvisualacuitynearlefteye = models.CharField(max_length=150,choices=nearSightOptions)

    visionwithpresentglassesdistancerighteye = models.CharField(max_length=150,choices=sightOptions)
    visionwithpresentglassesdistancelefteye = models.CharField(max_length=150,choices=sightOptions)

    visionwithpresentglassesdistancewithpinholerighteye = models.CharField(max_length=150,choices=sightOptions)
    visionwithpresentglassesdistancewithpinholelefteye = models.CharField(max_length=150,choices=sightOptions)

    visionwithpresentglassesnearrighteye = models.CharField(max_length=150,choices=nearSightOptions)
    visionwithpresentglassesnearlefteye = models.CharField(max_length=150,choices=nearSightOptions)

    subjectiverefractionrighteyesph = models.CharField(max_length=150)
    subjectiverefractionlefteyesph = models.CharField(max_length=150)

    subjectiverefractionrighteyecyl = models.CharField(max_length=150)
    subjectiverefractionlefteyecyl = models.CharField(max_length=150)

    subjectiverefractionrighteyeaxis = models.CharField(max_length=150)
    subjectiverefractionlefteyeaxis = models.CharField(max_length=150)

    subjectiverefractionrighteyeadd = models.CharField(max_length=150)
    subjectiverefractionlefteyeadd = models.CharField(max_length=150)

    externaleyeexaminationnormal = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationmeibomitis = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationblepharitis = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationchalazion = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationsyte = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationcoloboma = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationepicanthus = models.CharField(max_length=150,choices=eyeConditions)
    externaleyeexaminationentropion = models.CharField(max_length=150,choices=eyeConditions)

    corneanormal = models.CharField(max_length=150,choices=eyeConditions)
    corneaclear = models.CharField(max_length=150,choices=eyeConditions)
    corneascar = models.CharField(max_length=150,choices=eyeConditions)
    corneamegalocornea = models.CharField(max_length=150,choices=eyeConditions)
    corneamicrocornea = models.CharField(max_length=150,choices=eyeConditions)
    corneaedema = models.CharField(max_length=150,choices=eyeConditions)
    corneacornealplana = models.CharField(max_length=150,choices=eyeConditions)
    corneacloudycornea = models.CharField(max_length=150,choices=eyeConditions)

 
    conjunctivanormal = models.CharField(max_length=150,choices=eyeConditions)
    conjunctivapinguicula = models.CharField(max_length=150,choices=eyeConditions)
    conjunctivapteryguim = models.CharField(max_length=150,choices=eyeConditions)
    conjunctivabitotspots = models.CharField(max_length=150,choices=eyeConditions)
    conjunctivacongestion = models.CharField(max_length=150,choices=eyeConditions)

    irisnormal = models.CharField(max_length=150,choices=eyeConditions)
    irisheterocromia = models.CharField(max_length=150,choices=eyeConditions)
    iriscorectopia = models.CharField(max_length=150,choices=eyeConditions)
    irispolycoria = models.CharField(max_length=150,choices=eyeConditions)
    iriscoloboma = models.CharField(max_length=150,choices=eyeConditions)

    lensnormal = models.CharField(max_length=150,choices=eyeConditions)
    lensclear = models.CharField(max_length=150,choices=eyeConditions)
    lenscataract = models.CharField(max_length=150,choices=eyeConditions)
    lenspseudophakia = models.CharField(max_length=150,choices=eyeConditions)
    lenslenticonus = models.CharField(max_length=150,choices=eyeConditions)
    lenscoloboma = models.CharField(max_length=150,choices=eyeConditions)
    lensmicrospherophakia = models.CharField(max_length=150,choices=eyeConditions)

    ambylopia = models.CharField(max_length=150,choices=eyeConditions)

    strabismusesotropia =models.CharField(max_length=150,choices=eyeConditions)
    strabismusexotropia =models.CharField(max_length=150,choices=eyeConditions)
    strabismusesophoria =models.CharField(max_length=150,choices=eyeConditions)
    strabismusexophoria =models.CharField(max_length=150,choices=eyeConditions)

    pupillaryreflex =models.CharField(max_length=150,choices=reflex)

    binocularfunction =models.CharField(max_length=150)

    accomodationandvergence = models.CharField(max_length=150, null=True)

    colorvision =models.CharField(max_length=150,choices=colorvisionoptions)

    provisionaldiagnosisnormal =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)

    provisionaldiagnosismyopia =models.CharField(max_length=150,choices=provisionaldiagnosisoptions,default=None)
    provisionaldiagnosismyopiaconditions = models.CharField(max_length=150,choices=provisionaldiagnosismyopiaconditionsoptions,default=None)

    provisionaldiagnosishyperopia =models.CharField(max_length=150,choices=provisionaldiagnosisoptions,default=None)
    provisionaldiagnosishyperopiaconditions=models.CharField(max_length=150,choices=provisionaldiagnosishyperopiaconditionoptions,default=None)

    provisionaldiagnosisastigmatism =models.CharField(max_length=150,choices=provisionaldiagnosisoptions,default=None)
    provisionaldiagnosisastigmatismconditions =models.CharField(max_length=150,choices=provisionaldiagnosisastigmatismconditionsoptions,default=None)

    provisionaldiagnosisambylopia =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)

    provisionaldiagnosisstrabismus =models.CharField(max_length=150,choices=provisionaldiagnosisoptions,default=None)
    provisionaldiagnosisstrabismuscondtions =models.CharField(max_length=150,choices=provisionaldiagnosisstrabismuscondtionsoptions,default=None)


    provisionaldiagnosisnystagmus =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosisptosis =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosisconvergence =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosisinsufficiency =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosisblepharitis =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosismeibomitis =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosiscolorvision =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)
    provisionaldiagnosisblindness =models.CharField(max_length=150,choices=provisionaldiagnosisoptions)

    recommendationslist =models.CharField(max_length=150,choices=recommendationsoptions,default=None)
    recommendationslistothers =models.CharField(max_length=150)


    doctoradviceoptions =models.CharField(max_length=150,choices=adviceoptions,default=None)
    doctorotheradviceoptions =models.CharField(max_length=150)


    occulomotorfunction =models.CharField(max_length=150)

    childuid = models.CharField(max_length=150)


class Pediatrics(models.Model):
    options = {
        ('normal','Normal'),
        ('abnormal','Abnormal')
    }

    generalApperance = models.CharField(max_length=150, choices=options, default='normal')
    generalApperanceRemarks = models.CharField(max_length=300,blank=True)

    scalpandskin = models.CharField(max_length=150, choices=options, default='normal')
    scalpandskinRemarks = models.CharField(max_length=300,blank=True)

    lymphNodes = models.CharField(max_length=150, choices=options, default='normal')
    lymphNodesRemarks = models.CharField(max_length=300,blank=True)

    neck = models.CharField(max_length=150, choices=options, default='normal')
    neckRemarks = models.CharField(max_length=300,blank=True)

    ears = models.CharField(max_length=150, choices=options, default='normal')
    earsRemarks = models.CharField(max_length=300,blank=True)

    nose = models.CharField(max_length=150, choices=options, default='normal')
    noseRemarks = models.CharField(max_length=300,blank=True)

    throatAndOralCavity = models.CharField(max_length=150, choices=options, default='normal')
    throatAndOralCavitytRemarks = models.CharField(max_length=300,blank=True)

    cardioVascularSystem = models.CharField(max_length=150, choices=options, default='normal')
    cardioVascularSystemRemarks = models.CharField(max_length=300,blank=True)

    respiratatorySystem = models.CharField(max_length=150, choices=options, default='normal')
    respiratatorySystemRemarks = models.CharField(max_length=300,blank=True)

    abdomen = models.CharField(max_length=150, choices=options, default='normal')
    abdomenRemarks = models.CharField(max_length=300,blank=True)

    upperAndLowerExtremities = models.CharField(max_length=150, choices=options, default='normal')
    upperAndLowerExtremitiesRemarks = models.CharField(max_length=300,blank=True)

    spineGaitAndPosture = models.CharField(max_length=150, choices=options, default='normal')
    spineGaitAndPostureRemarks = models.CharField(max_length=300,blank=True)

    higherMentalPosture = models.CharField(max_length=150, choices=options, default='normal')
    higherMentalPostureRemarks = models.CharField(max_length=300,blank=True)

    pediatricRecommendations = models.CharField(max_length=300,blank=True)

    childuid =  models.CharField(max_length=245, unique = True,primary_key = True)

    def __str__(self):
        return self.childuid 


class Nutrition(models.Model): 
    childuid =  models.CharField(max_length=245, unique = True,primary_key = True)
    observations =  models.CharField(max_length=500)
    recommendations =  models.CharField(max_length=500)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.childuid


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
    mouthfloorRemarks = models.CharField(max_length=300,blank=True)

    palate = models.CharField(max_length=150, choices=options, default='normal')
    palateRemarks = models.CharField(max_length=300,blank=True)

    lips = models.CharField(max_length=150, choices=options, default='normal')
    lipsRemarks = models.CharField(max_length=300,blank=True)

    cheeks = models.CharField(max_length=150, choices=options, default='normal')
    cheeksRemarks = models.CharField(max_length=300,blank=True)

    tongue = models.CharField(max_length=150, choices=options, default='normal')
    tongueRemarks = models.CharField(max_length=300,blank=True)

    throat = models.CharField(max_length=150, choices=options, default='normal')
    throatRemarks = models.CharField(max_length=300,blank=True)

    frenulam = models.CharField(max_length=150, choices=options, default='normal')
    frenulamRemarks = models.CharField(max_length=300,blank=True)

    ridges = models.CharField(max_length=150, choices=options, default='normal')
    ridgesRemarks = models.CharField(max_length=300,blank=True)

    plaque = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    plaqueRemarks = models.CharField(max_length=300,blank=True)

    stain = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    stainRemarks = models.CharField(max_length=300,blank=True)

    gingivitis = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    gingivitisRemarks = models.CharField(max_length=300,blank=True)

    caries = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    cariesRemarks = models.CharField(max_length=300,blank=True)

    infection = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    infectionRemarks = models.CharField(max_length=300,blank=True)    

    fracturedorcrackedteeth = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    fracturedorcrackedteethRemarks = models.CharField(max_length=300,blank=True)  

    habits = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    habitsRemarks = models.CharField(max_length=300,blank=True)  

    calculus = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    calculusRemarks = models.CharField(max_length=300,blank=True) 

    malocclusion = models.CharField(max_length=150, choices=optionsTwo, default='absent')
    malocclusionRemarks = models.CharField(max_length=300,blank=True) 

    impactedwisdomteeth= models.CharField(max_length=150, choices=optionsTwo, default='absent')
    impactedwisdomteethRemarks = models.CharField(max_length=300,blank=True) 

    provisionalDiagnosisoptions= models.CharField(max_length=150, choices=provisionalDiagnosisOptions,default='NO ABNORMALITY DETECTED')

    abnormalfrenum = models.CharField(max_length=150, choices=abnormalFrenumOptions,blank =True)

    periodontalabnormalities= models.CharField(max_length=150, choices=periodontalAbnormalitiesOptions,blank =True)

    cariestypes= models.CharField(max_length=150, choices=cariesOptions,blank =True)

    fracturedorcrackedteethtypes = models.CharField(max_length=150, choices=fracturedorcrackedteethOptions,blank =True)

    orthodonticmalocculsionabnormalitiestypes = models.CharField(max_length=150, choices=orthodonticmalocculsionabnormalitiesOptions,blank =True)

    orthodonticmalocculsionabnormalitiesotherstypes = MultiSelectField(max_length=150, choices=orthodonticmalocculsionabnormalitiesothersOptions,blank = True)

    habitstypes = models.CharField(max_length=150, choices=habitsOptions, blank = True)
    
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

    heartrate = models.CharField(max_length=245,null = True)

    temparature = models.CharField(max_length=245,null = True)

    saturation = models.CharField(max_length=245,null = True)

    systolic = models.CharField(max_length=245,null = True)

    diastolic = models.CharField(max_length=245,null = True)
 
    respiratoryrate = models.CharField(max_length=245,null = True)

    bmi= models.CharField(max_length=245)
  
    bsa = models.CharField(max_length=245)

    year = models.CharField(max_length=245)

    kiduid =  models.CharField(max_length=245)

    sign =  models.CharField(max_length=245)
    

    def __str__(self):
        return self.kiduid


