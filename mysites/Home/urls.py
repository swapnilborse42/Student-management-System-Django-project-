from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.MyHome,name='home'),
    #path('login/',views.Login,name="home-login"),
    path('login/',views.Login,name="login"),
    path('about/',views.about,name="about"),
    path('feedback',views.feedback,name="feedback"),
    path('update_student/<int:std_id>/',views.update_student,name="update_student"),
    path('student-signup/',views.Student_Signup,name='student-signup'),
    path('bonafide_certificate/<int:std_id>/',views.bonafide_certificate,name='bonafide_certificate'),
    path('teacher-signup/',views.Teacher_Signup,name='teacher-signup'),
    path('student-signup/register/',views.Student_Register,name='student-register'),
    path('teacher-signup/register/',views.Teacher_Register,name='teacher-register'),
    path('login-delete/<int:std_id>/',views.Student_delete_view,name='student-delete'),
    # path('login/<str:year>/',views.Student_list_view_year,name='student-year'),
    path('teacher-signup/register/<str:year>/',views.Teacher_Register,name='teacher-register'),
    path('login/attendance',views.Add_Attendance,name='attendance'),
    path('login/attendance1',views.Add_Attendance1,name='attendance1'),
    path('login/attendance2',views.Add_Attendance2,name='attendance2'),
    path('login/attendance3',views.Add_Attendance3,name='attendance3'),
    path('login/attendance4',views.Add_Attendance4,name='attendance4'),

    path('login/student_view1',views.student_view1,name='student_view1'),
    path('login/student_view2',views.student_view2,name='student_view2'),
    path('login/student_view3',views.student_view3,name='student_view3'),
    path('login/student_view4',views.student_view4,name='student_view4'),
    path('parent',views.parent,name='parent'),
    path('login/notify',views.notifyme,name='notifyme')
    
]
