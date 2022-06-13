from django.contrib import admin
from .models import Machine
from .models import Routeur
from .models import Switch
from .models import Serveur
admin.site.register(Machine)
admin.site.register(Routeur)
admin.site.register(Switch)
admin.site.register(Serveur)
# Register your models here.
