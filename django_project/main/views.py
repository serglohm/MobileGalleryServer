# -*- coding: utf8 -*-
from django.views.generic import View, ListView, TemplateView
from django.contrib import auth
from django.views.generic.base import TemplateResponseMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from operator import or_, and_
from django.core import serializers
from models import *
import json
from collections import defaultdict


class GetPainters(View):
    def get(self, request):
        id = request.GET.get("id", "").strip()
        queries = []
        queries.append(Q(enable=True))
        if id:
            queries.append(Q(id=int(id)))

        painters = Painter.objects.filter(*queries).values_list("id", "name")
        return HttpResponse(json.dumps(list(painters)), content_type='application/json')



class GetArtworks(View):
    def get(self, request):
        id = request.GET.get("id", "").strip()
        queries = []
        queries.append(Q(enable=True))
        if id:
            queries.append(Q(id=int(id)))

        artworks = Artwork.objects.filter(*queries).values("id", "name")
        artworks = [dict(id=item.id, name=item.name) for item in artworks]
        return HttpResponse(json.dumps(artworks), content_type='application/json')