from django.contrib import admin
from .models import posting

# Register your models here.
class postingAdmin(admin.ModelAdmin):
    feilds = ["posting_title",
            "posting_date",
            "posting_context"]
admin.site.register(posting, postingAdmin)
