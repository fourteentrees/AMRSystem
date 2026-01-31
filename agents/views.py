from django.shortcuts import render
from django.http import JsonResponse
from .models import Agent
from songrequests.models import SongRequest
from adcrawls.models import AdCrawl
from django.utils import timezone

def api_root(request):
    api_key = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
    context = {'api_key': api_key}

    # search for the agent
    try:
        agent = Agent.objects.get(api_key=api_key)
        context['agent'] = agent
        data = JsonResponse({
            'code': 200,
            'http': 'OK',
            'message': f'your key works and i think u are the agent with id {agent.id}'
        })
        return data
    except Agent.DoesNotExist:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'Your API key sucks, check it against the ones in the admin panel.'
        })
        return data

def requests_since_last_poll(request):
    api_key = request.META['HTTP_AUTHORIZATION'].split(' ')[1]

    # search for the agent
    try:
        agent = Agent.objects.get(api_key=api_key)
    except Agent.DoesNotExist:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'Your API key sucks, check it against the ones in the admin panel.'
        })
        return data

    last_polled = agent.last_polled_songrequests
    new_requests = SongRequest.objects.filter(created_at=last_polled)

    requests_data = [
        {
            'id': req.id,
            'song': {
                'title': req.song.title,
                'artist': req.song.artist,
                'album': req.song.album,
                'url': req.song.url
            },
            'requested_by': req.requested_by,
            'created_at': req.created_at.isoformat()
        }
        for req in new_requests
    ]

    # Update the agent's last_polled time
    agent.last_polled = timezone.now()
    agent.save()

    data = JsonResponse({
        'code': 200,
        'http': 'OK',
        'new_requests': requests_data
    })
    return data

def random_ad_crawl(request, last_id):
    if 'HTTP_AUTHORIZATION' not in request.META:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'pls give api key!!!!!'
        })
        return data

    api_key = request.META['HTTP_AUTHORIZATION'].split(' ')[1]

    # search for the agent
    try:
        agent = Agent.objects.get(api_key=api_key)
    except Agent.DoesNotExist:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'Your API key sucks, check it against the ones in the admin panel.'
        })
        return data
    
    if not last_id:
        data = JsonResponse({
            'code': 400,
            'http': 'Bad Request',
            'message': 'last_id isnt a suggestion, give me one. if you don\'t have one, give me 0.'
        })
        return data


    # get a random ad crawl where the id is not the same one as last_id
    ad_crawls = AdCrawl.objects.exclude(id=last_id) if last_id != '0' else AdCrawl.objects.all()
    if not ad_crawls.exists():
        data = JsonResponse({
            'code': 404,
            'http': 'Not Found',
            'message': 'No ad crawls available. Add more in the admin UI'
        })
        return data

    random_crawl = ad_crawls.order_by('?').first()
    crawl_data = {
        'id': random_crawl.id,
        'content': random_crawl.content,
        'created_at': random_crawl.created_at.isoformat()
    }

    data = JsonResponse({
        'code': 200,
        'http': 'OK',
        'ad_crawl': crawl_data
    })
    return data

def random_ad_crawl_non_duplicate_safe(request):
    # Like random_ad_crawl, but it doesn't take a last_id parameter and always returns a random ad crawl
    if 'HTTP_AUTHORIZATION' not in request.META:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'pls give api key!!!!!'
        })
        return data
    api_key = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
    # search for the agent
    try:
        agent = Agent.objects.get(api_key=api_key)
    except Agent.DoesNotExist:
        data = JsonResponse({
            'code': 401,
            'http': 'Unauthorized',
            'message': 'Your API key sucks, check it against the ones in the admin panel.'
        })
        return data
    ad_crawls = AdCrawl.objects.all()
    if not ad_crawls.exists():
        data = JsonResponse({
            'code': 404,
            'http': 'Not Found',
            'message': 'No ad crawls available. Add more in the admin UI'
        })
        return data
    random_crawl = ad_crawls.order_by('?').first()
    crawl_data = {
        'id': random_crawl.id,
        'content': random_crawl.content,
        'created_at': random_crawl.created_at.isoformat()
    }
    data = JsonResponse({
        'code': 200,
        'http': 'OK',
        'ad_crawl': crawl_data
    })
    return data