from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# FUNCTIONS FOR ROUTES
def index(request):
    return HttpResponse("Bad request use other routes")

def getTheGood(request):
    return HttpResponse("Here you go! Thai food!!!")

def happyHappy(request):
    return HttpResponse("Did I say Thai food?")

#
# incomplete challenge
# def acceptThis(request):
#     return HttpResponse("I heard you!" + )