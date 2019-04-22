# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post


# Create your views here.


def homepage(request):
   template = get_template('base.html')
   posts = Post.objects.all()
   #post_lists = list()
   #for count, post in enumerate(posts):
   #   post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
   #   post_lists.append("<small>"+str(post.body.encode('utf-8'))+"</small><br><br>")
   #return HttpResponse(post_lists)
   now = datetime.now()
   html = template.render(locals())
   return HttpResponse(html)


def showpost(request, slug):
   template = get_template('post.html')
   try:
      post = Post.objects.get(slug=slug)
      if post != None:
         html = template.render(locals())
         return HttpResponse(html)
   except:
      return redirect('/')
