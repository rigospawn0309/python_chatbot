from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
# Create your views here.
# Configuro el bot con BestMatch(MejorRespuesta => mirar los otros que hay)
bot = ChatBot('chatbot',read_only=False,logic_adapters=[
    {
        'import_path':'chatterbot.logic.BestMatch'
        #'default_response':'Sorry but my answers are still limited, try with another question',
        #'maximum_similarity_threshold':0.90 #si es menor a este valor se lanza default
    }
    ])

list_to_train = [
    "hi", #Pregunta
    "Hello, do you know each others?",#Respuesta
    "Hello, my name is John", 
    "Nice to meet you, John! Do you want to make an appointment for your car review?",
    "Yes, I am",
    "When would you like to do it?",
    "No",
    "Ok, have you another question?",
    "16th of August",
    "I have these times available: 8:30, 10:30, 11:00 and 12:00",
    "8:30 is ok",
    "Great your appointment code is TIAGD00!",
    "8:30",
    "Great your appointment code is TIAGD00!",
    "10:30 is ok",
    "Great your appointment code is TIAGD00!",
    "10:30",
    "Great your appointment code is TIAGD00!",
    "11:00 is ok",
    "Great your appointment code is TIAGD00!",
    "11:00",
    "Great your appointment code is TIAGD00!",
    "12:00 is ok",
    "Great your appointment code is TIAGD00!",
    "12:00",
    "Great your appointment code is TIAGD00!",
    "Thanks",
    "Thanks for trusting us"
]

chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
chatterBotCorpusTrainer.train('chatterbot.corpus.spanish')
chatterBotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'chatbot/index.html')
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
