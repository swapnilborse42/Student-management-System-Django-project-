# Student-management-System-Django-project-
This is the Django project for Student Management system.

Admin-This is the admin pannel for principle or System Controller..This is not the Django Admin pannel.
admin can access admin pannel by login through login form on home page
1. Sign up for students is done here.
2. Sign up for teachers is done here.
3. Just like our collage..teacher and student authentication credentials are provided collage.(which are generated by admin).
4. Any notifications for students, teachers and parents are generated here by admin.(This notifs are shown to students, teachers and parents are there login).

Teacher -This is the pannel for teachers. Teacher can access teacher pannel by login through login form on home page.
1. Teacher can see all year students and sort them according to there year.
2. Teacher can delete any student from database.
3. Teacher can update students attendance for particular subject.
4. Teacher can see notifs at top notified by Admin.

Student -This is the pannel for student. Student can access student pannel by login through login form on home page.
1. Student can view his details and attendance.
2. Student can update his details
4. Student can see notifs at top notified by Admin.

Parents - This is the pannel for parents. parents can access parents pannel by login through login form on home page using student PRN number and his date of birth.

1. parents can see his son info and attendance in parent pannel.
2. Parent can see notifs at top notified by Admin.
3. can submit feedback.

Anyone visits site can submit feedback for collage.

# packages installed in virtial environment with there version
astroid==2.2.5 <br>
colorama==0.4.1 <br><br>
Django==2.2.5<br>
django-pgfields==1.4.4<br>
isort==4.3.21<br>
lazy-object-proxy==1.4.2<br>
mccabe==0.6.1<br>
psycopg2==2.8.3<br>
pylint==2.3.1<br>
pytz==2019.2<br>
six==1.12.0<br>
sqlparse==0.3.0<br>
typed-ast==1.4.0<br>
wrapt==1.11.2<br>

# setup 
1. Download project zip and extract it.<br>
1.1. Install " postgresql-9.5.19-1-windows-x64.exe " inside zip <br>
2. Open the project folder inside visual studio code<br>
3. press ctrl + shift + p or view -> command palette and select the virtual environment name as env:venv.<br>
4. press <b>ctrl + shift +  `<b> --- will open terminal inside virtual environment.<br>
5. In terminal python manage.py runserver to run project.<br>
6. If error occours for package missing then install above version for that specified package.<br>
  In my case errors are solve by installing these (after setup for 2nd time from git)-<br>
   postgresql-9.5.19-1-windows-x64.exe
  
# Django Tutorial in Visual Studio Code- (some common commands in use)
  Create a project virual environment for the Django tutorial.<br>
  #Windows<br>
  python -m venv env<br>
  In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:<br>
  The command presents a list of available interpreters that VS Code can locate automatically. select the virtual environment in your project folder<br>
  
  Install Django in the virtual environment by running one of the following commands in the VS Code Terminal:<br>
  python -m pip install django<br>
  
  Create the Django project<br>
  In the VS Code Terminal where your virtual environment is activated, run the following command:<br>
  django-admin startproject web_project .<br>
  
  Create a Django app<br>
  In the VS Code Terminal with your virtual environment activated, run the administrative utility's startapp command in your project folder (where manage.py resides):<br>
  python manage.py startapp hello.<br>
  
  In the VS Code Terminal, again with the virtual environment activated, run the development server with python manage.py runserver and open a browser to http://127.0.0.1:8000/    to see a project home page<br>
  
  After modifing model files run following commands to make changes inside database<br>
  python manage.py makemigrations<br>
  python manage.py migrate<br>
  
  to accesee Django admin pannel(/admin) to make entry inside database we need to create a superuser<br>
  python manage.py createsuperuser<br>
  
  # some references to learn Django-
  https://code.visualstudio.com/docs/python/tutorial-django <br>
  https://docs.djangoproject.com/en/2.2/ref/models/fields/<br>
  https://djangobook.com/mdj2-models/ <br>
  https://docs.djangoproject.com/en/3.1/topics/db/queries/ <br>
  https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294 <br>
  https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/ <br>
  https://books.agiliq.com/projects/django-orm-cookbook/en/latest/select_some_fields.html <br>
  https://bootsnipp.com/snippets/dldxB <br>

  
# screenshots (click to view in large)

<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/1.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/2.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/3.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/4.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/5.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/6.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/7.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/8.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/9.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/10.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/11.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/12.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/13.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/14.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/15.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/16.png" width="500" height="500"/><br>
<img src="https://github.com/swapnilborse42/Student-management-System-Django-project-/blob/master/images/17.png" width="500" height="500"/><br>



