#importing required modules 
import requests
from bs4 import BeautifulSoup
import json
import os
import datetime
import itertools
from requests import ConnectionError


#scraping india covid data 
URL_india = "https://www.mygov.in/covid-19/"
r_india = requests.get(URL_india)
htmlContent_india = r_india.content
soup_india = BeautifulSoup(htmlContent_india,'html.parser')

#scraping covid news
URL_news = "https://www.google.com/search?q=covid+news+world&sxsrf=ALeKk00b35wAS9ijIarr1VQGONbceXOxjQ:1623640431140&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjJ94_5k5bxAhVTILcAHf29CZ8Q_AUoAXoECAEQAw&biw=1280&bih=591&dpr=1.5"
r_news = requests.get(URL_news)
htmlContent_news = r_news.content
soup_news = BeautifulSoup(htmlContent_news,'html.parser')

#scraping covid symptoms 
URL_symptoms = 'https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html'
r_symptoms = requests.get(URL_symptoms)
htmlContent_symptoms = r_symptoms.content
soup_symptoms = BeautifulSoup(htmlContent_symptoms,'html.parser')

#scraping covid intro
URL_intro = 'https://openwho.org/courses/introduction-to-ncov'
r_intro = requests.get(URL_intro)
htmlContent_intro = r_intro.content
soup_intro = BeautifulSoup(htmlContent_intro,'html.parser')

#covid intro fuction
def covid_intro():
	intro_covid_raw = soup_intro.find('div',class_='col-md-12 course-description mt20')
	for item in intro_covid_raw.find_all('p'):
		print('* '+item.text)


#covid symptoms function
def covid_symptoms():
	symptoms_covid_raw = soup_symptoms.find('div',class_ ='mt-0')
	symptoms_covid = symptoms_covid_raw.find('ul')
	return symptoms_covid.text

#covid news function 
def covid_news():
	for item in soup_news.find_all('h3',class_ = 'zBAuLc'):
		print(item.text)

#india total count function
def india_total_cases():
	total_cases_india_raw = soup_india.find('div',class_ = 'iblock t_case')
	total_cases_india = total_cases_india_raw.find('span','icount')
	return total_cases_india.text

def india_active_cases():
	active_cases_india_raw = soup_india.find('div',class_ = 'block-active-cases')
	active_cases_india = active_cases_india_raw.find('span',class_='icount')
	return active_cases_india.text

def india_recovered_cases():
	recovered_cases_india_raw = soup_india.find('div',class_ = 'iblock discharge')
	recovered_cases_india = recovered_cases_india_raw.find('span',class_ = 'icount')
	return recovered_cases_india.text

def india_death_cases():
	death_india_cases_raw = soup_india.find('div','iblock death_case')
	death_india_cases = death_india_cases_raw.find('span', 'icount')
	return death_india_cases.text

def india_death_previos_day():
	death_india_previos_raw = soup_india.find('div','iblock death_case')
	death_india_previos = death_india_previos_raw.find('div', 'color-red up-arrow')
	return death_india_previos.text.strip()

def india_test_previos_day():
	test_count_india = soup_india.find('strong',class_ = 'testing_count')
	return test_count_india.text

def india_positive_previos_day():
	positive_india_pervios = soup_india.find('div',class_ = 'color-red up-arrow')
	return positive_india_pervios.text.strip()

def india_vaccination_count():
	vaccination_india_raw = soup_india.find('div',class_ = 'total-vcount')
	vaccination_india = vaccination_india_raw.find('strong')
	return vaccination_india.text

def covid_precautions():
	print('1.Clean your hands often. Use soap and water, or an alcohol-based hand rub\n2.Maintain a safe distance from anyone who is coughing or sneezing')
	print('3.Wear a mask when physical distancing is not possible\n4.Don’t touch your eyes, nose or mouth')
	print('5.Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze')
	print('6.Stay home if you feel unwell\n7.if you have a fever, cough and difficulty breathing, seek medical attention.')
def vaccination_effects():
	print('1.a fever\n2.fatigue\n3.headaches\n4.body aches\n5.chills\n6.nausea')


#world code starts here 

#scraping world deaths cases 
URL_world_deaths = 'https://www.indexmundi.com/coronavirus/'
r_world_deaths = requests.get(URL_world_deaths)
htmlContent_world_deaths = r_world_deaths.content
soup_world_deaths = BeautifulSoup(htmlContent_world_deaths,'html.parser')


#scraping world data
URL_world = 'https://www.worldometers.info/coronavirus/'
r_world = requests.get(URL_world)
htmlContent_world = r_world.content
soup_world = BeautifulSoup(htmlContent_world,'html.parser')

#scraping world vaccination data
URL_world_vacination = 'https://www.pharmaceutical-technology.com/covid-19-vaccination-tracker/'
r_world_vaccination = requests.get(URL_world_vacination)
htmlContent_world_vaccination = r_world_vaccination.content
soup_world_vaccination = BeautifulSoup(htmlContent_world_vaccination,'html.parser')

#world death count
def world_death_cases():
	death_case_world_raw = soup_world_deaths.find('div',class_='jumbotron')
	death_case_world = death_case_world_raw.find('h2',class_= 'display-4')
	return death_case_world.text


#world vacination 
def world_vaccination_count():
	vacination_count_world = soup_world_vaccination.find('p',class_='c-post-single__standfirst c-post-content__stats u-mb-1')
	return vacination_count_world.text

#world vacinaton pervios day
def world_vaccination_previos_day():
	vacination_count_world_previos_day = soup_world_vaccination.find('span',class_='c-post-content__small-stat-up u-mb-2')
	return vacination_count_world_previos_day.text
#world total cases

def world_total_cases():
	total_cases_world_raw = soup_world.find('div','maincounter-number')
	total_cases_world = total_cases_world_raw.find('span')
	return total_cases_world.text

#world active cases
def world_active_cases():
	active_cases_world_raw = soup_world.find('div',class_ = 'col-md-6')
	active_cases_world = active_cases_world_raw.find('div','number-table-main')
	return active_cases_world.text
# world code ends here




# search by state code starts here 
_url = 'https://www.mohfw.gov.in/data/datanew.json'
# path to current file
path = os.path.dirname(os.path.realpath(__file__))


def state_data(state=None) -> dict:
    try:
        req = requests.get(_url).json()
        update_json(req)
        return is_offline(state)
    except ConnectionError:
        return is_offline(state, offline=True)


def update_json(req):
    _timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    _update = dict()
    _total = {
        'Total': 0,
        'Active': 0,
        'Cured': 0,
        'Death': 0
    }

    for i in req:
        state, act, cur, dth, tot = i['state_name'], i['new_active'], \
                                    i['new_cured'], i['new_death'], \
                                    (i['new_active'] + i['new_cured'] +
                                     i['new_death'])

        _update.update({
            state: {
                "Total": int(tot),
                "Active": int(act),
                "Cured": int(cur),
                "Death": int(dth)
            }
        })

        _total['Total'] += _update[state]['Total']
        _total['Active'] += _update[state]['Active']
        _total['Cured'] += _update[state]['Cured']
        _total['Death'] += _update[state]['Death']
    _total['Total'] = _total['Total']//2
    _total['Active'] = _total['Active']//2
    _total['Cured'] = _total['Cured']//2
    _total['Death'] = _total['Death']//2
    _update.update({
        'Total': _total
    })

    _update.update({
        "lastupdated": _timestamp
    })

    with open(os.path.join(path, 'stats.json'), 'w') as f:
        json.dump(_update, f)


def is_offline(state, offline=False):
    with open(os.path.join(path, 'stats.json'), 'r') as f:
        _json = json.load(f)

    if not state:
        val = dict(itertools.islice(_json.items(), len(_json)-2))
    else:
        try:
            val = _json[state]
        except KeyError:
            val = {}
    if offline:
        val.update({
            "lastupdated": _json['lastupdated']
        })

    return val

#serch by state code ends here
