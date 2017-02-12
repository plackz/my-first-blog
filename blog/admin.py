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
#admin.site.register(Post)
#admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''# FIX: not sure why date_hierarchy isn't working. could be related to it's a datetime field
    vs a date field
    '''
    #date_hierarchy = 'created_date'

    search_fields = ['title', 'text', 'author']
    list_display = ('title', 'author', 'text', 'created_date', 'published_date')
    list_filter = ['created_date', 'published_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['post', 'author', 'text', 'created_date']
    list_display = ('post', 'author', 'text', 'created_date', 'approved_comment')
    list_filter = ['created_date', 'approved_comment','author']
