from django.contrib import admin
from polls.models import Thing, Ingredient

class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description','user',)
    prepopulated_fields = {'slug': ('name',)}

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

# Register your models here.
admin.site.register(Thing, ThingAdmin)
admin.site.register(Ingredient, IngredientAdmin)