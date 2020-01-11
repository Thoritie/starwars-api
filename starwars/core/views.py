from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import People, Planet


class PeopleListView(TemplateView):
    def get(self, request):
        people = People.objects.first()
        person = {
            'name': people.name,
            'gender': people.gender,
            'homeworld': people.homeworld.name
        }

        return JsonResponse(person)

class PeopleListApiView(APIView):
    def get(self, request):
        gender = request.query_params.get(
            'gender', None
        )

        if gender is not None:
            peoples = People.objects.filter(gender=gender)
        else:
            peoples = People.objects.all()

        people_list = []
        for people in  peoples:
            people = {
                'name': people.name,
                'gender': people.gender,
                'homeworld': people.homeworld.name
            }
            people_list.append(people)

        return Response(people_list)

    def post(self, request):
        data = request.data

        homeworld = Planet.objects.first()

        People.objects.create(
            name=data['name'],
            height=data['height'],
            mass=data['mass'],
            hair_color=data['hair_color'],
            skin_color=data['skin_color'],
            eye_color=data['eye_color'],
            gender=data['gender'],
            homeworld=homeworld
        )

        return_person = {
            'name': person.name,
            'gender': person.gender,
            'homeworld': person.homeworld.name
        }
        return Response(return_person)
