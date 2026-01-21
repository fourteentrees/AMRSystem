from django.db.models import ObjectDoesNotExist
from django.shortcuts import render
from .models import AdCrawl
from django.http import HttpResponse, JsonResponse

def getcrawlcontent(request, id):
    try:
        # pyright shut the fuck up this works
        crawl = AdCrawl.objects.filter(id=id).first()
        return HttpResponse(crawl.content, content_type="text/plain")
    except ObjectDoesNotExist:
        # respond with a 404
        return JsonResponse({"message": "No such crawl exists. Check the ID and try again."}, status=404)

def detailjson(request, id):
    try:
        # pyright shut the fuck up it works
        crawl = AdCrawl.objects.filter(id=id).first()
        data = {
            "id": crawl.id,
            "content": crawl.content,
            "campaign": crawl.campaign,
            "run_through": crawl.run_through,
            "active": crawl.active,
        }

        return JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error", "code": "404", "message": "No such crawl exists"}, status=404)