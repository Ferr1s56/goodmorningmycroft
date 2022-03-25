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
import random




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
        month = current_time.month
        numbertomonth = {
            '1': ['january'],
            '2': ['february'],
            '3': ['march'],
            '4': ['april'],
            '5': ['may'],
            '6': ['june'],
            '7': ['july'],
            '8': ['august'],
            '9': ['september'],
            '10': ['october'],
            '11': ['november'],
            '12': ['december'],
        }
        numbertodate = {
            '1': ['first'],
            '2': ['second'],
            '3': ['third'],
            '4': ['fourth'],
            '5': ['fifth'],
            '6': ['sixth'],
            '7': ['seventh'],
            '8': ['eighth'],
            '9': ['ninth'],
            '10': ['tenth'],
            '11': ['eleventh'],
            '12': ['twelfth'],
            '13': ['thirteenth'],
            '14': ['fourteenth'],
            '15': ['fifteenth'],
            '16': ['sixteenth'],
            '17': ['seventeenth'],
            '18': ['eighteenth'],
            '19': ['nineteenth'],
            '20': ['twentieth'],
            '21': ['twenty first'],
            '22': ['twenty second'],
            '23': ['twenty third'],
            '24': ['twenty fourth'],
            '25': ['twenty fifth'],
            '26': ['twenty sixth'],
            '27': ['twenty seventh'],
            '28': ['twenty eighth'],
            '29': ['twenty ninth'],
            '30': ['thirtieth'],
            '31': ['thirty first'],
        }
        numbertoweek = {
            '0': ['monday'],
            '1': ['tuesday'],
            '2': ['wednesday'],
            '3': ['thursday'],
            '4': ['friday'],
            '5': ['saturday'],
            '6': ['sunday'],
        }

        try:
            month = random.choice(numbertomonth[str(month)])
            day = random.choice(numbertodate[str(current_time.day)])
            weekday = random.choice(numbertoweek[str(datetime.datetime.now().weekday())])
        except:
            month = 'undefined'
            day = 'undefined'
            weekday = 'undefined'
        
        self.speak('Good morning Ethan, Todays date is '+weekday+', '+month+' '+day+', '+str(current_time.year)+'. The weather outside is currently '+weather+' degrees and '+info+'.')

    def stop(self):
        pass


def create_skill():
    return GoodMorningSkill()
