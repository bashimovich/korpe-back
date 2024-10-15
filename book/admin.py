from django import forms
from .models import Book, CategoryKids

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    category = forms.ModelChoiceField(
        queryset=CategoryKids.objects.all(),
        label="Category",
        widget=forms.Select,
    )
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = self.get_category_label
    def get_category_label(self, obj):
        return f"{obj.name_tm} - {obj.get_category_type_display()}"
from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    form = BookForm
admin.site.register(Book, BookAdmin)