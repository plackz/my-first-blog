from django.contrib import admin
from .models import Post, Comment

'''
# divider section
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author',
                                        'title',
                                        'text',
                                        ]}),
        ('Date information', {'fields': ['created_date',
                                        'published_date',
                                        ]}),
    ]
'''
# only use if using divider section
# admin.site.register(Post, PostAdmin)
admin.site.register(Post) 
admin.site.register(Comment)


