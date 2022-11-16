from django.shortcuts import render,HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import json


# Create your views here.
def chat_view(request):
    chatbot = ChatBot("Bot",storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatbot.sqlite3',read_only=True)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(
        "corpus.english.training"
    )
    response = chatbot.get_response("how are you")
    data ={
        "chat": response.text
    }
    data = json.dumps(data)
    return HttpResponse(data,content_type="application/json",status = 200)
