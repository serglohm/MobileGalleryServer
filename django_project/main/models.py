# -*- coding: utf8 -*-
from django.db import models
from django.conf import settings
import os

class Painter(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    enable = models.BooleanField(default=True)

    class Meta:
        db_table = "gallery_painters"

    def __unicode__(self):
        return u"%s" % self.name


class Artwork(models.Model):
    def get_path(self, filename):
        base_gallery_path = os.path.join("gallery", self.painter.slug)

        for i in range(1, 1000):
            ext = os.path.splitext(filename)[-1]
            new_filename = "%s%s" % (i, ext)
            file_path = os.path.join(base_gallery_path, new_filename)
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)
            if not os.path.exists(full_path):
                break

        return full_path

    name = models.CharField(max_length=255, blank=True)
    painter = models.ForeignKey(Painter)
    picture = models.ImageField(upload_to=get_path)
    enable = models.BooleanField(default=True)

    class Meta:
        db_table = "gallery_artworks"

    def __unicode__(self):
        return u"%s: %s" % (self.painter.name, self.name)


### Signals ###
def create_painter_folder(instance, created, **kwargs):
    if created:
        dir_path = os.path.join(settings.MEDIA_ROOT, "gallery", instance.slug)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

models.signals.post_save.connect(create_painter_folder, sender=Painter, dispatch_uid="Painter.create_painter_folder")