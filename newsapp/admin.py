from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import NewsUnit

class NewsUnitAdmin(admin.ModelAdmin):
    list_display =('category', 'title', 'author', 'pubtime', 'enabled', 'press')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            return AuthorChoiceField(queryset=User.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class AuthorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.__str__()

admin.site.register(NewsUnit, NewsUnitAdmin)