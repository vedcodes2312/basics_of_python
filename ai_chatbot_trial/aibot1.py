#AI chatbot in python 
#Google AI Studio and Gemini is used to create this chatbot
#by Ved Vyas github: vedcodes2312

import google.generativeai as ai 

#API key
API_KEY= 'AIzaSyC2CcPU1CymhTIXNORsbDcC9CnaSMzjRF4'

#initialize the API(configure)
ai.configure(api_key = API_KEY)

#create a model

model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

#start a conversation

while True:
    message = input('You: ')
    if message.lower() == 'bye':
        break
    response = chat.send_message(message)
    print('Foodie AI ChatBot: ', response.text)
