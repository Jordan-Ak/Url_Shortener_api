from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_link = serializers.ReadOnlyField()
    when_created = serializers.DateTimeField(format = "%H:%M, %d-%m-%Y", read_only =True,)

    class Meta:
        model = Link
        fields = '__all__'