import requests
from bs4 import BeautifulSoup
import json
import re

boy_url = "https://www.verywellfamily.com/top-1000-baby-boy-names-2757618"
boy_response = requests.get(boy_url)

girl_url = "https://www.verywellfamily.com/top-1000-baby-girl-names-2757832"
girl_response = requests.get(girl_url)

boy_soup = BeautifulSoup(boy_response.content, 'html.parser')
boy_namelist = boy_soup.find("ol")

girl_soup = BeautifulSoup(girl_response.content, 'html.parser')
girl_namelist = girl_soup.find("ol")

#initialize dictionary to become json file
baby_names_dict = {}
baby_names_dict['BOY'] = {}
baby_names_dict['GIRL'] = {}
ascii = 65 #Starts scraping for "A" names ends after "Z" names

while ascii < 91:
    boy_names_for_letter = []
    for item in boy_namelist:
        name = item.get_text()
        if re.match("^[A-Za-z]", name) and name[0] == chr(ascii):
            boy_names_for_letter.append(name)    
    
    girl_names_for_letter = []
    for item in girl_namelist:
        name = item.get_text()
        if re.match("^[A-Za-z]", name) and name[0] == chr(ascii):
            girl_names_for_letter.append(name) 

    baby_names_dict['BOY'][chr(ascii)] = boy_names_for_letter
    baby_names_dict['GIRL'][chr(ascii)] = girl_names_for_letter

    ascii +=1

with open('babynames.json', 'w') as file:
    json.dump(baby_names_dict, file)