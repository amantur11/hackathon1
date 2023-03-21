import logging

from django.http.response import HttpResponse

logger = logging.getLogger('main')

def login_view(request):
    logger.info('hello world!')
    return HttpResponse("<h1>Test</h1>") 