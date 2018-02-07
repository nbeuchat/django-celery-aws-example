# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Visit

@shared_task
def add_analytics(ua):
    print('add analytics task')
    #v = Visit(useragent=ua)
    #v.save()
    #visit_count = Visit.objects.count()
    #print('Added visit #{}, user-agent: {}'.format(visit_count,ua))
    print('New visit, user-agent: {}'.format(ua))
    #return visit_count