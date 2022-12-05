from django.contrib import admin

from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        base = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] == True:
                base += 1
        if base == 0:
            raise ValidationError('Укажите основной раздел')
        if base > 1:
            raise ValidationError('основной раздел может быть только один')
        return super().clean()
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInLineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
