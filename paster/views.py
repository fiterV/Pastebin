from django.shortcuts import render, Http404, HttpResponse, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Paste
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class PasteCBView(View):
    def get(self, request, code, *args, **kwargs):
        obj = Paste.objects.filter(shortcode=code)
        if len(obj)==0:
            raise Http404("Paste not found")
        obj = obj[0]
        context = {
            'text':obj.text,
            'title':obj.title,
            'pastes': Paste.objects.order_by('-pk')[:10],
            'hostname': request.get_host(),
        }
        return render(request, "paster/showPaste.html", context)


class PasteCBCreate(View):
    def get(self, request, *args, **kwargs):
        context = {
            'pastes' : Paste.objects.order_by('-pk')[:10],
            'hostname' : request.get_host(),

        }
        return render(request, "paster/createPaste.html", context)
    def post(self, request, *args, **kwargs):
        text = request.POST['text']
        title = request.POST['title']
        p = Paste(text = text, title=title)
        p.save()
        created = 'http://'+request.get_host()+'/'+p.shortcode
        print('Paste create , and take your redirect to {}'.format(created))
        return HttpResponseRedirect(created)

        return HttpResponse("hey there "+p.shortcode + " title = " + p.title)


class Archive(View):
    def get(self, request, page, *args, **kwargs):
        pastes = Paste.objects.order_by('-pk')
        paginator = Paginator(pastes, 10)


        try:
            contacts = paginator.page(page)
        except EmptyPage:
            raise Http404("That page does not exist")

        context = {
            'pastes': contacts,
            'contacts' : contacts,
	    'hostname' : request.get_host(),
        }
        return render(request, "paster/archive.html", context)
