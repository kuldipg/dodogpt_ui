import openai
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

openai.api_key = "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"

conversation_history = []

class ChatbotAction(Action):
    def name(self) -> Text:
        return "action_chatbot"

    def get_chatbot_response(self, user_query):
        global conversation_history
        prompt = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
        
        
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = prompt,
            n = 4,
            max_tokens = 2048,
            temperature = 0.6
            
        )
        
        response = completion['choices'][0]['message']['content']
        conversation_history += [{"role": "assistant", "content": response}]

        return response

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('Im in run')
        user_query = tracker.latest_message.get('text')
        response = self.get_chatbot_response(user_query)
        dispatcher.utter_message(response)

        return []
