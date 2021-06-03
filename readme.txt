CS50W Final Project 

This is a web application to create and download your pdf resume online.
To buils this project i used all the technologies i have learned in this course (css, html, javascript,bootstrap and python). 
The nature of this project is different from the other projects, it's designed to help people create a resume online fast and easy and download it as pdf with a click.
This project is more complex than the others in this course, this application is mobile-responsive and i used a python library, pdfkit that we didn't use before to generate the pdf file.



Project structure:

Static/Resume : in static folder there is the javascript and css files:
     
    -script_before.js: in this file there is two javascript functions to delete the education and experience from the resume builder form.
    -script.js: a javascript code to add another education or experience to the resume builder form.
    -styles.css: the css style of the app and the resume.

templates/Resume: in this folder there is the html templates of the app:
    -addnew.html: the template to add a new resume.
    -delete.html: template to delete a resume.
    -download.html: the template of the resume that will be downloaded as a pdf.
    -edit.html: to edit your resume content.
    -layout.html:the website layout .
    -login.html: login template.
    -logout.html:logout template.
    -resume_details.html: the resume you get after submitting the form.
    -resume.html: the profile page template shgowing your resume(s) if you have any created with a download button, if you don't have any resume a message will be displayed        saying "You don't have any resumes yet."
    -signup.html:the signup template.
    
        
admin.py: display the models in the admin panel.

models.py: three models : Resume, Experience and Education.

urls.py: contains the urls for each view in the app.

views.py:
   -index view : render the resume.html and displays a list of your resumes.
   -addnew view : to add new resume.
   -resume_details view: render created resume.
   -editresume view: to edit an existing resume from your list.
   -deletresume view : to delete a resume from your list.
   -login/logout/signup views : to create and access user account.
   -download view: to convert a resume to a pdf file and download it.
   
  
To run the application you need to pass this command to your command line:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver  

    

