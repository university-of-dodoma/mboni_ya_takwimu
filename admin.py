from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Dataset
from .models import User
from .models import Comment
from .models import Post
from .models import Post1

admin.site.register(Question)
admin.site.register(Dataset)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Post1)