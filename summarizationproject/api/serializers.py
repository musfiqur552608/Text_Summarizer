from rest_framework import serializers
from .models import Summarizer

class SummarizerSerializer(serializers.Serializer):
    mytext = serializers.CharField(max_length=1000000)
    myword = serializers.IntegerField()
    summarize = serializers.CharField(max_length=1000000)
    sumword = serializers.IntegerField()
    # created this function for create, read, delete
    def create(self, validated_data):
        return Summarizer.objects.create(**validated_data)
    # created this function for update
    def update(self, instance, validated_data):
        instance.mytext = validated_data.get('mytext', instance.mytext)
        instance.myword = validated_data.get('myword', instance.myword)
        instance.summarize = validated_data.get('summarize', instance.summarize)
        instance.sumword = validated_data.get('sumword', instance.sumword)
        instance.save()
        return instance