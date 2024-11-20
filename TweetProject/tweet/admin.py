from django.contrib import admin
from .models import Tweet

# After making the model,you have to make changes in the admin panel as well.


admin.site.register(Tweet)