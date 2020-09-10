from django.conf.urls import url,include
from App import views

from rest_framework import routers

from App.views import ExamQuestionViewset
from . views import QuestionViewset, ExamViewset

router = routers.DefaultRouter()
router.register(r'question',QuestionViewset)
router.register(r'exam',ExamViewset)

urlpatterns = [
    url(r'^api/',include(router.urls)),
    url('',views.welcome,name="welcome"),
    url('create/',views.create_user,name="create_user"),
    url('validate_login/',views.log_in,name="log_user"),
    url('add_exam/',views.add_exam,name="add_exam"),
    url('add_question/',views.add_question,name="add_question"),
    url('test',views.get_data,name="getdata"),
    url('logout',views.log_out,name="log_out"),
]
