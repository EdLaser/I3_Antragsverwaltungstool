from django.contrib import admin

from .models import AdvisoryMember, Finance, Universall, Position, Conduct

# Register your models here.
admin.site.register(AdvisoryMember)
admin.site.register(Finance)
admin.site.register(Universall)
admin.site.register(Position)
admin.site.register(Conduct)