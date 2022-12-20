from mycroft import MycroftSkill, intent_file_handler


class ErrorReporter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reporter.error.intent')
    def handle_reporter_error(self, message):
        skill = message.data.get('skill')

        self.speak_dialog('reporter.error', data={
            'skill': skill
        })


def create_skill():
    return ErrorReporter()

