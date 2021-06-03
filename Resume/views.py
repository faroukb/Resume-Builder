from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Resume, Education, Experience
from django.utils import timezone
from django.urls import reverse, NoReverseMatch
from django.contrib import auth
from django.template import loader

import pdfkit




def index(request):
    resumes_list = Resume.objects.filter(user_id=request.user.id)
    return render(request, 'Resume/resume.html', {'resumes_list': resumes_list})


def addnew(request):

    if request.POST:
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        zip_code = request.POST.get('zip_code', '')
        job_title = request.POST.get('job_title', '')
        summary = request.POST.get('summary', '')

        r = Resume(first_name=first_name,
                   last_name=last_name,
                   email=email,
                   phone=phone,
                   address=address,
                   city=city,
                   state=state,
                   country=country,
                   zip_code=zip_code,
                   summary=summary,
                   job_title=job_title,
                   user_id=request.user)

# Education
        start_dates = request.POST.getlist('year_start', '')
        end_dates = request.POST.getlist('year_end', '')
        organizations = request.POST.getlist('organization', '')
        titles = request.POST.getlist('title', '')
        descriptions = request.POST.getlist('description', '')
        ed_list = []
        for i in range(len(start_dates)):
            if start_dates[i] != "" and end_dates[i] != "" and organizations[i] != "" and titles[i] != "":
                ed = Education(start_date=start_dates[i],
                               end_date=end_dates[i],
                               organization_name=organizations[i],
                               title=titles[i],
                               description=descriptions[i],
                               resume_id=r)
                ed_list.append(ed)
# Experience
        ex_start_dates = request.POST.getlist('ex_year_start', '')
        ex_end_dates = request.POST.getlist('ex_year_end', '')
        companies = request.POST.getlist('company', '')
        positions = request.POST.getlist('position', '')
        ex_descriptions = request.POST.getlist('ex_description', '')
        ex_list = []
        for i in range(len(ex_start_dates)):
            if ex_start_dates[i] != "" and ex_end_dates[i] != "" and companies[i] != "" and positions[i] != "":
                ex = Experience(start_date=ex_start_dates[i],
                                end_date=ex_end_dates[i],
                                company_name=companies[i],
                                position=positions[i],
                                description=ex_descriptions[i],
                                resume_id=r)
                ex_list.append(ex)

        try:
            r.save()
            for x in ed_list:
                x.resume_id = r
                x.save()
            for y in ex_list:
                y.resume_id = r
                y.save()
            return render(request, 'Resume/addnew.html', {'status': 'Resume was added'})
        except:
            return render(request, 'Resume/addnew.html', {'error': 'Something went wrong'})

    else:
        return render(request, 'Resume/addnew.html')


def resume_details(request, resume_id):
    if request.user == Resume.objects.get(id=resume_id).user_id:
        safety = True
    else:
        safety = False
    resume = Resume.objects.get(id=resume_id)
    experience = Experience.objects.filter(resume_id=resume_id)
    education = Education.objects.filter(resume_id=resume_id)
    return render(request, 'Resume/resume_details.html', {'resume': resume, 'experience': experience, 'education': education, 'safety': safety})


def editresume(request, resume_id):

    if request.user != Resume.objects.get(id=resume_id).user_id:
        return render(request, 'Resume/addnew.html', {'error': 'You don\'t have permission edit this page'})
    if request.POST.get('job_title', ''):
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        zip_code = request.POST.get('zip_code', '')
        job_title = request.POST.get('job_title', '')
        summary = request.POST.get('summary', '')

        r = Resume(id=resume_id,
                   first_name=first_name,
                   last_name=last_name,
                   email=email,
                   phone=phone,
                   address=address,
                   city=city,
                   state=state,
                   country=country,
                   zip_code=zip_code,
                   summary=summary,
                   job_title=job_title,
                   user_id=request.user)

# Education
        start_dates = request.POST.getlist('year_start', '')
        end_dates = request.POST.getlist('year_end', '')
        organizations = request.POST.getlist('organization', '')
        titles = request.POST.getlist('title', '')
        descriptions = request.POST.getlist('description', '')
        ed_list = []
        for i in range(len(start_dates)):
            if start_dates[i] != "" and end_dates[i] != "" and organizations[i] != "" and titles[i] != "":
                ed = Education(start_date=start_dates[i],
                               end_date=end_dates[i],
                               organization_name=organizations[i],
                               title=titles[i],
                               description=descriptions[i],
                               resume_id=r)
                ed_list.append(ed)
# Experience
        ex_start_dates = request.POST.getlist('ex_year_start', '')
        ex_end_dates = request.POST.getlist('ex_year_end', '')
        companies = request.POST.getlist('company', '')
        positions = request.POST.getlist('position', '')
        ex_descriptions = request.POST.getlist('ex_description', '')
        ex_list = []
        for i in range(len(ex_start_dates)):
            if ex_start_dates[i] != "" and ex_end_dates[i] != "" and companies[i] != "" and positions[i] != "":
                ex = Experience(start_date=ex_start_dates[i],
                                end_date=ex_end_dates[i],
                                company_name=companies[i],
                                position=positions[i],
                                description=ex_descriptions[i],
                                resume_id=r)
                ex_list.append(ex)

        try:
            r.save()
            Experience.objects.filter(resume_id=resume_id).delete()
            Education.objects.filter(resume_id=resume_id).delete()
            for x in ed_list:
                x.save()
            for y in ex_list:
                y.save()
            return render(request, 'Resume/edit.html', {'status': 'Resume was edited'})
        except:
            return render(request, 'Resume/edit.html', {'error': 'Something went wrong'})

    else:
        resume = Resume.objects.get(id=resume_id)
        experience = Experience.objects.filter(resume_id=resume_id)
        education = Education.objects.filter(resume_id=resume_id)
        return render(request, 'Resume/edit.html', {'resume': resume, 'experience': experience, 'education': education})


def deleteresume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    try:
        resume.delete()
        return render(request, 'Resume/delete.html', {'status': 'Resume was deleted'})
    except:
        return render(request, 'Resume/delete.html', {'error': 'Something went wrong'})


def login(request):

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("error")
            return render(request, 'Resume/login.html', {'error': 'Wrong password or username'})
    else:
        return render(request, 'Resume/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'Resume/addnew.html')


def signup(request):

    if request.POST:
        username = request.POST.get('new_username', '')
        password = request.POST.get('new_password', '')
        passwordcheck = request.POST.get('passwordcheck', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        if (password != passwordcheck):
            return render(request, 'Resume/signup.html', {'error': "Passwords don't match"})
        user = User.objects.create_user(username, email, password)
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'Resume/login.html')
        else:
            return render(request, 'Resume/signup.html', {'error': "Something went wrong!"})
    else:
        return render(request, 'Resume/signup.html')



def download(request,resume_id):
    resume= Resume.objects.get(id=resume_id)
    experience = Experience.objects.filter(resume_id=resume_id)
    education = Education.objects.filter(resume_id=resume_id)
    html = loader.render_to_string('Resume/download.html', {'resume': resume, 'experience': experience, 'education': education})
    options={
        'page-size':'Letter',
        'encoding' : 'UTF-8',
        'enable-local-file-access': None,
    }

    pdf= pdfkit.from_string(html, False, options)
    response= HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition']= 'attachment'
    return response

