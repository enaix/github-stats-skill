from mycroft import MycroftSkill, intent_handler


class GithubStats(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('stats.github.intent')
    def handle_stats_github(self, message):
        self.speak_dialog('stats.github')


def create_skill():
    return GithubStats()

