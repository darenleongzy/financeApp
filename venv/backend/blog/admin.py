from django.contrib import admin
from .models import Blog # add this

class BlogAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Blog, BlogAdmin) # add this
