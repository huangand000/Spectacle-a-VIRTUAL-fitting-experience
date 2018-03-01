from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import datetime
import random

def index(request):
    return render(request,"chatbot/index2.html")

@csrf_exempt
def bot(request):
    userInput = str(request.POST['input'].lower())
    CONVERSING = True
    memory = []
    response =''

    greetings = ['Hola', 'Hello', 'hi','hey!','Hello','Hi','Ni Hao']
    
    greetings_questions = ['how are you?','how are you doing?','how are you','how are you doing']
    greetings_response= ['Okay','I am fine!','I am doing great!']
    
    having_questions = ['a question']
    question_response = ['How can I help you?']

    time_question = ['time is']
    time_response = ['It is now '+datetime.datetime.now().strftime('%H:%M')]

    validations = ['yes','yeah','yea','no','No','Nah','nah']
    verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
    storInfo = ['Please refer store locator for more store information']
    storeQuestions =['location','hours','stores','store','open','close','distance','address']

    thanks = ['thank']
    thanks_response = ['You are very welcome'] 


    while CONVERSING:
        if  any(word in userInput for word in greetings):
            random_greeting = random.choice(greetings)
            # say(random_greeting)
            response = random_greeting
            CONVERSING = False
        elif userInput in greetings_questions:
            response = random.choice(greetings_response)
            # say(response)
            CONVERSING = False
        elif any(word in userInput for word in having_questions):
            response = question_response
            # say(response)
            CONVERSING = False
        elif any(word in userInput for word in time_question):
            response = time_response
            # say(response)
            CONVERSING = False
        elif any(word in userInput for word in thanks):
            response = thanks_response
            # say(response)
            CONVERSING = False
        elif any(word in (userInput) for word in storeQuestions):
            response = storInfo
            # say(response)
            CONVERSING = False
        elif userInput in verifications:
            random_response = random.choice(validations)
            # say(random_response)
            CONVERSING = False
        elif userInput in storeQuestions:
            random_response = random.choice(validations)
            # say(random_response)
            CONVERSING = False
        elif 'sure' in userInput:
            response = "Sure about what?"
            CONVERSING = False
            # say(response)
        else:
            response = "I did not understand your question"
            # say(response)
            CONVERSING = False
            # CONVERSING = False
            
    context = {
        'response': response
    }
    return JsonResponse(context)



