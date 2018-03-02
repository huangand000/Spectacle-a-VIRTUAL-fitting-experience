from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import datetime
import random

def index(request):
    return render(request,"chatbot/index.html")

@csrf_exempt
def bot(request):
    userInput = str(request.POST['input'].lower())
    CONVERSING = True
    memory = []
    response =''
    merchant_name = ''   
    greetings = ['Hola', 'Hello', 'hi','hey!','Hello','Hi','Ni Hao']
    
    joke = [
        "I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
        "I bought some shoes from a drug dealer. I don't know what he laced them with, but I've been tripping all day.",
        "Two clowns are eating a cannibal. One turns to the other and says 'I think we got this joke wrong'",
        "My wife told me I had to stop acting like a flamingo. So I had to put my foot down.",
        "What's the difference between in-laws and outlaws? Outlaws are wanted.",
        "I poured root beer in a square glass.Now I just have beer."]
    joke_question = ['joke']

    
    if any(word in userInput for word in ['return','exchange']):
        merchant_name = userInput.split('policy')[1].split('of')[1].replace("?","")
    elif any(word in userInput for word in ['exchange policy']):
        merchant_name = userInput.split('exchange')[0].split("'s")

    love = ['love you']
    loveResponse = ['I love you,too']


    greetings_questions = ['how are you?','how are you doing?','how are you','how are you doing']
    greetings_response= ['Okay','I am fine!','I am doing great!']
    
    having_questions = ['a question']
    question_response = ['How can I help you?']

    time_question = ['time is',"what's the time",'what is the time']
    time_response = ['It is now '+datetime.datetime.now().strftime("%I:%M %p")]

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
        elif any(word in userInput for word in ['return','exchange']):
            if any(word in userInput for word in ['return']):
                response = merchant_name+"'s return policy can be found at www."+  merchant_name+".com/return"
                CONVERSING = False
            elif any(word in userInput for word in ['exchange']):
                response = merchant_name+"'s exchange policy can be found at www."+  merchant_name+".com/exchange"
                CONVERSING = False
        elif any(word in userInput for word in joke_question):
            response = random.choice(joke)
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
        elif any(word in userInput for word in love):
            response = loveResponse
            # say(response)
            CONVERSING = False
        elif any(word in userInput for word in thanks):
            response = thanks_response
            # say(response)
            CONVERSING = False
        elif any(word in (userInput) for word in storeQuestions):
            response = storInfo
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



