from django.shortcuts import render
from apps.tasks.serializers import TaskSerializer
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.tasks.models import Task
# Create your views here.


class CreateTaskView(GenericAPIView):
    serializer_class = TaskSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(TaskSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        task = Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            status=validated_data['status'],
            assignee=validated_data['assignee']
        )

        return Response(TaskSerializer(task).data)


class GetTasksView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        tasks = Task.objects.all()
        return Response(TaskSerializer(tasks).data)
