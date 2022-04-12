from fnmatch import translate
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.translation import gettext as _

from .models import Article, Service, Client
from .forms import ClientForm


def index(request):
    forms = ClientForm()
    articles = Article.objects.all()
    services = Service.objects.all()
    context = {
        'articles': articles,
        'services': services,
        'forms': forms,
    }
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        service = request.POST['service']
        client = Client(name=name, phone=phone, email=email)
        client.save()
        context['success'] = True
        send_mail(
            'Новый клиент',
            'Новый клиент: ' + name + '\n' + 'Телефон: ' + phone + '\n' + 'Почта: ' + email + '\n' + 'Услуга: ' + service, 
            'postmaster@sandboxd3d1ea751b8f42b395f3368371a3840c.mailgun.org',
            ['prdarishdery@gmail.com'],
        )
        return render(request, 'main_page/index.html', context=context)
    return render(request, 'main_page/index.html', context=context)


#def translate(language):
#    cur_language = get_language()
#    try:
#        activate(language)
#        text = gettext('Привет')
#    finally:
#        activate(cur_language)
#        return text


def site_map(request):
    return render(request, 'main_page/sitemap.xml', content_type='text/xml')
