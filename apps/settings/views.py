from django.http import HttpRequest
from django.shortcuts import render, redirect
from apps.settings.models import Settings, Shape, About, About_Person, Portfolio, Fact, Awards, Expirience, Education, Skills, Project, PricePlan, Quotes, ContactMe, Contact
from django.core.mail import send_mail
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    settings_id = Settings.objects.latest('id')
    shape_all = Shape.objects.all()
    about_id = About.objects.latest('id')
    about_person_id = About_Person.objects.latest('id')
    portfolio_all = Portfolio.objects.all()
    fact_all = Fact.objects.all()
    award_all = Awards.objects.all()
    expirience_all = Expirience.objects.all()
    education_all = Education.objects.all()
    skill_all = Skills.objects.all()
    project_all = Project.objects.all()
    price_plan_all = PricePlan.objects.all()
    quotes_all = Quotes.objects.all()
    contact_me_id = ContactMe.objects.latest('id')
    return render(request, 'index.html', locals())


def contact_views(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        page_contact = Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
        if page_contact:
            get_text(f"""
            Оставлена заявка на обратный звонок 📞
                         
    Имя пользователя:  {name}
    Почта: {email}
    Номер телефона: {phone}
    Объект: {subject}
    Сообщение: {message}

    """)
            return redirect('index')
    return render(request, 'index.html', locals())