from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from rest_framework import filters


from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionAnswerRUDSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListCreate(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'question']

    def get_queryset(self):
        queryset = QuestionAnswer.objects.order_by('-importance')
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class QuestionAnswerRUD(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerRUDSerializer


