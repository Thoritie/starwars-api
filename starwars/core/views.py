from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import People, Planet
from core.serializers import PeopleSerializers


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
            serializer = PeopleSerializers(people)
            person = serializer.data

            people_list.append(person)

        return Response(people_list)

    def post(self, request):
        data = request.data

        homeworld = Planet.objects.first()

        serializer = PeopleSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
