from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from core.models import People


class PeopleListView(TemplateView):
    def get(self, request):
        people = People.objects.first()
        person = {
            'name': people.name,
            'gender': people.gender,
            'homeworld': people.homeworld.name
        }

        return JsonResponse(person)
