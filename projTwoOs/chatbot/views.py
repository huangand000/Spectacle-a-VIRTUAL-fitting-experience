# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

import random
# from speech import *


def index(request):
    return render(request,"chatbot/index.html")

@csrf_exempt
def bot(text):
    return JsonResponse({'name':'laurece'})

# CONVERSING = True

# memory = []
# greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
# questions = ['How are you?','How are you doing?']
# responses = ['Okay','I am fine']
# validations = ['yes','yeah','yea','no','No','Nah','nah']
# verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]

# storInfo = ['Please refer store locator for more store questions']
# storeQuestions =['location','hours','stores','store','open','close','distance']

# while CONVERSING:
# 	lang = 'en-US'
# 	speed = .3
	
# 	# userInput = text
#   	userInput = raw_input("How can I help you?")
# 	if userInput in greetings:
# 		random_greeting = random.choice(greetings)
# 		# say(random_greeting)
# 		print random_greeting
# 		memory.append((userInput,random_greeting))
# 	elif any(word in (userInput).split() for word in storeQuestions):
# 		response = storInfo
# 		# say(response)
# 		memory.append((userInput,response))
# 		print response
# 	elif userInput in verifications:
# 		random_response = random.choice(validations)
# 		# say(random_response)
# 		memory.append((userInput,random_response))
# 		print random_response
# 	elif userInput in storeQuestions:
# 		random_response = random.choice(validations)
# 		# say(random_response)
# 		memory.append((userInput,random_response))
# 		print random_response

# 	elif 'sure' in userInput:
# 		response = "Sure about what?"
# 		# say(response)
# 		memory.append(('sure',response))
# 		print response
# 	else:
# 		# say("I did not understand what you said. Goodbye")

# 		CONVERSING = False
		
# for conversations in memory:
# 	print conversations
