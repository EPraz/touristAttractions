from django.shortcuts import render
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm
from django.views.generic.edit import CreateView

# This is the dictionary for all the attractions
attractions = [
  { 'attraction_name' : 'Niagra Falls', 'state' : 'New York'},
  { 'attraction_name' : 'Grand Canyon National Park', 'state' : 'Arizona'},
  { 'attraction_name' : 'Mall of America', 'state' : 'Minnesota'},
  { 'attraction_name' : 'Mount Rushmore', 'state' : 'South Dakota'},
  { 'attraction_name' : 'Times Square', 'state' : 'New York'},
  { 'attraction_name' : 'Walt Disney World', 'state' : 'Florida'}
]

def home(request):
  # The context is all of the variables we want passed into the template.
  context = {"attractions" : attractions}
  return render(request, 'tourist_attractions/home.html', context)

def details(request, statename):
  # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'tourist_attractions/details.html', context)


class StateCreateView(CreateView):
  model = State
  form_class = StateCreateForm
  template_name = "tourist_attractions/state_create_form.html"

class AttractionCreateView(CreateView):
  model = Attraction
  form_class = AttractionCreateForm
  template_name = "tourist_attractions/attraction_create_form.html"