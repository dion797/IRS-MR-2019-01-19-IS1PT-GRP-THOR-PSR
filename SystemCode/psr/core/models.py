from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    cuisine = models.CharField(max_length=50)
    isVegetarian = models.CharField(max_length=50)
    hasSoup = models.CharField(max_length=50)
    spicyLevel = models.CharField(max_length=50)
    sourLevel = models.CharField(max_length=50)
    sweetLevel = models.CharField(max_length=50)
    saltyLevel = models.CharField(max_length=50)
    fatLevel = models.CharField(max_length=50)
    calorieLevel = models.CharField(max_length=50)
    fiberLevel = models.CharField(max_length=50)
    carbLevel = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'cuisine: ' + self.cuisine + '\n' +\
            'isVegetarian: ' + self.isVegetarian + '\n' +\
            'hasSoup: ' + self.hasSoup + '\n' +\
            'spicyLevel: ' + self.spicyLevel + '\n' +\
            'sourLevel: ' + self.sourLevel + '\n' +\
            'sweetLevel: ' + self.sweetLevel + '\n' +\
            'saltyLevel: ' + self.saltyLevel + '\n' +\
            'fatLevel: ' + self.fatLevel + '\n' +\
            'calorieLevel: ' + self.calorieLevel + '\n' +\
            'carbLevel: ' + self.carbLevel + '\n' +\
            'fiberLevel: ' + self.fiberLevel + '\n'


class Review(models.Model):
    dishName = models.CharField(max_length=50)
    dishId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'dish-name: ' + self.dishName + '\n' +\
            'dish-id: ' + str(self.dishId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Suggestion(models.Model):
    dishName = models.CharField(max_length=50)
    dishId = models.IntegerField()
    attribute = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'dish-name: ' + self.dishName + '\n' +\
            'dish-id: ' + str(self.dishId) + '\n' +\
            'attribute: ' + self.attribute + '\n' +\
            'value: ' + self.value + '\n' +\
            'quantity: ' + str(self.quantity) + '\n'


class PSRProfile(models.Model):
    houseType = models.CharField(max_length=15)
    income = models.CharField(max_length=15)
    residence = models.CharField(max_length=15)
    risk = models.CharField(max_length=15)
    bill = models.CharField(max_length=15)
    sd = models.CharField(max_length=15)
    incentive = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    otherConsider = models.CharField(max_length=1000)
    createdTime = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'housetype: ' + str(self.houseType) + '\n' +\
            'income: ' + str(self.income) + '\n' +\
            'residence: ' + str(self.residence) + '\n' +\
            'risk: ' + str(self.risk) + '\n' +\
            'bill: ' + str(self.bill) + '\n' +\
            'sd: ' + str(self.sd) + '\n' +\
            'incentive: ' + str(self.incentive) + '\n' +\
            'brand: ' + str(self.brand) + '\n' +\
            'otherconsider: ' + str(self.otherConsider) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class OEMR(models.Model):
    name = models.TextField()
    plan = models.TextField()
    priceCentsKwh = models.TextField()
    incentives = models.TextField()
    contract = models.TextField()
    autoRenewal = models.TextField()
    smartMeterReq = models.TextField()
    separateBill = models.TextField()
    OTRegFee = models.TextField()
    lateCharge = models.TextField()
    earlyTerm = models.TextField()
    securityDeposit = models.TextField()
    others = models.TextField()

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + str(self.name) + '\n' +\
            'plan: ' + str(self.plan) + '\n' +\
            'priceCentsKwh: ' + str(self.priceCentsKwh) + '\n' +\
            'incentives: ' + str(self.incentives) + '\n' +\
            'contract: ' + str(self.contract) + '\n' +\
            'autoRenewal: ' + str(self.autoRenewal) + '\n' +\
            'smartMeterReq: ' + str(self.smartMeterReq) + '\n' + \
            'separateBill: ' + str(self.separateBill) + '\n' + \
            'OTRegFee: ' + str(self.OTRegFee) + '\n' +\
            'lateCharge: ' + str(self.lateCharge) + '\n' + \
            'earlyTerm: ' + str(self.earlyTerm) + '\n' + \
            'securityDeposit: ' + str(self.securityDeposit) + '\n' + \
            'others: ' + str(self.others) + '\n'
