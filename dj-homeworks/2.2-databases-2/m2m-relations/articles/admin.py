from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        count_main_tag = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                count_main_tag += 1
            if count_main_tag > 1:
                raise ValidationError('Должен быть только один основной тэг')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormSet


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]




