from django.contrib import admin

# Register your models here.
from .models import PostModel, CommentModel

admin.site.register(PostModel)
admin.site.register(CommentModel)