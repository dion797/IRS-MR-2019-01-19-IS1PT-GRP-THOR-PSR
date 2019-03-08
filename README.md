IRS-MR-2019-01-19-IS1PT-GRP-THOR-PSR
---

## SECTION 1 : PROJECT TITLE
Power Supplier Recommender

---
## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
Since 1 November 2018, the Open Electricity Market had been extended to all consumers across Singapore by zones. This initiative provided about 1.4 million households and business accounts with more choice and flexibility when buying electricity, while being provided with the same electricity supply through the national power grid. 

This decision making task may seem confusing due to overwhelming number of different supplier and pricing plans. While a current model exists in the open market website, it is a supplier centric based on filtering technique to rank the different price plans according to the decision maker preferences. This requires the decision maker to understand the differences between the supplier price plans in terms of pricing, green energy etc.   Our team, comprising of 6 Singaporeans from different age group and background hope to improve the model by making it more consumer centric where the model works on individual profile and preferences to arrive  on the final recommendation. Leveraging on the diversity of the team, we redefined the rules according to individual preferences which did not exists in the current model to help us build the power supplier recommender model. 

Using the techniques imparted to us in lectures, our group first set out to build a sizeable knowledge base via conducting an interview and administering a survey. While building the system, we downloaded the pricing information from the different power suppliers and transform it into a database, CLIPS to synthesize the rule based reasoning process, and Python to integrate it into an easy to use UI for the everyday user. 

Our team had an exciting time working on this project, and hope to share our insights with everyone. There are truly are a wide array of individual factors to come to a final decision in the switch to a different pricing plan, and we only wish there was more time to work on the scope and scale of the project.   

---
## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| IAN TAN ENG KIONG | A0120534W | SurveyAnalysis ProjectReport ApplicationTesting|  |
| KHOO WEE BENG | A0195308Y | Development Integration|  |
| KOH SOOK BING | A0195413E | ProjectReport UserGuide|  |
| RANA BHATTACHARJEE | A0195178N | SurveyAnalysis CLIPS VideoDemo|  |
| TAN YAO TAI TEERAPONG | A0073460L | SurveyAnalysis ProjectReport|  |
| YEO WHYE CHUNG NELSON | A0195405A | ProjectReport CLIPS|  |

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Power Supplier Recommender]](https://youtu.be/9vngsi4aftA "Power Supplier Recommender")

---
## SECTION 5 : USER GUIDE

`<Github File Link>` : <https://github.com/telescopeuser/Workshop-Project-Submission-Template/blob/master/UserGuide/User%20Guide%20HDB-BTO.pdf>

### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/dion797/IRS-MR-2019-01-19-IS1PT-GRP-THOR-PSR.git

> $ sudo apt-get install python-django

> $ cd IRS-MR-2019-01-19-IS1PT-GRP-THOR-PSR/SystemCode/psr

> $ python2 manage.py runserver

> **Go to URL using web browser** http://localhost:8000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in python 2 only.

> $ sudo apt-get install python-clips clips build-essential python-dev python-pip python-django

> $ pip install pyclips 

---
## SECTION 6 : PROJECT REPORT / PAPER

Power_Supplier_Recommender.pdf
`<Github File Link>` : <https://github.com/dion797/IRS-MR-2019-01-19-IS1PT-GRP-THOR-PSR/blob/master/ProjectReport/Power_Supplier_Recommender.pdf>

---
## SECTION 7 : MISCELLANEOUS

Power Supplier Recommender.xlsx
`<Github File Link>` : <https://github.com/dion797/IRS-MR-2019-01-19-IS1PT-GRP-THOR-PSR/blob/master/Miscellaneous/Power%20Supplier%20Recommender.xlsx>

---
