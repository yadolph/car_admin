from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['brand', 'model', 'review_count', ]
    search_fields = ['brand', 'model']
    ordering = ['-id']

    pass


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    model = Review
    list_display = ['car', 'title', ]
    search_fields = ['title']
    ordering = ['-id']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
