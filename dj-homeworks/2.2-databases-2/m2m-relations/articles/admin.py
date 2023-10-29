from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            if not form.cleaned_data['article']:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormSet


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]




