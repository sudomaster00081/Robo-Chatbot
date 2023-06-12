from chatterbot import ChatBot

chatbot = ChatBot('MyChatBot')


from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings")


response = chatbot.get_response('Hello, how are you?')
print(response)
