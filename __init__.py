from mycroft import MycroftSkill, intent_handler
import re
from datetime import datetime


class GithubStats(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def tell_stats(self, message):
        pass

    def get_time(self):
        t = datetime.now().hour
        if t > 5 and t <= 12:
            return "morning"
        elif t > 12 and t <= 17:
            return "day"
        elif t > 17 and t <= 23:
            return "evening"
        else:
            return "night"

    def greet(self, message):
        if re.match(self.translate_regex('is.awake'), message):
            self.speak_dialog('awake.dialog')
        else:
            self.speak_dialog('greet.dialog', data={'time': self.get_time()})

    @intent_handler('stats.github.intent')
    def handle_stats_github(self, message):
        pass
        #self.speak_dialog('stats.github')


def create_skill():
    return GithubStats()

