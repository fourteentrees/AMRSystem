from typing import Any
from .models import AdCrawl
from django.http import HttpResponse, JsonResponse

def getcrawlcontent(request, id: int):
        # pyright shut the fuck up this works
        crawl = AdCrawl.objects.filter(id=id).first()
        if crawl == None:
            return HttpResponse("No such crawl exists, check the ID and try again", status=404, content_type="text/plain")
        return HttpResponse(crawl.content, content_type="text/plain")

def detailjson(request, id: int):
        # pyright shut the fuck up it works
        crawl = AdCrawl.objects.filter(id=id).first()
        if crawl == None:
            data = {"content": "No such crawl exists. Check the ID and try again."}
            return JsonResponse(data)
        data = {
            "id": crawl.id,
            "content": crawl.content,
            "campaign": crawl.campaign,
            "run_through": crawl.run_through,
            "active": crawl.active,
        }

        return JsonResponse(data)