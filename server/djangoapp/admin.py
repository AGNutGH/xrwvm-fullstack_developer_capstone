from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class allows us to edit CarModel records 
# from within the CarMake page
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    # Added 'fuel_type' to list_display so it appears as a column
    list_display = ['name', 'car_make', 'type', 'year', 'fuel_type', 'dealer_id']
    # Added 'fuel_type' to filters for better search capability
    list_filter = ['type', 'year', 'car_make', 'fuel_type']
    search_fields = ['name', 'car_make__name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    # Added 'country_of_origin' to reflect your custom model field
    list_display = ['name', 'description', 'country_of_origin']
    search_fields = ['name', 'country_of_origin']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
