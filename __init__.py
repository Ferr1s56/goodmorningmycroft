# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import datetime
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import time





class GoodMorningSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

  
    @intent_handler('goodmorning.intent')
    def handle_good_morning_intent(self, message):
        current_time = datetime.datetime.now() 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        data = requests.get(
            url = 'https://api.hypixel.net/resources/skyblock/election'
        ).json()
        mayor = (data['mayor']['name'])
        res = requests.get(f'https://www.google.com/search?q=Lansdale+weather&oq=Lansdale+weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')   
        info = soup.select('#wob_dc')[0].getText().strip() 
        weather = soup.select('#wob_tm')[0].getText().strip()

        if (str(current_time.month) == '3'):
            month = 'March'
        elif (str(current_time.month) == '1'):
            month = 'January'
        elif (str(current_time.month) == '2'):
            month = 'February'
        elif (str(current_time.month) == '4'):
            month = 'April'
        elif (str(current_time.month) == '5'):
            month = 'May'
        elif (str(current_time.month) == '6'):
            month = 'June'
        elif (str(current_time.month) == '7'):
            month = 'July'
        elif (str(current_time.month) == '8'):
            month = 'August'
        elif (str(current_time.month) == '9'):
            month = 'September'
        elif (str(current_time.month) == '10'):
            month = 'October'
        elif (str(current_time.month) == '11'):
            month = 'November'
        elif (str(current_time.month) == '12'):
            month = 'December'

        self.speak('Good morning Ethan. Todays date is '+month+' '+str(current_time.day)+', '+str(current_time.year)+'. The weather outside is currently '+weather+' degrees and '+info+'.')

    def stop(self):
        pass


def create_skill():
    return GoodMorningSkill()
