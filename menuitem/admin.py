from django.contrib import admin
from .models import Menuitem
from .models import Itemlist
from .models import Feedback
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Menuitem)
# Register your models here.
admin.site.register(Itemlist)


admin.site.register(Feedback)
admin.site.register(UserProfile)
