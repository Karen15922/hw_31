from rest_framework.generics import CreateAPIView  # type: ignore
from rest_framework.generics import (DestroyAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.viewsets import ModelViewSet  # type: ignore

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer

class CourseViewSet(ModelViewSet):
    """
    контроллер CRUD курса
    """
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class LessonCreateApiView(CreateAPIView):
    """
    контроллер создания урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(UpdateAPIView):
    """
    контроллер редактирования урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveApiView(RetrieveAPIView):
    """
    контроллер детального отображения урока
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


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
