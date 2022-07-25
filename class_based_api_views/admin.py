from django.contrib import admin
from .models import Transformer, Book
from guardian.admin import GuardedModelAdmin


class TransformerAdmin(GuardedModelAdmin):
    pass


admin.site.register(Transformer, TransformerAdmin)
admin.site.register(Book)
