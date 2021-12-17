from mycroft import MycroftSkill, intent_handler
import re


class GithubStats(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def tell_stats(self, message):
        pass

    def greet(self, message):
        if re.match(self.translate_regex('is.awake'), message):
            self.speak_dialog('awake.dialog')
        else:
            self.speak_dialog('greet.dialog')

    @intent_handler('stats.github.intent')
    def handle_stats_github(self, message):
        pass
        #self.speak_dialog('stats.github')


def create_skill():
    return GithubStats()

