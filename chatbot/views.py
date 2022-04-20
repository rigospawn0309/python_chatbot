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
    "hi there", #Respuesta
    "what is your name",
    "I'm chatbot",
    "food",
    "womens",
    ""
]

chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterBotCorpusTrainer.train('chatterbot.corpus.spanish')
chatterBotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'chatbot/index.html')
def specific(request):
    return HttpResponse("This is the specific url")
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
