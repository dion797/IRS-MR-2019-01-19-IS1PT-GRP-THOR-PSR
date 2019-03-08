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
| IAN TAN ENG KIONG | A0120534W | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |
| KHOO WEE BENG | A0195308Y | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |
| KOH SOOK BING | A0195413E | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |
| RANA BHATTACHARJEE | A0195178N | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |
| TAN YAO TAI TEERAPONG | A0073460L | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |
| YEO WHYE CHUNG NELSON | A0195405A | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz|  |

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Sudoku AI Solver](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Sudoku AI Solver")

Note: It is not mandatory for every project member to appear in video presentation; Presentation by one project member is acceptable. 
More reference video presentations [here](https://telescopeuser.wordpress.com/2018/03/31/master-of-technology-solution-know-how-video-index-2/ "video presentations")

---
## SECTION 5 : USER GUIDE

`<Github File Link>` : <https://github.com/telescopeuser/Workshop-Project-Submission-Template/blob/master/UserGuide/User%20Guide%20HDB-BTO.pdf>

### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/telescopeuser/Workshop-Project-Submission-Template.git

> $ source activate iss-env-py2

> (iss-env-py2) $ cd Workshop-Project-Submission-Template/SystemCode/clips

> (iss-env-py2) $ python app.py

> **Go to URL using web browser** http://0.0.0.0:5000 or http://127.0.0.1:5000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in python 2 only.

> $ sudo apt-get install python-clips clips build-essential libssl-dev libffi-dev python-dev python-pip

> $ pip install pyclips flask flask-socketio eventlet simplejson pandas

---
## SECTION 6 : PROJECT REPORT / PAPER

`<Github File Link>` : <https://github.com/telescopeuser/Workshop-Project-Submission-Template/blob/master/ProjectReport/Project%20Report%20HDB-BTO.pdf>

**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Sponsor Company Introduction (if applicable)
- Business Problem Background
- Project Objectives & Success Measurements
- Project Solution (To detail domain modelling & system design.)
- Project Implementation (To detail system development & testing approach.)
- Project Performance & Validation (To prove project objectives are met.)
- Project Conclusions: Findings & Recommendation
- List of Abbreviations (if applicable)
- References (if applicable)

---
## SECTION 7 : MISCELLANEOUS

### HDB_BTO_SURVEY.xlsx
* Results of survey
* Insights derived, which were subsequently used in our system

---
