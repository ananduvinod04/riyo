from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionAboutRiyo(Action):
    def name(self):
        return "action_about_riyo"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text=(
                "I’m Riyo 🤖 — your AI assistant inside ECHO.\n"
                "I help you understand features, guide you through the app, "
                "and make your experience smoother.\n"
                "Riyo means a friendly digital companion 🌱"
            )
        )
        return []

class ActionCurrentDateTime(Action):
    def name(self):
        return "action_current_datetime"

    def run(self, dispatcher, tracker, domain):
        now = datetime.now()
        dispatcher.utter_message(
            text=f"📅 Today is {now.strftime('%A, %d %B %Y')} ⏰ Time: {now.strftime('%I:%M %p')}"
        )
        return []
