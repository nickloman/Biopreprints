
from django.shortcuts import render_to_response

from preprint.journals.models import Journal
from preprint.servers.models import PreprintServer
from preprint.faq.models import FAQEntry

def startpage(request):
    j = Journal.objects.all()
    s = PreprintServer.objects.all()
    f = FAQEntry.objects.all()

    return render_to_response('index.html', {'j' : j, 's' : s, 'f' : f})
