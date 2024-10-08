from rest_framework.generics import CreateAPIView  # type: ignore
from rest_framework.generics import (DestroyAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet  # type: ignore
from users.permissions import IsModer, IsOwner

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer

class CourseViewSet(ModelViewSet):
    """
    контроллер CRUD курса
    """
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer, IsOwner)

        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    """
    контроллер создания урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class LessonUpdateApiView(UpdateAPIView):
    """
    контроллер редактирования урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]



class LessonRetrieveApiView(RetrieveAPIView):
    """
    контроллер детального отображения урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]



class LessonListApiView(ListAPIView):
    """
    контроллер отображения списка уроков
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(DestroyAPIView):
    """
    контроллер удаления урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer, IsOwner]
