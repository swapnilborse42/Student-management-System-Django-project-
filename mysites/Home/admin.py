from django.contrib import admin
from Home.models import Teacher,Subject,Attendance,Notify,Feedback

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Notify)
admin.site.register(Feedback)
