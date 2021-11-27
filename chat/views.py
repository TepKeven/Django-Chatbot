from django.shortcuts import render,HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import json


# Create your views here.
def chat_view(request):
    chatbot = ChatBot("Cool")
    chatbot.storage.drop()
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(
        "chatterbot.corpus.custom.service",
        "chatterbot.corpus.english.greetings",
    )
    response = chatbot.get_response("tell course ")
    data ={
        "chat": response.text
    }
    data = json.dumps(data)
    return HttpResponse(data,content_type="application/json")
