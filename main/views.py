from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

# from forms import MyRegistrationForm

@twilio_view
def sms(request):
  message = request.POST.get('Body', '')
  r = Response()
  r.message(message)
  return r
