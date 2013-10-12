# -*- coding: utf8 -*-
from django.contrib import admin
from django import forms
from models import *

class ArtworksInline(admin.TabularInline):
    model = Artwork
    extra = 3

class PainterAdmin(admin.ModelAdmin):
    list_display    = ["name"]
    list_display_links = ["name"]
    #list_editable = ("name")
    #list_filter     = []
    fieldsets       = (
        ("Информация о художнике", {"fields":["name", "slug"]}),
    )
    inlines = [ArtworksInline]

admin.site.register(Painter, PainterAdmin)