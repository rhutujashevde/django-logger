# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
import logging
from django.http.response import JsonResponse


logger = logging.getLogger("info")

def post_list(request):
    try:
        raise Exception("lalal")
        posts = Post.objects.filter(
            published_date__lte=timezone.now()).order_by('published_date')
        logger.info('Some 111 message')
        return render(request, 'blog/post_list.html', {"posts": posts})
    except Exception as e:
        logger.error(e)
        return render(request, 'blog/post_list.html', {"posts": {}})
    
def sample_view(request):
    print request.GET
    return JsonResponse({"status": "okay"})