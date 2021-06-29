""" Registers models on the admin Page. """

from django.contrib import admin

from .models import AdvisoryMember, Finance, Universall, Position, Conduct

admin.site.register(AdvisoryMember)
""" Register the AdvisoryMember Model on admin page. """
admin.site.register(Finance)
""" Register the Finance Model on admin page. """
admin.site.register(Universall)
""" Register the Universall Model on admin page. """
admin.site.register(Position)
""" Register the Position Model on admin page. """
admin.site.register(Conduct)
""" Register the Conduct Model on admin page. """
