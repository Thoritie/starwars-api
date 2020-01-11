from rest_framework import serializers

from core.models import People


class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = [ 'name', 'gender', 'homeworld']
