from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .external_knowledge import external_search

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


class ActionExternalKnowledge(Action):

    def name(self):
        return "action_external_knowledge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):

        user_query = tracker.latest_message.get("text")
        result = external_search(user_query)

        if result:
            source, answer = result
            dispatcher.utter_message(
                text=f"🔎 Source: {source}\n\n{answer}"
            )
        else:
            dispatcher.utter_message(
                text="Sorry, I couldn’t find reliable information for that 😕"
            )

        return []
