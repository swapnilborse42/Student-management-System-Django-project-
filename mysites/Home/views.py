from django.shortcuts import render,redirect
from dashboard.models import Student
from Home.models import Teacher,Subject,Attendance,Notify,Feedback
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
import time
# Create your views here.
def Login(request):
    template_name_one = "Home/student_login_view.html"
    template_name_two = "Home/base_error.html"
    template_name_three = "Home/teacher_login_view.html"
    template_name_four = "Home/admin_view.html"
    if request.method == 'POST':
      role = request.POST.get('role')
      email = request.POST.get('email')
      password = request.POST.get('password')
      print(role+email+password)
      if (role == "0" ):
          context={
            'message' : "Please Select Valid User Designation!..."
          }
          return render(request,template_name_two,context)
      elif (role == "1"):
          try:
            #print("role is student")
            s = Student.objects.get(email=email)
            PRN2=s.PRN
            #for attendace count
            mydate=time.strftime('%Y-%m-%d') 
            attend=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate)
            math=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate,subject_name="Math")

            coa=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate,subject_name="Coa")
            a=len(attend)
            b=len(math)
            c=len(coa)
            print(s.first_name)
            if(s.password == password):
              print("user found pass matched")
              notif=Notify.objects.get(ID=1)
              context={
                  'student':s,
                  'notif':notif,
                  'atten':a,
                  'math':b,
                  'coa':c
                } 
              return render(request,template_name_one,context)
            else:
              context={
                  'message' : "Password didn't match Please try again!..."
                } 
              return render(request,template_name_two,context)
          except:
            context={
            'message' : "Users Doesnt Exists!..."
                    } 
            return render(request,template_name_two,context)
            #print("no user in db")
            #raise Http404
      elif (role == "2"):
          print("role is teacher")
          try:
            s = Teacher.objects.get(email=email)
            print(s.first_name)
            if(s.password == password):
              print("user found pass matched")
              notif=Notify.objects.get(ID=2)
              context={
                  'students':Student.objects.all(),
                  'notif':notif
                } 
              return render(request,template_name_three,context)
            else:
              context={
                'message' : "Password didn't match Please try again!..."
              }
              return render(request,template_name_two,context)
              print("user found pass not matched")
          except Exception as e:
            print("i dont know")
            print(e)
            context={
            'message' : "Uers Doesnt Exists!..."
                    } 
            return render(request,template_name_two,context)


      elif (role == "3"):
          try:
            Feed=Feedback.objects.all()
            print("Feed")
            print(Feed)           
            if(email=="ADMIN@123" and password=="ADMIN@123"):
              print("user found pass matched")
              context={
                  'student':"hello",
                  'feed':Feed
                } 
              return render(request,template_name_four,context)
            else:
              context={
                  'message' : "Password didn't match Please try again!..."
                } 
              return render(request,template_name_two,context)
          except:
            context={
            'message' : "Users Doesnt Exists!..."
                    } 
            return render(request,template_name_two,context)
            #print("no user in db")
            #raise Http404
          
              



    else:
      context={
            'message' : "It seems you have not LoginIn!..."
                    } 
      return render(request,template_name_two,context)
        
def MyHome(request):
  Feed=Feedback.objects.all()
  print("Feed")
  print(Feed)
  context={
    'feed':Feed
  }
  return render(request,'Home/home.html',context)

def Student_Signup(request):
    return render(request,'Home/student_signup.html')

def Teacher_Signup(request):
    return render(request,'Home/teacher_signup.html')

def Student_Register(request):
    if request.method == 'POST':
            #if request.POST.get('prn'):
                student=Student()
                student.PRN= request.POST.get('prn')
                student.first_name = request.POST.get('first_name')
                student.last_name = request.POST.get('last_name')
                student.mobile_no = request.POST.get('mobile_no')
                student.email = request.POST.get('email')
                student.gender = request.POST.get('gender')
                student.state = request.POST.get('state')
                student.course = request.POST.get('course')
                student.address = request.POST.get('address')
                student.branch = request.POST.get('branch')
                student.division = request.POST.get('div')
                student.adm_cat= request.POST.get('adm_cat')  
                student.dob = request.POST.get('dob')
                student.password = request.POST.get('password')
                try:
                  student.save()
                except:
                  return HttpResponse("<h2 align=center>Student with Given PRN OR EMAIL already present...<h2>")
                #print("student")
                #print(student.division)
                #return HttpResponse("student")
                template_name = "Home/student_login_view.html"
                context={
                  'student':student
                } 
                return render(request,template_name,context)

    else:
      #print("in else")
      #return HttpResponse("else")
      template_name = "Home/login_register_error.html"
      return render(request,template_name)

def Teacher_Register(request):
    if request.method == 'POST':
            #if request.POST.get('prn'):
                teacher=Teacher()
                teacher.T_PRN= request.POST.get('tprn')
                teacher.first_name = request.POST.get('first_name')
                teacher.last_name = request.POST.get('last_name')
                teacher.mobile_no = request.POST.get('mobile_no')
                teacher.email = request.POST.get('email')
                teacher.gender = request.POST.get('gender')
                teacher.state = request.POST.get('state')
                teacher.course = request.POST.get('course')
                teacher.address = request.POST.get('address')
                teacher.department = request.POST.get('branch')
                print(teacher.T_PRN+teacher.first_name+teacher.last_name)
                print(teacher.mobile_no+teacher.email+teacher.gender+teacher.state+teacher.course)
                print(teacher.address+teacher.department)
                teacher.years = request.POST.getlist('years')
                print(teacher.years)
                teacher.subjects = request.POST.get('subject')
                print(teacher.subjects)
                teacher.doj = request.POST.get('doj')
                teacher.password = request.POST.get('password')
                print(teacher.doj+teacher.password)
                try:
                  teacher.save()
                  print("teacher saved")
                except:
                  return HttpResponse("<h2 align=center>Teacher with Given TPRN OR EMAIL already present...<h2>")
                #print("student")
                #print(student.division)
                #return HttpResponse("student")
                template_name = "Home/teacher_login_view.html"
                context={
                  'students':Student.objects.all()
                } 
                return render(request,template_name,context)
    else:
      #print("in else")
      #return HttpResponse("teacher else")
      template_name = "Home/login_register_error.html"
      return render(request,template_name)

def Student_delete_view(request,std_id):
    prn = std_id
    template_name = "Home/teacher_login_view.html"
    try:
        student_obj = Student.objects.get(PRN=prn)
        student_obj.delete()
    except:
        raise Http404
    context={
                  'students':Student.objects.all()
                } 
    return render(request,template_name,context)

# def Student_list_view_year(request,year):#details in student module
#     std_year = year
#     print(std_year)
#     template_name = "/Home/teacher_login_view.html"
#     try:
#         student_obj = Student.objects.all().filter(division=std_year)
#     except Exception as e:
#       print(e)    
#     context={
#                   'students':student_obj
#             } 
#     return render(request,template_name,context)

def Add_Attendance(request):
    template_name = "Home/attendance.html"
    student_obj = Student.objects.all()
    context={
                  'students':student_obj
                } 
    
    if request.method == "POST":
      # a = Attendance()
      # yr=request.POST['year']
      # if(yr=="FE"):
      #   FE(request,yr)  
      PRN = request.POST.getlist('prn[]')
      atten = request.POST.getlist('testName[]')
      dob=request.POST.getlist('dob[]')
      print(PRN)
      print(atten)
      
      for i in range(0,len(PRN)):
        # print(temp)
        prn=PRN[i]
        a=atten[i]
        dobirth=dob[i]
        #  print(prn)
        #  print(x)
        y=request.POST['attend-date']
        sub=request.POST['subject']
        print(sub)
        
        a=Attendance(PRN=prn,subject_name=sub,status=a,date=y,dob=dobirth)
        a.save()
        # a.PRN=temp
        # a.subject_id = 100
        # a.status = request.POST['status']
        # a.date = request.POST['attend-date']
        
      # print(a)
      return render(request,template_name,context)

    else:
      print("in att")
      return render(request,template_name,context)

# def FE(request,yr):
#   template_name = "Home/attendance.html"
#   student_ob = Student.objects.filter(division=yr)
#   context1={
#                   'students':student_ob
#                 }
#   return render(request,template_name,context1)

def Add_Attendance1(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='FE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance2(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='SE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance3(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='TE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance4(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='BE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def student_view1(request):
  template_name = "Home/year_view/student_view1.html"
  student= Student.objects.filter(division='FE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def student_view2(request):
  template_name = "Home/year_view/student_view1.html"
  student= Student.objects.filter(division='SE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def student_view3(request):
  template_name = "Home/year_view/student_view1.html"
  student= Student.objects.filter(division='TE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def student_view4(request):
  template_name = "Home/year_view/student_view1.html"
  student= Student.objects.filter(division='BE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)
 
#   template_name = "Home/attendance.html"
#   if request.method == "POST":
#     yr=request.POST['year']
#     if yr=="TE":
#       student_ob = Student.objects.filter(division=yr)
#       context1={
#                   'studen':student_ob
#                 }
#       return render(request,template_name,context1)

      

def parent(request):
  
  if request.method == "POST":
    PRN1 = request.POST['prn']
    PRN2=int(PRN1)
    dob1 = request.POST['dob']
    dob2=dob1
 
    # print(PRN1)
    queryset=Student.objects.values_list('PRN',flat=True)
    queryset1=Student.objects.values_list('dob',flat=True)
    studdata=Student.objects.get(PRN=PRN2)
    notif=Notify.objects.get(ID=3)

    mydate=time.strftime('%Y-%m-%d') 
    # print(livedate)
    attend=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate)
    math=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate,subject_name="Math")
    coa=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate,subject_name="Coa")
    Attendace_count=len(attend)
    b=len(math)
    c=len(coa)
    print(attend)
    

    for i in queryset:
        if (PRN2==i):
          print(PRN1)
          for j in queryset1:
            if (dob2==j):
              print(dob1)
              template_name = "Home/parentview.html"
              data={
                      "showdata":studdata,
                       "count":Attendace_count,
                       'notif':notif,
                       'math':b,
                       'coa':c

              }
              return render(request,template_name,data)
              
        else:
          pass
    template_name = "Home/parent.html"  
    data={
                      "myname":"SRY!!! WRONG PRN OR DATE OF BIRTH",
                }
    return render(request,template_name,data)       
  

  else:
    template_name = "Home/parent.html"
    return render(request,template_name)
    

# def update_student(request):
#   if request.method == "POST":
#       d=request.POST.get('update')
#       print(d)
#       print(d)
#       if(d=="1"):

#         data={
#          'd':d
#         }
#         template_name = "Home/update_student.html"
#         return render(request,template_name,data)


#   else:
#       template_name = "Home/update_student.html"
#       return render(request,template_name)
def update_student(request,std_id):#by student
  if request.method == "POST":
    # PRN1 = request.POST['prn']
    print(123)
    s = Student.objects.get(PRN=std_id)
    s.email=request.POST.get('email')
    s.mobile_no=request.POST.get('num')
    s.password=request.POST.get('pass')
    s.save()
    return redirect('/home')
  else:
    prn = std_id
    print(prn)
    print(prn)
    template_name = "Home/update_student.html"
    student_obj = Student.objects.get(PRN=prn)
    context={
                  'students':student_obj
    } 
    return render(request,template_name,context)

def bonafide_certificate(request,std_id):
  prn = std_id
  print(prn)
  print(prn)
  template_name = "Home/bonafide_certificate.html"
  student_obj = Student.objects.get(PRN=prn)
  mydate=time.strftime('%Y-%m-%d') 
  context={
                  'students':student_obj,
                   'date': mydate
  } 
  return render(request,template_name,context)
  

def notifyme(request):
  idd=request.POST['idd']
  msg=request.POST['msg']
  print(idd)
  print(msg)
  if(idd=="1"):
    s = Notify.objects.get(ID=idd)
    s.subject_name=msg
    s.save()
  if(idd=="2"):
    s = Notify.objects.get(ID=idd)
    s.subject_name=msg
    s.save()
  if(idd=="3"):
    s = Notify.objects.get(ID=idd)
    s.subject_name=msg
    s.save()
  template_name ="Home/admin_view.html"
  return render(request,template_name)
  # if(idd=="2"):
  #   a=Notify(ID=idd,subject_name=msg)
  #   a.save()
  # if(idd=="3"):
  #   a=Notify(ID=idd,subject_name=msg)
  #   a.save()

def about(request):
  template_name = "Home/about.html"
  return render(request,template_name)

def feedback(request):
  if request.method == "POST":
    print("1")
    name = request.POST['name']
    email = request.POST['email']
    feedback = request.POST['feed']
    a=Feedback(name=name,email=email,feedback=feedback)
    a.save()
    template_name = "Home/home.html"
    return render(request,template_name)


  else:
    print("2")
    template_name = "Home/feedback.html"
    return render(request,template_name)