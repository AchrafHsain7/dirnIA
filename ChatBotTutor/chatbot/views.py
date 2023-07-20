from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

SYLLABUS = [{'name': "Section1: Intro to algorithmes", 'completed': True}, 
            {'name': "Section2: Greedy Search", 'completed': True},
            {'name': "Section3: Brute Force", 'completed': False},
            {'name': "Section4: Dynamic Programming", 'completed': False},
            ]

QUESTION_ANSWER = {"question": "What is a for loop used for", "answer": {"1": "To infinitely loop", "2": "To loop for a determined number of times",
                                                                           "3": "There is no such thing as a for loop", "4":"tHE HELL is that?"}}

def index(request):
    return render(request, 'chatbot/index.html', {
            "syllabus": SYLLABUS,
            "qa": QUESTION_ANSWER,
    })
  

             
