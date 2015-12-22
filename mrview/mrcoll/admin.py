from django.contrib import admin

from .models import AudioUnit, Brand, Tag, Effect, Instrument

admin.site.register(AudioUnit)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(Effect)
admin.site.register(Instrument)
