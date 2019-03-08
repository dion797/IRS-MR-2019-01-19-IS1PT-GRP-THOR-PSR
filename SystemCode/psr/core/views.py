from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from core.models import Dish, Review, Suggestion, PSRProfile, OEMR
from PIL import Image, ImageOps
import datetime
import os.path
import clips
import ast
import time
from django.views.decorators.csrf import csrf_exempt

# ------------------------------------------------------------------------------
# Create your views here.

def index(request):
    return render(request, 'index.html')


def choose(request):
    return render(request, 'choose.html')


def index_old(request):
    return render(request, 'index_old.html')


def preferencePage(request):
    return render(request, 'preferences.html')


def newDishPage(request):
    return render(request, 'new.html')


def aboutUsPage(request):
    return render(request, 'about.html')


# A new preferences. Assume Data is CORRECT!
@csrf_exempt
def newChoice(request):
    id = insertPSRProfiletoDatabase(request.POST)
    print('in newChoice() \n')
    result2 = clipsChooseOEMR(request.POST)
    response = []
    top1 = 0
    weight1 = 0
    top2 = 0
    weight2 = 0
    top3 = 0
    weight3 = 0
    if result2 != None:
        print('have results \n')
        for val in result2.split('---'):
            if "," in val:
                val2 = val.split(',')
                print('ID:'+str(val2[0])+", weightage:"+str(val2[3])+"\n")
                tempid = int(val2[0])
                tempweight = float(val2[3])
                if top1 == 0:
                    top1 = tempid
                    weight1 = tempweight
                else:
                    if weight1 < tempweight:
                        # push down all the rankings
                        top3 = top2
                        weight3 = weight2
                        top2 = top1
                        weight2 = weight1
                        top1 = tempid
                        weight1 = tempweight
                    else:
                        if weight2 < tempweight and weight1 > tempweight:
                            # push down rank2 to rank 3
                            top3 = top2
                            weight3 = weight2
                            top2 = tempid
                            weight2 = tempweight
                        else:
                            if weight3 < tempweight and weight2 > tempweight:
                                # replace top3
                                top3 = tempid
                                weight3 = tempweight
        oemr = OEMR.objects.get(id=top1)
        #oemr = OEMR.objects.get(id=int(val2[0]))
        response.append({"id": oemr.id, "name": oemr.name, "plan": oemr.plan,
                         "priceCentsKwh": oemr.priceCentsKwh, "incentives": oemr.incentives,
                         "contract": oemr.contract, "autoRenewal": oemr.autoRenewal, "separateBill": oemr.separateBill,
                         "smartMeterReq": oemr.smartMeterReq, "OTRegFee": oemr.OTRegFee,
                         "lateCharge": oemr.lateCharge, "earlyTerm": oemr.earlyTerm,
                         "securityDeposit": oemr.securityDeposit, "others": oemr.others})
        oemr = OEMR.objects.get(id=top2)
        # oemr = OEMR.objects.get(id=int(val2[0]))
        response.append({"id": oemr.id, "name": oemr.name, "plan": oemr.plan,
                         "priceCentsKwh": oemr.priceCentsKwh, "incentives": oemr.incentives,
                         "contract": oemr.contract, "autoRenewal": oemr.autoRenewal, "separateBill": oemr.separateBill,
                         "smartMeterReq": oemr.smartMeterReq, "OTRegFee": oemr.OTRegFee,
                         "lateCharge": oemr.lateCharge, "earlyTerm": oemr.earlyTerm,
                         "securityDeposit": oemr.securityDeposit, "others": oemr.others})
        oemr = OEMR.objects.get(id=top3)
        # oemr = OEMR.objects.get(id=int(val2[0]))
        response.append({"id": oemr.id, "name": oemr.name, "plan": oemr.plan,
                         "priceCentsKwh": oemr.priceCentsKwh, "incentives": oemr.incentives,
                         "contract": oemr.contract, "autoRenewal": oemr.autoRenewal, "separateBill": oemr.separateBill,
                         "smartMeterReq": oemr.smartMeterReq, "OTRegFee": oemr.OTRegFee,
                         "lateCharge": oemr.lateCharge, "earlyTerm": oemr.earlyTerm,
                         "securityDeposit": oemr.securityDeposit, "others": oemr.others})






    # response.append({"id": "3",
    #                  "name": "ES Power (by Environmental Solutions (Asia) Pte Ltd)",
    #                  "plan": "Chope the Rate (3 Months)",
    #                  "priceCentsKwh": "17.66",
    #                  "incentives": "1) Free 1 Air-con Servicing \n 2) Free AIA Personal " +
    #                                "Accident Protection \n 3) Get 1% cash rebate on POSB Everyday Card \n 4) Get up to 5% Cash " +
    #                                "back rebate on UOB ONE Credit Card \n 5) Green Certified Electricity at no additional cost " +
    #                                "\n 6) Carbon Tax absorbed",
    #                  "contract": "12",
    #                  "autoRenewal": "Renewed contract term will " +
    #                                 "remain as the same current contract duration. Renewed electricity rate will be lower than " +
    #                                 "prevailing regulated tariff at renewal. All other applicable charges/fees will be the same" +
    #                                 " or better.",
    #                  "smartMeterReq": "No",
    #                  "OTRegFee": "No",
    #                  "lateCharge": "1% of the outstanding amount per month",
    #                  "earlyTerm": "1) $100 if terminated within 3 Cal days from sign-up. \n2) 30 % X Months left in" +
    #                               " contract X Average of latest 2 months bill if terminated after 3 Cal days from signup or " +
    #                               "during contract period. \n3) ETC is waived for re-location or expatriation.",
    #                  "securityDeposit": "1) HDB 1-Room / 2-Room / 3-Room: $30 \n2) HDB 4 - Room / 5 - Room / Exec /" +
    #                                     " HUDC: $60 \n3) Condominiums / Landed: $90",
    #                  "others": "Hardcopy Billing: $1.00 per Bill (Exc. GST); $1.07 per Bill (Inc GST)"
    #                  })

    return JsonResponse(response, safe=False)


def insertPSRProfiletoDatabase(data):
    psrProfile = PSRProfile(houseType=data['housetype'],
                income=data['income'],
                residence=data['residence'],
                risk=data['risk'],
                bill=data['bill'],
                sd=data['sd'],
                incentive=data['incentive'],
                brand=data['brand'],
                otherConsider=data['otherconsider'],
                createdTime=datetime.datetime.now())
    print(psrProfile)
    psrProfile.save()
    return psrProfile.id


# New Review, Assume Data is CORRECT
@csrf_exempt
def processReviews(request):
    if request.method == "POST":
        id = insertReviewIntoDatabase(request.POST)
        insertReviewIntoClips(request.POST, id)
        return HttpResponse('')
    else:
        response = []
        reviews = Review.objects.filter(dishId=int(request.GET['dishId'])).order_by("-id")
        for review in reviews:
            response.append({"id": review.id, "comment": review.comment, "reviewer": review.reviewer,
                    "createdTime": review.createdTime})
        return JsonResponse(response, safe=False)


# Create New Dish, Assume Data is CORRECT!
@csrf_exempt
def createDish(request):
    id = insertNewDish(request.POST)
    insertIntoClips(id, request.POST)
    return HttpResponse('')


# A new preferences. Assume Data is CORRECT!
@csrf_exempt
def newPreference(request):
    result = clipsMatchPreference(request.POST)
    print(result)
    response = []
    if result != None:
        for val in result.split('---'):
            if "," in val:
                val2 = val.split(',')
                dish = Dish.objects.get(id=int(val2[0]))
                response.append({"id": dish.id, "name": dish.name, "images": dish.images, "description": dish.description,
                    "cuisine": val2[1], "vegetarian": val2[2], "hasSoup": val2[3],
                    "calorieLevel": val2[4], "fiberLevel": val2[5], "fatLevel": val2[6], "carbLevel": val2[7],
                    "spicyLevel": val2[8], "saltyLevel": val2[9], "sourLevel": val2[10], "sweetLevel": val2[11],
                    "stars": float(val2[12])})
    return JsonResponse(response, safe=False)


# A new preferences. Assume Data is CORRECT!
@csrf_exempt
def modify(request):
    insertSuggestionIntoDatabase(request.POST)
    insertSuggestionsIntoClips()
    return HttpResponse('')


# ------------------------------------------------------------------------------
# Utility Functions
def insertNewDish(data):
    images = ast.literal_eval(data['images'])
    imageNum = 0;
    for image in images:
        imageNum = imageNum + (image != 'null')

    dish = Dish(name=data['name'],
                description=data['description'],
                images=imageNum,
                cuisine=data['cuisine'],
                isVegetarian=data['isVegetarian'],
                hasSoup=data['hasSoup'],
                spicyLevel=data['spicyLevel'],
                sweetLevel=data['sweetLevel'],
                sourLevel=data['sourLevel'],
                saltyLevel=data['saltyLevel'],
                fatLevel=data['fatLevel'],
                calorieLevel=data['calorieLevel'],
                fiberLevel=data['fiberLevel'],
                carbLevel=data['carbLevel'])
    dish.save()

    index = 0
    for image in images:
        if image != 'null':
            index = index + 1
            createImage(dish.id, index, image)

    return dish.id


def createImage(id, index, image):
    imgCore = image.split(',')[1]
    imgFile = open(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg", "wb")
    imgFile.write(imgCore.decode('base64'))
    imgFile.close()

    # Create square image
    img = Image.open(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg")
    longer_side = max(img.size)
    thumb = Image.new('RGBA', (longer_side, longer_side), (255, 255, 255, 0))
    thumb.paste(
        img, ((longer_side - img.size[0]) / 2, (longer_side - img.size[1]) / 2)
    )
    thumb.save(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + "_square.jpeg")


def insertIntoClips(id, data):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/dishes.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts dishes)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (dish '
                '(ID '+str(id)+')'
                '(name "'+data['name']+'") '
                '(cuisine "'+data['cuisine']+'") '
                '(is-vegetarian "'+data['isVegetarian']+'") '
                '(has-soup "'+data['hasSoup']+'") '
                '(fat-level "'+data['fatLevel']+'")'
                '(calorie-level "'+data['calorieLevel']+'") '
                '(fiber-level "'+data['fiberLevel']+'") '
                '(carb-level "'+data['carbLevel']+'") '
                '(spicy-level "'+data['spicyLevel']+'") '
                '(sour-level "'+data['sourLevel']+'") '
                '(sweet-level "'+data['sweetLevel']+'") '
                '(salty-level "'+data['saltyLevel']+'") '
                '(stars -1)))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


attributeMap = { 'isVegetarian': 'is-vegetarian',
        'hasSoup': 'has-soup',
        'spicyLevel': 'spicy-level',
        'sourLevel': 'sour-level',
        'saltyLevel': 'salty-level',
        'sweetLevel': 'sweet-level',
        'fatLevel': 'fat-level',
        'calorieLevel': 'calorie-level',
        'carbLevel': 'carb-level',
        'fiberLevel': 'fiber-level'};
def insertSuggestionIntoDatabase(data):
    suggestion = Suggestion(
                dishName=data['dishName'],
                dishId=int(data['dishId']),
                attribute=attributeMap[data['key']],
                value=data['value'],
                quantity=0)

    suggestions = Suggestion.objects.filter(dishId=int(data['dishId']), attribute=attributeMap[data['key']], value=data['value'])
    if (len(suggestions) != 0):
        suggestion = suggestions[0]

    suggestion.quantity = suggestion.quantity + 1
    suggestion.save()
    print(suggestion)


def insertSuggestionsIntoClips():
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/suggestions.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts suggestions)\n")
        file.close()

    # modify facts
    suggestions = Suggestion.objects.all()
    lines = ['(deffacts suggestions\n']
    for suggestion in suggestions:
        lines.append('  (suggestion '
                     '(dish-name "'+suggestion.dishName+'")'
                     '(dish-id '+str(suggestion.dishId)+')'
                     '(attribute "'+suggestion.attribute+'")'
                     '(value "'+suggestion.value+'")'
                     '(quantity '+str(suggestion.quantity)+'))\n')

    lines.append(')\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


def insertReviewIntoDatabase(data):
    review = Review(reviewer=data['reviewer'],
                comment=data['comment'],
                stars=float(data['stars']),
                dishName=data['dishName'],
                dishId=int(data['dishId']),
                createdTime=datetime.datetime.now())
    print(review)
    review.save()
    return review.id


def insertReviewIntoClips(data, id):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/reviews.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts reviews)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (review '
                '(ID '+str(id)+')'
                '(dish-name "'+data['dishName']+'")'
                '(dish-id '+data['dishId']+')'
                '(reviewer "'+data['reviewer']+'")'
                '(comment "'+data['comment']+'")'
                '(stars '+data['stars']+')))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


def clipsMatchPreference(data):
    # Preference
    preference = '(preference ' +\
                 '(cuisine "'+data['cuisine']+'") ' +\
                 '(is-vegetarian "'+data['isVegetarian']+'") ' +\
                 '(has-soup "'+data['hasSoup']+'") ' +\
                 '(fat-level "'+data['fatLevel']+'")' +\
                 '(calorie-level "'+data['calorieLevel']+'") ' +\
                 '(fiber-level "'+data['fiberLevel']+'") ' +\
                 '(carb-level "'+data['carbLevel']+'") ' +\
                 '(spicy-level "'+data['spicyLevel']+'") ' +\
                 '(sour-level "'+data['sourLevel']+'") ' +\
                 '(sweet-level "'+data['sweetLevel']+'") ' +\
                 '(salty-level "'+data['saltyLevel']+'"))'

    # CLIPS
    print(preference)
    clips.Clear()
    clips.BatchStar(settings.CLIPS_DIR + "/templates.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/dishes.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/dishes.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/reviews.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/reviews.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/suggestions.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/suggestions.clp")
    clips.BatchStar(settings.CLIPS_DIR + "/rules.clp")
    clips.Reset()
    clips.Assert(preference)
    clips.Run()
    return clips.StdoutStream.Read()


def clipsChooseOEMR(data):
    # Preference
    psrprofile = '(form-input ' +\
                 '(aptType '+data['housetype']+') ' +\
                 '(income '+data['income']+') ' +\
                 '(tenancy-type '+data['residence']+') ' +\
                 '(is-risk-averse '+data['risk']+') ' +\
                 '(accept-direct-billing '+data['bill']+') ' +\
                 '(accept-sec-dep '+data['sd']+') ' +\
                 '(want-incentives '+data['incentive']+') ' +\
                 '(prefer-est-brand '+data['brand']+'))'
    # CLIPS
    clips.Clear()
    clips.Load(settings.CLIPS_DIR + "/psr_templates.clp")
    clips.Load(settings.CLIPS_DIR + "/psr_init_facts.clp")
    clips.Load(settings.CLIPS_DIR + "/psr_plans.CLP")
    clips.Load(settings.CLIPS_DIR + "/psr_rules.CLP")
    clips.Reset()
    clips.Assert(psrprofile)
    clips.Run()
    return clips.StdoutStream.Read()
