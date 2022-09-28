from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'short_answer', 'answer', 'importance', 'category']
        extra_kwargs = {
            'answer': {'write_only': True},
        }


class QuestionAnswerRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
