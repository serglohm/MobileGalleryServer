from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.finders import BaseStorageFinder
from django.conf import settings

class StaticRootFinder(BaseStorageFinder):
    storage = FileSystemStorage(settings.STATIC_ROOT, settings.STATIC_URL)

class MediaRootFinder(BaseStorageFinder):
    storage = FileSystemStorage(settings.MEDIA_ROOT, settings.MEDIA_URL)